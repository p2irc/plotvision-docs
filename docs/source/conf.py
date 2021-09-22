# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'PlotVision'
copyright = 'University of Saskatchewan'
author = 'William van der Kamp, Danny Huang, Josh Kocur, Travis Gray, Aristides Mairena Flores, Steven Xue, Matthew Martens'

release = '0.4'
version = '0.4.10'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
