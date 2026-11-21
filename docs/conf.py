# Sphinx configuration for seminal
import os
import shutil
import sys

sys.path.insert(0, os.path.abspath("../src"))

import seminal  # noqa: E402

project = "seminal"
author = "Leonid Shpaner"
copyright = "2026, Leon Shpaner"
release = seminal.__version__
version = release

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx_copybutton",
    "myst_nb",
]

# Notebooks live in ../notebooks (committed without outputs). They are copied
# into the docs tree and executed by myst-nb at build time, so the published
# pages show outputs. Both need data/processed/, built by
# `make data_gen preprocess` (the docs workflow does this before building).
_NB_SRC = os.path.abspath("../notebooks")
_NB_DST = os.path.abspath("_notebooks")
os.makedirs(_NB_DST, exist_ok=True)
for _nb in ["00_quickstart.ipynb", "01_reproduce_tradewell.ipynb"]:
    shutil.copy2(os.path.join(_NB_SRC, _nb), os.path.join(_NB_DST, _nb))

# The notebooks are written to run from notebooks/ and refer to ../data and
# ../preprocessing.py. Executed from docs/_notebooks/ those resolve to docs/,
# so link them through.
for _name in ["data", "preprocessing.py"]:
    _link = os.path.abspath(_name)
    if not os.path.lexists(_link):
        os.symlink(os.path.abspath(os.path.join("..", _name)), _link)

nb_execution_mode = "force"
nb_execution_timeout = 900
nb_execution_raise_on_error = True
nb_merge_streams = True

napoleon_numpy_docstring = True
napoleon_google_docstring = False
autodoc_member_order = "bysource"

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "jupyter_execute"]

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_title = f"seminal {release}"
html_theme_options = {"navigation_depth": 3, "collapse_navigation": False}

# copy buttons skip prompts and output markers
copybutton_prompt_text = r">>> |\.\.\. |\$ "
copybutton_prompt_is_regexp = True

rst_epilog = f"""
.. |version_str| replace:: {release}
"""
