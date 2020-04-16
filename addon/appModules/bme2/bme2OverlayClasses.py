import textInfos
import addonHandler
import winUser
import config
import controlTypes as ct
import comHelper
from comtypes import COMError
import speech
import eventHandler
import braille
import NVDAObjects.window.edit as edit
from NVDAObjects.IAccessible.sysTreeView32 import TreeViewItem
from NVDAObjects.IAccessible.sysListView32 import ListItem# WithoutColumnSupport
from NVDAObjects.IAccessible import IAccessible

speakTypedCharacters = False
speakTypedWords = False
positionIndexInListBox = 0
reportHintOnListBox = True

addonHandler.initTranslation()

class Bme2SpeechSupport(object):
	s = None
	_BME2COMOBJNAME = "bme2.Jaws.object"
	_bme2ComObj = None #self.getBme2ComObj()
	def __init__(self):
		self._bme2ComObj = self.getBme2ComObj()
	def getBme2ComObj(self):
		if not self._bme2ComObj:# and not bme2ComObj:
			self.empty = ""
			bme2ComObj = comHelper.getActiveObject(self._BME2COMOBJNAME, dynamic=True)
			if bme2ComObj:
				self._bme2ComObj = bme2ComObj
				self.empty = self._bme2ComObj.getNone()
		return self._bme2ComObj
	def isManagedWindow(self, windowHandle):
		return self.getBme2ComObj().isManagedWindow(self.windowHandle)			
	def sayText(self, text):
		if text == None or text == self.empty: return
		speech.speakText(text)

class Bme2Edit(Bme2SpeechSupport,edit.Edit):
	global speakTypedCharacters, speakTypedWords
	s = None
	announceValueChange = True

	def script_reportCurrentLine(self,gesture):
		if not self.isManagedWindow(self.windowHandle): return
		try:
			s = self.getBme2ComObj().getline(self.windowHandle, -1, -1)
			self.sayText(s)
		except COMError: pass
	script_reportCurrentLine.__doc__ = _("reports the current line under the application cursor")

	def script_sayAll(self,gesture):
		if not self.isManagedWindow(self.windowHandle): return
		try:
			s = self.getBme2ComObj().getAll(self.windowHandle)
			self.sayText(s)
		except COMError: pass
	script_sayAll.__doc__ = _("reads from the begining of the document up to the end of the text. ")

	def script_sayFromCursor(self,gesture):
		if not self.isManagedWindow(self.windowHandle): return
		try:
			s = self.getBme2ComObj().getFromCursor(self.windowHandle, -1, -1)
			self.sayText(s)
		except COMError: pass
	script_sayFromCursor.__doc__ = _("reads from the cursor  up to the end of the text. ")

	def script_sayToCursor(self,gesture):
		if not self.isManagedWindow(self.windowHandle): return
		try:
			s = self.getBme2ComObj().getToCursor(self.windowHandle, -1, -1)
			self.sayText(s)
		except COMError: pass
	script_sayToCursor.__doc__ = _("reads from the begining of the document up to the cursor. ")

	def script_reportSelectedText(self,gesture):
		if not self.isManagedWindow(self.windowHandle): return
		try:
			s = self.getBme2ComObj().getSelectedText(self.windowHandle)
			self.sayText(s)
		except COMError: pass
	script_reportSelectedText.__doc__ = _("report the current selected text ")

#	def script_caretMoveByChar(self,gesture):
#		gesture.send()
#		try:
#			s = self.getBme2ComObj().getChar(self.windowHandle, -1, -1)
#			self.sayText("ciccio"+s)
#			braille.handler.mainBuffer.clear()
#			braille.handler.handleGainFocus(self)
#		except COMError: pass

	def script_caret_backspaceCharacter(self,gesture):
		if not self.isManagedWindow(self.windowHandle):
			gesture.send()
			return
		try:
			self.announceValueChange = False
			s = self.getBme2ComObj().getPriorChar(self.windowHandle)
			self.sayText(s)
			gesture.send()
			braille.handler.mainBuffer.clear()
			braille.handler.handleGainFocus(self)
		except COMError: pass

	def script_caret_delete(self,gesture):
		if not self.isManagedWindow(self.windowHandle):
			gesture.send()
			return
		self.announceValueChange = False
		gesture.send()

	def script_caretMoveByLine(self,gesture):
		gesture.send()
		if not self.isManagedWindow(self.windowHandle): return
		self.script_reportCurrentLine(gesture)
		self.redraw()
		braille.handler.mainBuffer.clear()
		braille.handler.handleGainFocus(self)

	def script_caretMoveByWord(self,gesture):
		gesture.send()
		if not self.isManagedWindow(self.windowHandle): return
		try:
			s = self.getBme2ComObj().getWord(self.windowHandle, -1, -1)
			self.sayText(s)
			braille.handler.mainBuffer.clear()
			braille.handler.handleGainFocus(self)
		except COMError: pass

	def script_caretMoveByParagraph(self,gesture):
		gesture.send()
		if not self.isManagedWindow(self.windowHandle): return
		try:
			s = self.getBme2ComObj().getParagraph(self.windowHandle, -1, -1)
			self.sayText(s)
			braille.handler.mainBuffer.clear()
			braille.handler.handleGainFocus(self)
		except COMError: pass

	def event_gainFocus(self):
		global speakTypedCharacters, speakTYpedWords
		speakTypedCharacters = config.conf["keyboard"]["speakTypedCharacters"]
		speakTypedWords = config.conf["keyboard"]["speakTypedWords"]
		if not self.isManagedWindow(self.windowHandle): return
		config.conf["keyboard"]["speakTypedCharacters"] = False
		config.conf["keyboard"]["speakTypedWords"] = False
		super(Bme2Edit, self).event_gainFocus()
		braille.handler.handleGainFocus(self)
		try:
			s = self.getBme2ComObj().getLine(self.windowHandle, -1, -1)
			self.sayText(s)
		except COMError: pass

	def selectionInProgress(self):
		try:
			info = self.makeTextInfo(textInfos.POSITION_SELECTION)
		except (RuntimeError, NotImplementedError): return False
		if not info or info.isCollapsed: return False
		return True

	def detectPossibleSelectionChange(self):
		if not self.selectionInProgress(): return
		try:
			s = self.getBme2ComObj().getSelectedText(self.windowHandle)
			self.sayText(s)
		except COMError: pass

	def event_loseFocus(self):
		global speakTypedCharacters, speakTypedWords
		super(Bme2Edit, self).event_loseFocus()
		config.conf["keyboard"]["speakTypedCharacters"] = speakTypedCharacters
		config.conf["keyboard"]["speakTypedWords"] = speakTypedWords

	#def event_typedCharacter(self,ch):
	#	if eventHandler.isPendingEvents("caret"): return
	#	super(Bme2Edit, self).event_typedCharacter()

	def event_valueChange(self):
		if eventHandler.isPendingEvents("textChange") or eventHandler.isPendingEvents("valueChange"): return
		if not self.announceValueChange or self.selectionInProgress() or not self.isManagedWindow(self.windowHandle): 
			self.announceValueChange = True
			return
		try:
			s = self.getBme2ComObj().getNewChar(self.windowHandle)
			self.sayText(s)
		except COMError: pass
		braille.handler.mainBuffer.clear()
		braille.handler.handleGainFocus(self)
#		self.announceValueChange = True

	def event_caret(self):
		if  eventHandler.isPendingEvents("gainFocus") or eventHandler.isPendingEvents("caret") or eventHandler.isPendingEvents("valueChange") or eventHandler.isPendingEvents("typedCharacter"): return
		super(edit.Edit, self).event_caret()
		braille.handler.mainBuffer.clear()
		braille.handler.handleGainFocus(self) 
		if not self.announceValueChange or self.selectionInProgress() or not self.isManagedWindow(self.windowHandle): return 
		try:
			s = self.getBme2ComObj().getChar(self.windowHandle)
			self.sayText(s)
		except COMError: pass

	def script_reportProperties(self,gesture):
		if not self.isManagedWindow(self.windowHandle): return
		try:
			s = self.getBme2ComObj().getProperties(self.windowHandle, -1, -1)
			self.sayText(s)
		except COMError: pass
	script_reportProperties.__doc__ = _("reports the element properties under the cursor if they exists")

	def script_reportLyrics(self,gesture):
		if not self.isManagedWindow(self.windowHandle): return
		try:
			s = self.getBme2ComObj().GetLyrics(self.windowHandle, -1, -1)
			self.sayText(s)
		except COMError: pass
	script_reportLyrics.__doc__ = _("reports the element lyrics under the cursor if exists")

	__gestures = {"kb(desktop):NVDA+upArrow": "reportCurrentLine",		"kb(laptop):NVDA+l": "reportCurrentLine",
		"kb(desktop):NVDA+downArrow": "sayAll",
		"kb(laptop):NVDA+a": "sayAll",
#		"kb:rightArrow": "caretMoveByChar",
#		"kb:leftArrow": "caretMoveByChar",
#		"kb:home": "caretMoveByChar",
#		"kb:end": "caretMoveByChar",
		"kb:upArrow": "caretMoveByLine",
		"kb:downArrow": "caretMoveByLine",
		"kb:pageUp": "caretMoveByLine",
		"kb:pageDown": "caretMoveByLine",
		"kb:control+home": "caretMoveByLine",
		"kb:control+end": "caretMoveByLine",
		"kb:control+leftArrow": "caretMoveByWord",
		"kb:control+rightArrow": "caretMoveByWord",
		"kb:control+upArrow": "caretMoveByParagraph",
		"kb:control+downArrow": "caretMoveByParagraph",
		"kb:NVDA+alt+upArrow": "sayToCursor",
		"kb:NVDA+alt+downArrow": "sayFromCursor",
		"kb:backspace": "caret_backspaceCharacter",
		"kb:Delete": "caret_delete",
		"kb:numpad+Delete": "caret_delete",
		"kb(desktop):NVDA+shift+upArrow": "reportSelectedText",
		"kb(laptop):NVDA+shift+s": "reportSelectedText",
		"kb:NVDA+o": "reportProperties",
		"KB:F12": "reportLyrics",
		}


class Bme2TreeViewItem(TreeViewItem,Bme2SpeechSupport):
	def event_gainFocus(self):
		if not self.isManagedWindow(self.windowHandle): 
			super(Bme2TreeViewItem, self).event_gainFocus()
			return
		if ct.STATE_EXPANDED not in self.states and ct.STATE_COLLAPSED not in self.states:
			try:
				s = self.getBme2ComObj().getSelectedText(self.windowHandle)
				self.sayText(s)
			except: pass
		super(Bme2TreeViewItem, self).event_gainFocus()

	def event_typedCharacter(self, ch):
		if not self.isManagedWindow(self.windowHandle): return
		if ch == ' ':
			try:
				s = self.getBme2ComObj().GetSpace(self.windowHandle)
				self.sayText(s)
			except COMError: pass
		super(Bme2TreeViewItem, self).event_typedCharacter(ch)


class Bme2ListBoxItem(ListItem,Bme2SpeechSupport):
	def __init__(self, *args, **kwargs):
		super(Bme2ListBoxItem, self).__init__(*args, **kwargs)
		global reportHintOnListBox
		reportHintOnListBox = True
		return self.reportHintOnListBox

	def _get_allowIAccessibleChildIDAndChildCountForPositionInfo(self):
		return True

	def _get_positionInfo(self):
		positionInfo = super(Bme2ListBoxItem, self).positionInfo
		positionInfo["similarItemsInGroup"] = self.parent.childCount
		return positionInfo

	def event_gainFocus(self):
		global positionIndexInListBox, reportHintOnListBox
		if ct.STATE_PRESSED in self.states: 
			return
		if not self.isManagedWindow(self.windowHandle):
			super(Bme2ListBoxItem, self).event_gainFocus()
			return
		if (winUser.getAsyncKeyState(winUser.VK_LCONTROL) <= 1 and winUser.getAsyncKeyState(winUser.VK_RCONTROL) <= 1 and ct.STATE_SELECTED not in self.states):
			self.setFocus()
			return
		positionInfo = self._get_positionInfo()
		try:
			s = self.getBme2ComObj().getSelectedText(self.windowHandle)
			if not positionIndexInListBox: positionIndexInListBox = positionInfo["indexInGroup"]
			if winUser.getAsyncKeyState(winUser.VK_RCONTROL) > 1 or winUser.getAsyncKeyState(winUser.VK_LCONTROL) > 1: 
				case = positionInfo["indexInGroup"]!=positionIndexInListBox	
				text = (s,_("moved to position %d of %d")%(positionInfo["indexInGroup"],positionInfo["similarItemsInGroup"]))[case]
				self.sayText(text)
				positionIndexInListBox = positionInfo["indexInGroup"]
				return
			else: 
				positionIndexInListBox = None
				self.sayText(s)
			if positionInfo["similarItemsInGroup"]> 1 and reportHintOnListBox: 
				self.sayText(_("hold down control key to order elements in the list"))
				reportHintOnListBox = False
		except: pass
		super(Bme2ListBoxItem, self).event_gainFocus()

#	def event_stateChange(self):
#
#		return

	def event_typedCharacter(self, ch):
		if not self.isManagedWindow(self.windowHandle): return # == False or ct.STATE_SELECTED not in self.states: return
		if ch == ' ':
			self.sayText(_("removed from list"))
			self.setFocus() #braille.handler.handleGainFocus(self)
		super(Bme2ListBoxItem, self).event_typedCharacter(ch)


class Bme2Checkbox(Bme2SpeechSupport, IAccessible):
	def event_gainFocus(self):
		if not self.isManagedWindow(self.windowHandle): 
			super(Bme2Checkbox, self).event_gainFocus()
			return
		try:
			s = self.getBme2ComObj().getObjTypeAndText(self.windowHandle)
			self.sayText(s)
		except: pass
		super(Bme2Checkbox, self).event_gainFocus()

	def event_stateChange(self):
		if ct.STATE_PRESSED  in self.states: return
		try:
			s = self.getBme2ComObj().getObjStateChanged(self.windowHandle, (1 if ct.STATE_CHECKED in self.states else 2))
			self.sayText(s	)
		except COMError: pass
		super(Bme2Checkbox, self).event_stateChange()
