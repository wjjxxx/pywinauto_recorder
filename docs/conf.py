# -*- coding: utf-8 -*-

import os
import sys

sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('../pywinauto_recorder'))


extensions = ['sphinx.ext.autodoc', 'sphinx.ext.autosummary']

exclude_patterns = ['contribute.rst', 'description.rst', 'pywinauto_recorder_exe.rst', 'smart_mode.rst']
autodoc_mock_imports = ["pywinauto", "win32api", "win32gui"]
# import pywinauto_recorder.player

autosummary_generate = True

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'


# General information about the project.
project = u'pywinauto_recorder'
copyright = u"2021, David Pratmarty"
author = u"David Pratmarty"