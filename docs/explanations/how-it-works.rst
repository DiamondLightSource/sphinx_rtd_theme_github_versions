How it works
============

The theme works by injecting some javascript that populates the version list
at runtime. This javascript does the following:

- Fetch the set of all directories in the ``gh-pages`` branch of the ``project`` repo in `github_org`
- Take the `versions_branches`, and add the names of all the tags in that repo
- Make a link to github.io for each version that has a directory in ``gh-pages``

You should make sure that there are appropriately named branches in the
``gh-pages`` branch by doing something like
https://github.com/dls-controls/sphinx_rtd_theme_github_versions/blob/master/.github/workflows/docs.yml