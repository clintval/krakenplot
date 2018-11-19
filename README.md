# krakenplot

[![Testing Status](https://travis-ci.org/clintval/krakenplot.svg?branch=master)](https://travis-ci.org/clintval/krakenplot)
[![codecov](https://codecov.io/gh/clintval/krakenplot/branch/master/graph/badge.svg)](https://codecov.io/gh/clintval/krakenplot)
[![Documentation Build Status](https://readthedocs.org/projects/krakenplot/badge/?version=latest)](https://krakenplot.readthedocs.io/en/latest/?badge=latest)
[![PyPi Release](https://badge.fury.io/py/krakenplot.svg)](https://badge.fury.io/py/krakenplot)
[![Python Versions](https://img.shields.io/pypi/pyversions/krakenplot.svg)](https://pypi.python.org/pypi/krakenplot/)
[![MyPy Checked](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

Analysis and plotting library for base substitution spectra and signatures.

```bash
❯ pip install krakenplot
```

Features that may be implemented include:

- Bar plot or scatter plot integration showing the magnitude of sequences assigned to each node in the phylogenetic tree.
- Method for _forcing_ all counts either up or down a linear branch to simplify sequence classification.
- Clade collapsing based on taxonomic assignment and phylogenetic order.

Read the documentation at: [krakenplot.readthedocs.io](http://krakenplot.readthedocs.io/)

```python
>>> from krakenplot import KrakenSummary
>>> summary = KrakenSummary('sample-report.txt')
>>> summary.newick
'(((Mus musculus musculus:1):1,(Rattus norvegicus albus:1):1,Homo sapiens:1),unclassified:1);'
```

```python
>>> canvas, coords = summary.toytree.draw(
>>>     width=500,
>>>     height=175,
>>>     tip_labels_color=['red', 'black', 'black', 'black'],
>>>     # Make Carl Linnaeus proud and italicize those species names!
>>>     tip_labels=[f'<i>{l}</i>' for l in summary.toytree.get_tip_labels()])
```

![Simple Tree Example](docs/img/simple-tree.png "Simple Tree Example")