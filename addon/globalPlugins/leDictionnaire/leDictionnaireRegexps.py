# globalPlugins/leDictionnaire/leDictionnaireRegexps.py.

# Copyright 2022-2023 Abdelkrim Bensaïd, released under gPL.
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

import re

# Patterns.
patternClean = r"<[^>]*?>"
patternTitle = r"<h1>.*?</h1>"
patternDef = (
	r'<div class="defbox(?: extraboxinfo)?">.*?'
	'(<span>.*?</span>.*?<div class="(?:motboxinfo|wrapboxattention|wrapboxinfo)">.*?'
	'</div>(.*?<ul>.*?</ul>)?)'
)
patternOl = r'<div class="defbox"><span>(?P<type>.*?)</span>.*?<ol style="[^>]*?>(?P<liste>.*?)</ol>'
patternLi = r'(?P<type>.*?)?\n?.*?<a href=[^>]*?>(?P<item>.*?)</a>'

# Compiled regexps.
regClean = re.compile(patternClean, re.I | re.S)
regTitle = re.compile(patternTitle, re.I | re.M)
regDef = re.compile(patternDef, re.I | re.S)
regOl = re.compile(patternOl, re.I | re.S)
regLi = re.compile(patternLi, re.I | re.M)

# functions for replacements.


def replItem(match):
	tName = match.group("type")
	if tName:
		return f'<h2>{tName}</h2>\n<ul>\n<li>{match.group("item")}</li>\n'
	return f'<li>{match.group("item")}</li>\n'
