Installation
============

.. note::

    For installation inside DLS, please see the internal documentation on
    ``dls-python3`` and ``pipenv``. Although these instructions will work
    inside DLS, they are intended for external use.

    If you want to contribute to the library itself, please follow
    the `../reference/contributing` instructions.


Check your version of python
----------------------------

You will need python 3.7 or later. You can check your version of python by
typing into a terminal::

    python3 --version


Create a virtual environment
----------------------------

It is recommended that you install into a “virtual environment” so this
installation will not interfere with any existing Python software::

    python3 -m venv /path/to/venv
    source /path/to/venv/bin/activate


Installing the library
----------------------

You can now use ``pip`` to install the library::

    python3 -m pip install sphinx_rtd_theme_github_versions

If you require a feature that is not currently released you can also install
from github::

    python3 -m pip install git+git://github.com/DiamondLightSource/sphinx_rtd_theme_github_versions.git

The library should now be installed and the commandline interface on your path.
You can check the version that has been installed by typing::

    sphinx_rtd_theme_github_versions --version

Including in Sphinx Documentation
---------------------------------

Set the theme by declaring the `html_theme` in your ``conf.py`` file:

.. code-block:: python

    html_theme = "sphinx_rtd_theme_github_versions"

See `../how-to/configure-the-theme` for more details on configuring the theme

Deployment
----------

At development time you will not see any version section as there is only one
version of the documentation. For it to be active there must be a
``versions.txt`` file alongside the built documentation.

See `../explanations/how-it-works` for details on how to add this.
