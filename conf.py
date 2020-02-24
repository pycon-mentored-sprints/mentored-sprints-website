# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "PyCon Mentored Sprint for Diverse Beginners"
copyright = "2019-2020, Menored Sprints organising team"
author = "Tania Allard"

# The short X.Y version
version = "2020"
# The full version, including alpha/beta/rc tags
release = ""

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["sphinx.ext.githubpages"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.

master_doc = "index"

html_sidebars = {
    "**": [
        "about.html",
        "localtoc.html",
        "navigation.html",
        "relations.html",
        "searchbox.html",
        "sidebar.html",
    ]
}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"

html_theme_options = {
    "github_user": "pycon-mentored-sprints",
    "github_repo": "mentored-sprints-website",
    "github_type": "star",
    "github_banner": True,
    "show_relbars": True,
    "font_family": "Montserrat, Georgia, sans",
    "head_font_family": "Sulphur Point, Georgia, serif",
    "code_font_family": "'Source Code Pro', 'Consolas', monospace",
    "logo": "https://raw.githubusercontent.com/pycon-mentored-sprints/digital-assets/master/logos/blue-pink-text.svg",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
