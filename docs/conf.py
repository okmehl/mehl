#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

import os

extensions = ['sphinx.ext.imgmath', 'sphinx.ext.viewcode']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = 'Mehl'
copyright = '2021, Mehl authors'
author = 'Mehl authors'
version = release = os.environ.get('VERSION', 'master')
language = None
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'Dockerfile', 'docker-compose.yml']
pygments_style = 'sphinx'
todo_include_todos = False
html_theme = 'sphinx_rtd_theme'
html_title = 'Mehl, Docker based mail server'
html_static_path = []
htmlhelp_basename = 'Mehldoc'

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
html_sidebars = {
    '**': [
        'relations.html', 
        'searchbox.html',
    ]
}

# Theme options
html_context = {
    'display_github': True,
    'github_user': 'mehl',
    'github_repo': 'mehl',
    'github_version': version,
    'stable_version': '1.0',
    'versions': [
        ('master', '/master/')
    ],
    'conf_py_path': '/docs/'
}
