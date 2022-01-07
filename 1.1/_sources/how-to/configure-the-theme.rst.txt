Configure the theme
===================

Theme options can be defined in your project's ``conf.py`` file, using the
:confval:`html_theme_options <sphinx:html_theme_options>` configuration option.

This theme does not add any options, but all `sphinx_rtd_theme options
<sphinx_rtd_theme:configuring>` like :std:confval:`style_nav_header_background`
are supported.

For example:

.. code-block:: python

    html_theme_options = {
        "style_nav_header_background": "rgb(7, 43, 93)"
    }
