How it works
============

The theme comes in two parts:

- A commandline script that generates a ``versions.txt`` file at documentation
  build time
- A bit of javascript that populates the versions section of the
  sidebar at runtime

Commandline script
------------------

This works by writing a ``versions.txt`` file alongside the build documentation
directories that are pushed to the ``gh-pages`` branch. These are ordered:

- main or master branch
- tags in descending order
- other branches

This generation should be run at CI time using something like this:

https://github.com/dls-controls/sphinx_rtd_theme_github_versions/blob/master/.github/workflows/docs.yml

Javascript population
---------------------

This works by fetching ``../versions.txt`` and populating an ``Other Versions``
section of the side-bar with the contents. If the fetch fails the that section
is hidden.