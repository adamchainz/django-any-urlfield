#!/usr/bin/env python
from setuptools import setup, find_packages
from os.path import dirname, join

setup(
    name='django-cmsfields',
    version='1.0.0',
    license='Apache License, Version 2.0',

    description='A set of CMS input fields, including an improved URL selector',
    long_description=open(join(dirname(__file__), 'README.rst')).read(),

    author='Diederik van der Boor',
    author_email='opensource@edoburu.nl',

    url='https://github.com/edoburu/django-cmsfields',
    download_url='https://github.com/edoburu/django-cmsfields/zipball/master',

    packages=find_packages(exclude=('example*',)),
    include_package_data=True,

    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ]
)
