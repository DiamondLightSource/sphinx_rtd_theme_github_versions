Configure the theme
===================

The following options can be defined in your project's ``conf.py`` file, using
the :confval:`html_theme_options <sphinx:html_theme_options>` configuration option.

For example:

.. code-block:: python

    html_theme_options = {
        'versions_branches': 'main master',
        'github_org': 'dls-controls',
    }


Theme Options
-------------

.. confval:: versions_branches

    The branches that should appear top of the list of versions before all the
    tags. Should be supplied as a space separated string.

    :type: str
    :default: ``"main master"``

.. confval:: github_org

    The github organization that the repo is hosted under

    :type: str
    :default: ``"dls-controls"``

All other `sphinx_rtd_theme options <sphinx_rtd_theme:configuring>` like
:std:confval:`style_nav_header_background` are also supported.
