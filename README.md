Del Extension for Python-Markdown
=====================================

Wraps inline content with `del` tags.


Installation
------------

    pip install git+git://github.com/aendrew/mdx_del.git


Usage
-----

    >>> import markdown
    >>> src = """This is ~~deleted content~~""" 
    >>> html = markdown.markdown(src, ['del'])
    >>> print(html)
    <p>This <del>deleted content</del>
    </p>


Dependencies
------------

* [Markdown 2.0+](http://www.freewisdom.org/projects/python-markdown/)


Copyright
---------

2011, 2012 [The active archives contributors](http://activearchives.org/)
All rights reserved.

This software is released under the modified BSD License. 
See LICENSE.md for details.
