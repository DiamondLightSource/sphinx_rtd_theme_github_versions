from io import StringIO
from pathlib import Path
from unittest.mock import patch

import pytest
from sphinx.testing.util import SphinxTestApp

from sphinx_rtd_theme_github_versions.__main__ import get_sorted_tags_list, main


@pytest.mark.sphinx("html", testroot="dls-defaults")
def test_dls_defaults(app: SphinxTestApp, status: StringIO, warning: StringIO) -> None:
    app.warningiserror = True
    assert app.builder
    app.builder.build_all()
    html = open(Path(app.outdir) / "index.html").read()
    assert "other-versions-dl" in html
    assert (
        '<div class="wy-side-nav-search"  style="background: rgb(7, 43, 93)" >' in html
    )


@patch("sphinx_rtd_theme_github_versions.__main__.get_sorted_tags_list")
@patch("sphinx_rtd_theme_github_versions.__main__.get_branch_contents")
def test_versions_txt(get_branch_contents, get_sorted_tags_list, tmp_path: Path):
    (tmp_path / "0.3").mkdir()
    get_branch_contents.return_value = ["0.1", "master", "0.2", "wip"]
    get_sorted_tags_list.return_value = ["0.3", "0.2", "0.1"]
    main([str(tmp_path)])
    lines = (tmp_path / "versions.txt").read_text().splitlines()
    assert lines == ["master", "0.3", "0.2", "0.1", "wip"]


def test_git_tags():
    assert "0.2" in get_sorted_tags_list()


def test_no_gh_pages(tmp_path: Path):
    (tmp_path / "master").mkdir()
    main([str(tmp_path), "--remote", "a-non-existant-remote"])
    lines = (tmp_path / "versions.txt").read_text().splitlines()
    assert lines == ["master"]
