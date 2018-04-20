# -*- coding: utf-8 -*-

# -- Path setup --------------------------------------------------------------
import sys, os
sys.path.insert(0, os.path.abspath('../../mymodule'))

import colorbar

# -- Project information -----------------------------------------------------
project = 'MyModule'
copyright = '2018, AuthorName'
author = 'AuthorName'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.viewcode',
]

autosummary_generate = True
autodoc_default_flags = ['members', 'undoc-members']
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']


source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'bizstyle' #'sphinxdoc'
html_static_path = ['_static']
htmlhelp_basename = 'MyModuledoc'


