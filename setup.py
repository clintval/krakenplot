import setuptools

from pathlib import Path
from setuptools import find_packages

PACKAGE = 'krakenplot'
VERSION = '0.1.0'

setuptools.setup(
    name='krakenplot',
    version=VERSION,
    author='clintval',
    author_email='valentine.clint@gmail.com',
    description='Plot the summary output from Kraken.',
    url=f'https://github.com/clintval/{PACKAGE}',
    download_url=f'https://github.com/clintval/{PACKAGE}/archive/v{VERSION}.tar.gz',
    long_description=Path('README.md').read_text(),
    long_description_content_type='text/markdown',
    license='MIT',
    zip_safe=False,
    packages=[PACKAGE],
    install_requires=['ete3', 'numpy', 'toytree'],
    keywords='kraken tree phylogeny taxonomy classification',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    project_urls={
        'Documentation': f'https://{PACKAGE}.readthedocs.io',
        'Issue-Tracker': f'https://github.com/clintval/{PACKAGE}/issues',
    },
)
