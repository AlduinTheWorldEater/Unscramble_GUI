# Unscramble_GUI
A python application with a barebones GUI that provides all unscrambled words formed from the feeded string.

The GUI, in its bare form, creates a table of all words formed by every possible subset of the input string and creates a table of words separated by the number of letters in it.

Feel free to contact me at anirudh442003@gmail.com

File structure:

dictio.txt --> This file contains the master dictionary used to check if a word can be formed by unscrambling a certain subset. This is basically the Collins scrabble dictionary.

utils.py --> This file contains the different functions used to run the backend code, i.e, the vectorization, conversions, I/O. Do not modify this unless there's a bug in the production of words

main.py --> This file is responsible for housing the function that actually creates the usable word dictionary. 

GUI.py --> Self-explanatory. This file houses the entire GUI interface code. Edit this file for changes in the interface.
