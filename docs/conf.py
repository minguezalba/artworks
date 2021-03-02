"""Sphinx configuration."""
from datetime import datetime
import os
import sys
sys.path.insert(0, os.path.abspath('..'))


project = "artworks"
author = "Alba Mínguez Sánchez"
copyright = f"{datetime.now().year}, {author}"
extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon", "sphinx_autodoc_typehints"]
