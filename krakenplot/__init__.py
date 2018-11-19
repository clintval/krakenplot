import csv
import re

from pathlib import Path
from typing import Mapping

import ete3
import toytree
from toytree.Toytree import ToyTree

__all__ = ['KrakenSummary']

INDENT_UNIT: int = 2


class KrakenSummary(object):
    """Visualize and interrogate the summary report from the taxonomic classifier Kraken.

    Args:
        infile: The path to the Kraken summary metric text file.
        ignore_unclassified: Whether to ignore *unclassified* assignments.

    """
    def __init__(self, infile: Path, ignore_unclassified: bool = False) -> None:
        self.infile = Path(infile).expanduser().resolve()
        self.ignore_unclassified = ignore_unclassified

        nodes: Mapping[int, ete3.coretype.tree.TreeNode] = {}
        current_root_index: int = 0
        re_indent = re.compile(r'^\s*')

        tree: ete3.coretype.tree.TreeNode = ete3.Tree()
        root = tree.add_child(name='root')

        nodes[current_root_index] = root

        with self.infile.open() as handle:
            for line in csv.reader(handle, delimiter='\t'):
                fraction, cumulative, count, order, tax_id, taxa_entry = line
                indents = re_indent.match(taxa_entry)

                if not indents:
                    continue
                else:
                    indent_size = len(indents.group())
                taxa_name = re_indent.sub('', taxa_entry)

                if taxa_name == 'root':
                    continue

                if not ignore_unclassified and taxa_name == 'unclassified':
                    tree.add_child(name='unclassified')

                if indent_size >= current_root_index:
                    parent = nodes[current_root_index]
                else:
                    parent = nodes[indent_size - INDENT_UNIT]

                child = parent.add_child(name=taxa_name)
                current_root_index = indent_size
                nodes[current_root_index] = child

        self.tree = tree

    @property
    def newick(self) -> str:
        """Return a Newick string of this phylogeny."""
        newick: str = self.tree.write()
        return newick

    @property
    def toytree(self) -> ToyTree:
        """Return a ToyTree object of this phylogeny."""
        tree: ToyTree = toytree.tree(self.newick)
        return tree

    def __repr__(self) -> str:
        return (
            f'{self.__class__.__name__}('
            f'"{self.infile}", '
            f'ignore_unclassified={self.ignore_unclassified})'
        )
