# globalPlugins/leDictionnaire/contextHelp.py.

# Copyright 2022-2023 Abdelkrim Bensaïd, released under gPL.
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.


import os
import gui
import tempfile
import addonHandler
from .leDictionnaireSettings import ADDON_NAME
from logHandler import log
if hasattr(gui, 'contextHelp'):
	from gui.contextHelp import writeRedirect
	from .skipTranslation import translate


def showAddonHelp(helpId: str):
	"""Display the corresponding section of the user guide when either the Help
	button in an NVDA dialog is pressed or the F1 key is pressed on a
	recognized control.
	This function was taken from the gui.contextHelp.showHelp function of NVDA source to allow use with add-ons.
	"""

	import ui
	import queueHandler
	if not helpId:
		# Translators: Message indicating no context sensitive help is available for the control or dialog.
		noHelpMessage = translate("No help available here.")
		queueHandler.queueFunction(queueHandler.eventQueue, ui.message, noHelpMessage)
		return
	helpFile = addonHandler.getCodeAddon().getDocFilePath()
	if helpFile is None:
		# Translators: Message shown when trying to display context sensitive help,
		# indicating that	the user guide could not be found.
		noHelpMessage = translate("No user guide found.")
		log.debugWarning("No user guide found: possible cause - running from source without building user docs")
		queueHandler.queueFunction(queueHandler.eventQueue, ui.message, noHelpMessage)
		return
	log.debug(f"Opening help: helpId = {helpId}, userGuidePath: {helpFile}")

	addonTempDir = os.path.join(tempfile.gettempdir(), ADDON_NAME)
	if not os.path.exists(addonTempDir):
		os.mkdir(addonTempDir)

	contextHelpRedirect = os.path.join(addonTempDir, "contextHelp.html")
	if hasattr(gui, 'contextHelp'):
		try:
			# a redirect is necessary because not all browsers support opening a fragment URL from the command line.
			writeRedirect(helpId, helpFile, contextHelpRedirect)
		except Exception:
			log.error("Unable to write context help redirect file.", exc_info=True)
			return

	try:
		os.startfile(f"file://{contextHelpRedirect}")  # type: ignore[attr-defined]
	except Exception:
		log.error("Unable to launch context help.", exc_info=True)
