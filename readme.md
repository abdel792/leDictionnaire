# Le dictionnaire #

* Authors : Abdel.
* Download [stable version][1]
* Download [development version][2]

This add-on allows you to display the definition of a French word using the site: «https://www.le-dictionnaire.com».

It adds an item to the NVDA Tools menu named «Le dictionnaire».

When you validate on this item, you obtain a dialog box composed of the following elements:

* An input field to type the word whose definition you are looking for;
{: #promptToEnterSearchTerms }
* An "OK" button to display a page containing your definition according to the display mode you chose in the add-on's settings panel;
* A "Cancel" button to close the dialog box.

## Add-on settings ## {: #leDictionnaireSettings }

In the add-on's settings panel, you should find the following:

* Display mode for leDictionnaire definitions, which allows to define the display mode of your definitions found;
* This display mode offers the following 3 choices:
    * Display in an HTML message, which allows you to display the definition in a browseable HTML message  (this is the default choice);
    * Display in a simple message, which allows you to display the definition in a simple browseable message, without HTML formatting;
    * Display in default browser, to display the definition in your default browser.
* An "OK" button to save your configuration;
* A "Cancel" button to cancel and close the dialog box.
* An "Apply" button to apply your configuration;

## Notes ##

* By default, the "control + shift+F12" gesture is assigned to the script which displays the dialog inviting the user to enter a word to find its definition;
* A script without an assigned gesture allows you to open the add-on settings panel;
* You can assign  new gestures to run this scripts in the "Input gestures" menu and, more precisely, in the «Verbs» category;
* If you are using nvda-2021.1 or later, you will be able to access the help from the input field of the word to search, as well as from the add-on settings panel by simply pressing the "F1" key. as soon as the focus is on one of these 2 controls.

## Compatibility ##

* This add-on is compatible with NVDA 2019.3 and beyond.

## Changes for version 23.11.19 ##

* Initial version.


[1]: https://github.com/abdel792/leDictionnaire/releases/download/v23.11.19/leDictionnaire-23.11.19.nvda-addon

[2]: http://cyber25.free.fr/nvda-addons/leDictionnaire-23.11.19-dev.nvda-addon
