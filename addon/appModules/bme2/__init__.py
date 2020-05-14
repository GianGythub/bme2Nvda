import winUser
import controlTypes as ct
import addonHandler
import appModuleHandler
from .bme2OverlayClasses import *

noItemsLabel = _("%s items")%0
addonHandler.initTranslation()

class AppModule(appModuleHandler.AppModule):
	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if (obj.role == ct.ROLE_EDITABLETEXT and obj._get_windowControlID() == 157) or (obj.role == ct.ROLE_EDITABLETEXT and 'Braille' in obj.name): 
			try:
				if obj.parent.next.firstChild.role == ct.ROLE_CHECKBOX or (obj.parent.next.firstChild.role == ct.ROLE_GRAPHIC and obj.windowStyle & winUser.ES_MULTILINE): return
			except: pass
			clsList.insert(0,Bme2Edit)
		elif obj.role == ct.ROLE_TREEVIEWITEM: clsList.insert(0,Bme2TreeViewItem)
		elif obj.role == ct.ROLE_LISTITEM and obj.windowClassName != "DirectUIHWND": clsList.insert(0,Bme2ListBoxItem)
		elif obj.role == ct.ROLE_CHECKBOX: clsList.insert(0,Bme2Checkbox)
		elif obj.role == ct.ROLE_UNKNOWN  and obj.parent.role == ct.ROLE_LIST: 
			obj.name = noItemsLabel
