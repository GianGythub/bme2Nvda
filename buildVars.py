# -*- coding: UTF-8 -*-

# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

# Full getext (please don't change)
_ = lambda x : x

# Add-on information variables
addon_info = {
	# for previously unpublished addons, please follow the community guidelines at:
	# https://bitbucket.org/nvdaaddonteam/todo/raw/master/guidelines.txt
	# add-on Name, internal for nvda
		"addon_name" : "bme2",
	# Add-on summary, usually the user visible name of the addon.
	# Translators: Summary for this add-on to be shown on installation and add-on information.
	"addon_summary" : _("Bme2 App Module"), 
	# Add-on description
	# Translators: Long description to be shown for this add-on on add-on information from add-ons manager
	"addon_description" : _("""Add-on to provide bme2 accessibility with NVDA
	In the main editor and special edit field, During cursor movementts and during editing, music elements are spoken correctly and presented on the Braille display.
	In addition,you can use these commands:
	
	Nvda+Alt+upArrow: reads from the begining of the text until the cursor position.
	Nvda+alt+downArrow: reads from the position of the cursor until the end of the text
	Nvda+o: reads the properties of the musical element if any.
F12: reports lyrics of the element under the cursor, if present.
	"""),
	# version
	"addon_version" : "2022.05.1",
	# Author(s)
	"addon_author" : u"Gianluca Casalino <giludev@casalino.cloud>",
	# URL for the add-on documentation support
	"addon_url" : None,
	# Documentation file name
	"addon_docFileName" : "readme.html",
	# Minimum NVDA version supported (e.g. "2018.3.0", minor version is optional)
	"addon_minimumNVDAVersion" : None,
	# Last NVDA version supported/tested (e.g. "2018.4.0", ideally more recent than minimum version)
	"addon_lastTestedNVDAVersion" : "2022.1",
	# Add-on update channel (default is None, denoting stable releases, and for development releases, use "dev"; do not change unless you know what you are doing)
	"addon_updateChannel" : None,
}


import os.path

# Define the python files that are the sources of your add-on.
# You can use glob expressions here, they will be expanded.
pythonSources = [
	os.path.join("addon","appModules","bme2", "*.py"),
	os.path.join("addon", "*.py"),
	
]

# Files that contain strings for translation. Usually your python sources
i18nSources = pythonSources + ["buildVars.py"]

# Files that will be ignored when building the nvda-addon file
# Paths are relative to the addon directory, not to the root directory of your addon sources.
excludedFiles = []
