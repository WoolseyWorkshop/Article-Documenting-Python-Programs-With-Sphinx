# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'My Sphinx Example Project'
copyright = '2020, Woolsey Workshop'
author = 'John Woolsey'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Disable prepending module names
add_module_names = False

# Sort members by type
autodoc_member_order = 'groupwise'

# Document __init__, __repr__, and __str__ methods
def skip(app, what, name, obj, would_skip, options):
    if name in ("__init__", "__repr__", "__str__"):
        return False
    return would_skip

def setup(app):
    app.connect("autodoc-skip-member", skip)

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
