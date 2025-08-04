import os

project = 'Aurora Agent User Manual'
copyright = '2025, Nextron Systems GmbH'
author = 'Nextron Systems GmbH'
version="1.0"
extensions = [
    'sphinx.ext.autosectionlabel',
]
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
language = 'en'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.venv/*']
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'prev_next_buttons_location': 'both',
    'style_external_links': True
}
html_logo = "images/html/aurora-logo.png"
html_favicon = "images/html/favicon.ico"
html_static_path = ['_static']
html_css_files = ['css/custom.css',]
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "")
if os.environ.get("READTHEDOCS", "") == "True":
    if "html_context" not in globals():
        html_context = {}
    html_context["READTHEDOCS"] = True
html_show_sourcelink = False
epub_title = project
epub_exclude_files = ['search.html']
intersphinx_mapping = {'https://docs.python.org/': None}
smartquotes = False
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 4
suppress_warnings = ["epub.unknown_project_files"]
