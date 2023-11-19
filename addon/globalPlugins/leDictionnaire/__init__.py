# globalPlugins/leDictionnaire/__init__.py.

# Copyright 2022-2023 Abdelkrim Bensaïd, released under gPL.
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.


import addonHandler
import globalPluginHandler
from typing import Callable
import wx
import gui
import config
from gui import NVDASettingsDialog
import os
from .leDictionnaireSettings import ADDON_NAME, ADDON_SUMMARY, LeDictionnaireSettingsPanel
from .leDictionnaireRegexps import (
	regClean,
	regTitle,
	regDef,
	regOl,
	regLi,
	replItem,
)
from .leDictionnaireClean import (
	cleanMessageForHtml,
	cleanMessageForText,
)
from .contextHelp import showAddonHelp
from urllib.request import Request, urlopen, quote  # type: ignore[attr-defined]
import ui
import tempfile
addonHandler.initTranslation()

# gettex translation function.
_: Callable[[str], str]

if hasattr(gui, 'contextHelp'):
	saveShowHelp = gui.contextHelp.showHelp

	class EnterSearchTermsDialog(
			gui.contextHelp.ContextHelpMixin,
			wx.TextEntryDialog,  # wxPython does not seem to call base class initializer, put last in MRO
	):
		helpId = "promptToEnterSearchTerms"
else:
	class EnterSearchTermsDialog(  # type: ignore[no-redef]
			wx.TextEntryDialog
	):
		pass


def getPage(url):
	headers = {"User-Agent": "Mozilla/5.0"}
	req = Request(url=url, headers=headers)
	return urlopen(req).read().decode("utf-8")


def displayInDefaultBrowser(fileName, title, body):
	addonTempDir = os.path.join(tempfile.gettempdir(), ADDON_NAME)
	if not os.path.exists(addonTempDir):
		os.mkdir(addonTempDir)
	file = os.path.join(addonTempDir, f"{fileName}.html")
	htmlText = f"""<!DOCTYPE html>
	<html lang='fr'>
	<meta charset = 'utf-8' />
	<head>
	<title>{title}</title>
	</head>
	{body}
	</html>"""
	with open(file, mode="w", encoding="utf-8") as f:
		f.write(htmlText)
	os.startfile(file)


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	scriptCategory = ADDON_SUMMARY
	_instance = False
	contextHelp = False

	def __init__(self, *args, **kwargs):
		super(GlobalPlugin, self).__init__(*args, **kwargs)
		self.terms = ""
		NVDASettingsDialog.categoryClasses.append(LeDictionnaireSettingsPanel)
		self.createMenu()

	def createMenu(self):
		self.toolsMenu = gui.mainFrame.sysTrayIcon.toolsMenu

		self.leDictionnaireItem = self.toolsMenu.Append(wx.ID_ANY,
		"Le diction&naire...",
		# Translators: The tooltyp text for leDictionnaire item.
		_("Allows you to search for a definition in the free online French dictionary le-dictionnaire.com"))

		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onLeDictionnaireDialog, self.leDictionnaireItem)

	def terminate(self):
		try:
			NVDASettingsDialog.categoryClasses.remove(LeDictionnaireSettingsPanel)
		except Exception:
			pass
		try:
			if wx.version().startswith("4"):
				self.toolsMenu.Remove(self.leDictionnaireItem)
			else:
				self.toolsMenu.RemoveItem(self.leDictionnaireItem)
		except Exception:
			pass

	def event_gainFocus(self, obj, nextHandler):
		if hasattr(gui, 'contextHelp'):
			if obj.parent and obj.parent.parent and any(
				x == ADDON_SUMMARY for x in (obj.name, obj.parent.parent.name)
			) or self.contextHelp:
				gui.contextHelp.showHelp = showAddonHelp
			else:
				gui.contextHelp.showHelp = saveShowHelp
		nextHandler()

	def script_enterSearchTerms(self, gesture):
		self.onLeDictionnaireDialog()

	# Translators: Message presented in input help mode.
	script_enterSearchTerms.__doc__ = _(
		"Displays a dialog box prompting the user to enter a search for a definition on le-dictionnaire.com"
	)

	def script_activateAddonSettingsDialog(self, gesture):
		wx.CallAfter(self.onAddonSettingsDialog, None)

	# Translators: Message presented in input help mode.
	script_activateAddonSettingsDialog.__doc__ = _("Allows you to display leDictionnaire add-on settings panel.")

	def onLeDictionnaireDialog(self, evt=None):
		if hasattr(gui, 'contextHelp'):
			self.contextHelp = True
			gui.contextHelp.showHelp = showAddonHelp
		if not self._instance:
			d = EnterSearchTermsDialog(
				gui.mainFrame,
				# Translators: Dialog text for the search terms dialog.
				_("Enter the word whose definition you are looking for"),
				# Translators: Title for the search terms dialog
				_("Search terms"))

			def callback(result):
				if result in (wx.ID_OK, wx.ID_CANCEL):
					self._instance = False
					if hasattr(gui, 'contextHelp'):
						gui.contextHelp.showHelp = saveShowHelp
						self.contextHelp = False
				if result == wx.ID_OK:
					self.terms = d.Value
					self.displayDefinition()
			gui.runScriptModalDialog(d, callback)
			self._instance = True

	def onAddonSettingsDialog(self, evt):
		gui.mainFrame._popupSettingsDialog(NVDASettingsDialog, LeDictionnaireSettingsPanel)

	def displayDefinition(self):  # noqa: C901
		terms = quote(self.terms)
		page = getPage(url=f"https://www.le-dictionnaire.com/definition/{terms}")
		if terms != "" and regTitle.search(page):
			title = regTitle.search(page).group(0)
			content = [f"{x.group(1).replace('span', 'h2')}" for x in regDef.finditer(page)]
			content.insert(0, title)
			content = [f"{x.strip()}\n" for x in content]
			title = regClean.sub("", title)
			syns = getPage(url=f"https://www.synonymes.com/synonyme.php?mot={terms}")
			ols = [f'\n{x.group("type")}\n{x.group("liste")}' for x in regOl.finditer(syns)]
			if len(ols):
				items = "<h1>Synonymes</h1>\n" + regLi.sub(replItem, "".join(ols)).replace("<br /></li>", "</ul>")
			else:
				items = ""
			htmlDefinition = cleanMessageForHtml("".join(content) + items)
			textDefinition = cleanMessageForText("".join(content) + items)
		else:
			gui.messageBox(
				# Translators: A message to indicate that the text entered is not correctly written.
				_("Either you didn't enter anything or the terms entered are not correct. Please try again"),
				# Translators: Title of the message indicating the input error.
				_("Input error")
			)
			self.onLeDictionnaireDialog()
			return
		msg = f"<body>{htmlDefinition}</body>"
		if config.conf["verbs"]["displayConjugationMode"] == "HTMLMessage":
			wx.CallAfter(ui.browseableMessage, title=title, message=msg, isHtml=True)
		elif config.conf["verbs"]["displayConjugationMode"] == "defaultBrowser":
			displayInDefaultBrowser(fileName="conjugaison", title=title, body=msg)
		else:
			wx.CallAfter(ui.browseableMessage, title=title, message=textDefinition)

	__gestures = {
		"kb:control+shift+f12": "enterSearchTerms",
	}
