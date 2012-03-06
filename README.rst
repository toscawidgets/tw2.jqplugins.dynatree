tw2.jqplugins.dynatree
=========================

:Author: Ralph Bean <rbean@redhat.com>

.. comment: split here

.. _toscawidgets2 (tw2): http://toscawidgets.org/documentation/tw2.core/
.. _dynatree: http://code.google.com/p/dynatree/

tw2.jqplugins.dynatree is a `toscawidgets2 (tw2)`_ wrapper for `dynatree`_.

Live Demo
---------
Peep the `live demonstration <http://tw2-demos.threebean.org/module?module=tw2.jqplugins.dynatree>`_.

Links
-----
Get the `source from github <http://github.com/toscawidgets/tw2.jqplugins.dynatree>`_.

`PyPI page <http://pypi.python.org/pypi/tw2.jqplugins.dynatree>`_
and `bugs <http://github.com/toscawidgets/tw2.jqplugins.dynatree/issues/>`_

Description
-----------

`toscawidgets2 (tw2)`_ aims to be a practical and useful widgets framework
that helps people build interactive websites with compelling features, faster
and easier. Widgets are re-usable web components that can include a template,
server-side code and JavaScripts/CSS resources. The library aims to be:
flexible, reliable, documented, performant, and as simple as possible.

`dynatree`_ is a jQuery plugin that allows to dynamically create html
tree view controls using JavaScript.

This module, tw2.jqplugins.dynatree, provides `toscawidgets2 (tw2)`_ access
to `dynatree`_ widgets.

Sampling tw2.dynatree in the WidgetBrowser
------------------------------------------

The best way to scope out ``tw2.dynatree`` is to load its widgets in the
``tw2.devtools`` WidgetBrowser.  To see the source code that configures them,
check out ``tw2.dynatree/tw2/dynatree/samples.py``

To give it a try you'll need git, python, and `virtualenvwrapper
<http://pypi.python.org/pypi/virtualenvwrapper>`_.  Run::

    $ git clone git://github.com/toscawidgets/tw2.dynatree.git
    $ cd tw2.dynatree
    $ mkvirtualenv tw2.dynatree
    (tw2.dynatree) $ pip install tw2.devtools
    (tw2.dynatree) $ python setup.py develop
    (tw2.dynatree) $ paster tw2.browser

...and browse to http://localhost:8000/ to check it out.
