#!/usr/bin/env python


from setuptools import setup


setup(
    name='mdx_del',
    version='1.0',
    author='Ændrew Rininsland',
    author_email='aendrew@aendrew.com',
    description='Python-Markdown extension to support the <del> tag, forked from https://github.com/aleray/mdx_del_ins',
    url='https://github.com/aendrew/mdx_del',
    py_modules=['mdx_del'],
    install_requires=['Markdown>=2.0',],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML'
    ]
)
