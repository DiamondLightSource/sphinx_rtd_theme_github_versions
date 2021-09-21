from io import StringIO
from pathlib import Path

import pytest
from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx("html", testroot="dls-defaults")
def test_dls_defaults(app: SphinxTestApp, status: StringIO, warning: StringIO) -> None:
    app.warningiserror = True
    assert app.builder
    app.builder.build_all()
    content = open(Path(app.outdir) / "index.html").read()
    print(content)
    assert False
