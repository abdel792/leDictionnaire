# globalPlugins/leDictionnaire/leDictionnaireSettings.py.

# Copyright 2022-2023 Abdelkrim Bensaïd, released under gPL.
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

import wx
from typing import Callable
import gui
import gui.guiHelper
import config

# We initialize translation support
import addonHandler
addonHandler.initTranslation()
if hasattr(gui.settingsDialogs, "SettingsPanel"):
	from gui.settingsDialogs import SettingsPanel
else:
	from gui import SettingsPanel

# Constants
ADDON_SUMMARY = addonHandler.getCodeAddon().manifest["summary"]
ADDON_NAME = addonHandler.getCodeAddon().manifest["name"]

# gettex translation function.
_: Callable[[str], str]
confSpec = {
	"displayLeDictionnaireMode": "string(default = HTMLMessage)",
}
config.conf.spec["leDictionnaire"] = confSpec


class LeDictionnaireSettingsPanel(SettingsPanel):

	# Translators: The title of the add-on configuration dialog box.
	title = ADDON_SUMMARY
	helpId = "leDictionnaireSettings"
	DISPLAY_MODES = (
		("HTMLMessage",
		 # Translators: Display the result in an NVDA message of type HTML.
		 _("Display in HTML message")),
		("simpleMessage",
		 # Translators: Displays the result in a simple NVDA browseable message.
		 _("Display in a simple NVDA browseable message")),
		("defaultBrowser",
		 # Translators: Display the result in default browser.
		 _("Display in default browser"))
	)

	def makeSettings(self, settingsSizer):
		# Translators: The label for an item to select the display mode for leDictionnaire.
		self.displayLeDictionnaireModeText = _("Display mode for leDictionnaire definitions.")
		self.showSettingsDialog(settingsSizer)

	def showSettingsDialog(self, settingsSizer):
		settingsSizerHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
		displayLeDictionnaireModeChoices = [name for mode, name in self.DISPLAY_MODES]
		self.displayLeDictionnaireModesList = settingsSizerHelper.addLabeledControl(
			self.displayLeDictionnaireModeText,
			wx.Choice,
			choices=displayLeDictionnaireModeChoices
		)
		curLeDictionnaireMode = config.conf["leDictionnaire"]["displayLeDictionnaireMode"]
		for index, (mode, name) in enumerate(self.DISPLAY_MODES):
			if mode == curLeDictionnaireMode:
				self.displayLeDictionnaireModesList.SetSelection(index)
				break

	def onSave(self):
		displayLeDictionnaireMode = self.DISPLAY_MODES[self.displayLeDictionnaireModesList.GetSelection()][0]
		config.conf["leDictionnaire"]["displayLeDictionnaireMode"] = displayLeDictionnaireMode
