#! /usr/bin/env python


'''
Del Extension for Python-Markdown
=====================================

Wraps the inline content with del tags. Gratuitous fork of https://github.com/aleray/mdx_del_ins,
except lacking the somewhat-useless "ins" functionality.


Usage
-----

    >>> import markdown
    >>> src = """This is ~~deleted content~~""" 
    >>> html = markdown.markdown(src, ['del'])
    >>> print(html)
    <p>This is <del>deleted content</del>
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
'''


import markdown
from markdown.inlinepatterns import SimpleTagPattern


DEL_RE = r"(\~\~)(.+?)(\~\~)"


class DelExtension(markdown.extensions.Extension):
    """Adds del extension to Markdown class."""

    def extendMarkdown(self, md, md_globals):
        """Modifies inline patterns."""
        md.inlinePatterns.add('del', SimpleTagPattern(DEL_RE, 'del'), '<not_strong')


def makeExtension(configs={}):
    return DelExtension(configs=dict(configs))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
