from pathlib import Path

from sphinx_rtd_theme import setup as base_setup

from ._version_git import __version__


# See https://www.sphinx-doc.org/en/master/development/theming.html
#         #distribute-your-theme-as-a-python-package
def setup(app):
    # Register the theme that can be referenced without adding a theme path
    app.add_html_theme(
        "sphinx_rtd_theme_github_versions", Path(__file__).absolute().parent
    )
    return base_setup(app)


__all__ = ["setup", "__version__"]
