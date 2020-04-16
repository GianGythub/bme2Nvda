# Braille Music Editor Add-On for NVDA
* Author: Gianluca Casalino
* Download 

This project is an appModule for the Braille Music Editor 2 (Bme2) Software. It has been inspired by the work done for Jaws For Windows, provided from the same authors of Bme2.
**Please note:** This addon has been developed by Gianluca Casalino as a voluntary activity. Nor the author or the contributors are involved in selling and / or development of the software bme2.  If you are encountering any difficulties when using or installing this addon, please contact the author or use the "Issues" link on the Github project page.

### [Official Github Repository](https://github.com/bme2-nvda/bme2Nvda/)

## Addon Features:

### Speech support:

* Dialogs and menus are properly reported;
* Natural speech support for musical elements using the bme2 engine; 
* Implemented the Reading by character, words, paragraph, lines, say from cursor, say to cursor and Say All;
* Speaks when a block of text or which block of text is selected;
* Speaks when moving in the text editor using standard Windows commands; 
* Special dialogs like play midi, parts selector, and instruments midi selector window are now correctly reported and NVDA reads correctly when moving the cursor around or when new text is typed  or an item selected;
* Typing echo uses the bme2 text processor, so musical elements  will be correctly reported.

### Braille support:

* Dialogs and menus are properly reported in braille;
* The content of the editor is correctly rendered in braille and the user is able to move using braille scrolling keys or cursor routing keys;
* The selection will be marked properly using dots 7 and 8, and marking is properly refreshed while standard Windows commands (SHIFT+ARROWS)  are pressed.

## Addon Keyboard Shortcuts:

* **NVDA+alt+upArrow**: Reads from the beginign of the text until the cursor position;
* **NVDA+alt+downArrow**: Reads from the cursor position until the end of the text;
* **NVDA+o**: Reports the musical element properties if any, at the cursor position.
* **F12**: If present, reads the lyrics related to the cursor position;

## Known issues:

* Nvda Review Cursor is not implemented yet for Bme2.
* When performing braille routing on a note, midi event is not triggered. It needs more investigation
* When performing a say all command, if the text is significantly long, NVDA freezes.

## Change log

Below is a list of changes between the different add-on versions. Next to the version number, between parentheses, is the development status. The current development release isn't included as it could have changes until it is flagged as stable or discarded as candidate.

### Version 2020.04.4

* Completely reengenired the old release of add-on. It is now compatible with 2019.3 release of Nvda and following.
* Added support for all special dialog windows as for example parts selector or midi instruments selector.
* Added some new commands script.

## Thanks

A special thanks to Alberto Buffolino. With patience he has allowed me to realign my knowledge of the changes that have taken place over several years in the NVDA code.