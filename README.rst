# Build Setup

Setup for read the docs and github was found here:
https://docs.readthedocs.io/en/stable/tutorial/

Github repository:
https://github.com/MatticusPrime29/plotvision-docs

Documentation for documentation building with Sphinx

Steps to build on local machine:
1. Clone repository and navigate to the root folder
2. Assuming you already have python, run 'pip install sphinx'
3. then run 'pip install sphinx-rtd-theme'
4. navigate to the docs folder
5. Create a directory called '_build'
6. run 'sphinx-build -b html source _build'
7. This will generate html files which can be opened for viewing during development