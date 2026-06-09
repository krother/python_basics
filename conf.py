# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Teaching Programming'
copyright = '2026, Kristian Rother'
author = 'Kristian Rother'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_design',
    'sphinx_copybutton',
    'sphinx.ext.todo',
    'myst_parser',
    ]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'learning_goals.md', 'README.md']

language = 'ls'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_theme_path = ['themes']
html_static_path = ['_static']
#html_logo = "_static/banner_wide.svg"
html_favicon = "_static/favicon.ico"

html_css_files = [
    "academis.css",
]
html_theme_options = {
    "source_repository": "https://github.com/krother/python_basics",
    "source_branch": "main",
    "source_directory": "",
}
