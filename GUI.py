#GUI!

from tkinter import *
import tkinter as tk
import os
from main import get_unscrambled_words


# Function to return the letter weights in a clean list form
def get_weights() -> "List of integers":

    global weight_var_list

    weights = [0] * 26
    for i in range(26): weights[i] = weight_var_list[i].get()

    return weights #Returns a list of integers

# Function to convert an integer to its corresponding ASCII character
def letterify(num: int) -> str:

    return chr(num + 65)

# Function to clean the created table
def clean_table() -> None:

    global frame, canv

    size = frame.grid_size()

    for i in range(size[0]):
        for j in range(10, size[1]):

            try:
                widg = frame.grid_slaves(j, i)[0]
                widg.destroy()

            except Exception: continue

# Function to calculate the score of a word given the letter weight list.
def score(word: str, weight_list: "List of letter weights") -> int:

    score = 0

    for i in word: score += weight_list[ord(i) - 65]

    return score

# Function that actually creates the GUI Table
def tabling(wordle: str) -> None:

    global frame, canv
    
    word_dict_by_letters = get_unscrambled_words(wordle)
    weight_list = get_weights()

    Label(frame, text = "").grid(row = 9, column = 0, padx = 10, pady = 10)
    clean_table()
    
    for i in range(len(word_dict_by_letters.keys())):

        word_list = word_dict_by_letters[i + 3]

        Label(frame, text = f"{i + 3} Letter Words", relief = SOLID).grid(row = 10, column = 2 * i, columnspan = 2, ipadx = 10, ipady = 10, sticky = N+E+W+S)

        for j in range(len(word_list)):
            Label(frame, text = word_list[j], relief = SOLID).grid(row = 11 + j, column = 2 * i, ipadx = 20, ipady = 10, sticky = N+E+W+S) 
            Label(frame, text = str(score(word_list[j], weight_list)), relief = SOLID).grid(row = 11 + j, column = 2 * i + 1, ipadx = 10, ipady = 10, sticky = N+E+W+S)

    canv.update_idletasks()
    canv.config(scrollregion = frame.bbox("all")) #This is to enable scrolling.


# Miscellaneous starting definitions

root = Tk()
root.geometry("1200x800")

canv = Canvas(root)

scrollbar_x = Scrollbar(root)
scrollbar_y = Scrollbar(root)

frame = Frame(canv)

root.title("Unscramble It!")

#Declare buttons

#Entry of the word, and the master submit button

wordvar = StringVar()

word_label = Label(frame, text = "Enter the word: ")
word_label.grid(row = 1, column = 0, columnspan = 3, padx = 10, pady = 10, sticky = W)

word_entry = Entry(frame, width = 50, textvariable = wordvar)
word_entry.grid(row = 1, column = 3, columnspan = 4, padx = 10, pady = 10, sticky = E)

word_submit = Button(frame, text = "Submit", command = lambda: tabling(wordvar.get()))
word_submit.grid(row = 1, column = 7, padx = 10, pady = 10, sticky = E)

# Bind the Enter key to the Submit action ONLY IF THE TEXT FIELD IS SELECTED.
word_entry.bind("<Return>", lambda event: tabling(wordvar.get()))

#Entry of the lettr weights (individually)

weight_var_list = [IntVar(), IntVar(), IntVar(), IntVar(), IntVar(),
                   IntVar(), IntVar(), IntVar(), IntVar(), IntVar(),
                   IntVar(), IntVar(), IntVar(), IntVar(), IntVar(),
                   IntVar(), IntVar(), IntVar(), IntVar(), IntVar(),
                   IntVar(), IntVar(), IntVar(), IntVar(), IntVar(),
                   IntVar()]

for i in weight_var_list: i.set(0)

weight_label = Label(frame, text = "Enter the letter weights below (optional)")
weight_label.grid(row = 2, column = 0, columnspan = 4, padx = 10, pady = 10, sticky = S+W)

for i in range(26):
    
    Label(frame, text = f"{letterify(i)}: ").grid(row = 3 + (i // 5), column = 2 * (i % 5), padx = 20, pady = 10, sticky = W)
    Entry(frame, width = 10, textvariable = weight_var_list[i]).grid(row = 3 + (i // 5), column = 2 * (i % 5) + 1, padx = 20, pady = 10, sticky = E)

# Creates 26 entry fields, in a 6 x 5 table

#Scrollbar and canvas packing (for display in the GUI)

scrollbar_y.config(orient = VERTICAL, command = canv.yview)
scrollbar_x.config(orient = HORIZONTAL, command = canv.xview)

# Allow the Mouse Wheel to scroll through the canvas window
canv.bind_all("<MouseWheel>", lambda event: canv.yview_scroll(int(-1 * event.delta / 120), "units"))

canv.update_idletasks()    
canv.config(xscrollcommand = scrollbar_x.set, yscrollcommand = scrollbar_y.set, scrollregion = frame.bbox("all"))

#Configurations of the scrollbars, and the canvas to use the scrollbars.

scrollbar_y.pack(fill = Y, side = RIGHT)
scrollbar_x.pack(fill = X, side = BOTTOM)
canv.pack(fill = 'both', expand = True, side = 'left')

#Placement of the scrollbars inside the window

canv.create_window(0, 0, anchor = NW, window = frame) #Creation of the canvas.

root.mainloop() #Infinite loop to catch occurrences of multple events.
