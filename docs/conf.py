# docs/conf.py

project = "GLIMS Submissions"
author = "NSIDC"
copyright = "2026, NSIDC"

version = "1.0"
release = "1.0"

extensions = [
    "sphinx.ext.autodoc",       # pull docstrings from Python code
    "sphinx.ext.napoleon",      # Google/NumPy style docstrings
    "sphinx.ext.viewcode",      # links to source code
    "myst_parser",
]

# If using Markdown (.md) files
source_suffix = {
    ".md": "markdown",
}

# Root doc
root_doc = "index"

# Theme — rtd theme is the classic choice
html_theme = "sphinx_rtd_theme"

# If you have a logo
# html_logo = "_static/logo.png"

# Static files
html_static_path = ["_static"]
