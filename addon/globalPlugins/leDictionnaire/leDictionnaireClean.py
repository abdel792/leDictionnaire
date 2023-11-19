# globalPlugins/leDictionnaire/leDictionnaireClean.py.

# Copyright 2022-2023 Abdelkrim Bensaïd, released under gPL.
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

from.leDictionnaireRegexps import regClean


def cleanMessageForText(htmlMessage):
	text = regClean.sub("", htmlMessage)
	lines = [x.strip() for x in text.split("\n")]
	while lines.count(""):
		lines.remove("")
	return "\n".join(lines)


def cleanMessageForHtml(htmlMessage):
	lines = [x.strip() for x in htmlMessage.split("\n")]
	while lines.count(""):
		lines.remove("")
	return "\n".join(lines)
