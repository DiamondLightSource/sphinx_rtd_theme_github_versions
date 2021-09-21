from io import StringIO
from pathlib import Path

import pytest
from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx("html", testroot="dls-defaults")
def test_dls_defaults(app: SphinxTestApp, status: StringIO, warning: StringIO) -> None:
    app.warningiserror = True
    assert app.builder
    app.builder.build_all()
    html = open(Path(app.outdir) / "index.html").read()
    assert "var versions = ['main', 'master'];" in html
    assert (
        '<div class="wy-side-nav-search"  style="background: rgb(7, 43, 93)" >' in html
    )
