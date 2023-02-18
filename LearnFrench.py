import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import random

#use excel file with words
dict = pd.read_excel('dictionary.ods')

#length of game
k=100

#randomize
r = np.random.randint(0, len(dict), size=k)


# MAIN ROOT
###################################################################################################################

def information(rootPL,inftitle,inftext):
    message_box = tk.Toplevel(rootPL)
    message_box.title(inftitle)
    message_box.geometry('400x200')
    message_box['bg'] = '#49A'
    message_label = tk.Label(message_box,
        text = inftext,
        bg = '#49A',
        font = ("Arial", 40)
    )
    message_label.pack(padx=10, pady=10)

    ok_button = tk.Button(message_box, text = 'OK', command = message_box.destroy)
    ok_button.pack(pady=10)

def translate(rootPL,i,a):
    if a == 'POLISH':
        Translate_button = tk.Button(rootPL,
            text = "Show translation",
            command = lambda: information(rootPL,
                'Translation of' + dict.at[r[i],a],
                dict.at[r[i],'FRENCH']
            )
        )
    else:
        Translate_button = tk.Button(
            rootPL,
            text = "Show translation",
            command = lambda: information(rootPL,'Translation of' + dict.at[r[i], a], dict.at[r[i],'POLISH']))
    return Translate_button

def next_word(rootPL,i,a):
    if i < (k-1):
        rootPL.destroy()
        first_language(i + 1, a)
    else:
        showinfo('Information',
                 'This is the last word. Please choose last word or quit the game.'
        )

def last_word(rootPL,i,a):
    if i > 0:
        rootPL.destroy()
        first_language(i - 1, a)
    else:
        showinfo(
            'Information',
            'This is the first word. Please choose next word or quit the game.'
        )

def next_button(rootPL,i,a):
    Next_button = tk.Button(
        rootPL,
        text = "Next word",
        command = lambda: next_word(rootPL,i,a)
    )
    return Next_button

def last_button(rootPL,i,a):
    Last_button = tk.Button(
        rootPL,
        text="Last word",
        command=lambda: last_word(rootPL, i, a)
    )
    return Last_button


def first_language(i,a):
    rootPL = tk.Toplevel(root)
    rootPL.geometry('600x400')
    rootPL.resizable(True, True)
    rootPL.title(a)
    rootPL['bg'] = '#49A'
    l = tk.Label(
        rootPL,
        text = dict.at[r[i],a],
        font=("Arial", 40),
        bg = '#49A',
        #fg = '#10159f'
    )
    ExitPL_button = tk.Button(rootPL, text = "Exit", command = rootPL.destroy)
    Translate_button = translate(rootPL,i,a)
    Next_button = next_button(rootPL,i,a)
    Last_button = last_button(rootPL,i,a)
    l.pack()
    Translate_button.pack(ipadx=5,ipady=4,expand=True)
    Next_button.pack(ipadx=5,ipady=4,expand=True)
    Last_button.pack(ipadx=5,ipady=4,expand=True)
    ExitPL_button.pack(ipadx=5,ipady=4,expand=True)
    rootPL.mainloop()


#root window
root = tk.Tk()
root.geometry('500x400')
root.resizable(True, True)
root.title('LearnFrench')
root['bg'] = '#49A'
root.attributes('-alpha', 0.2)


#exit button
exit_button = ttk.Button(
    root,
    text='Exit',
    command=lambda: root.destroy()
)
exit_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

#PL button
PL_button = ttk.Button(
    root,
    text = 'PL',
    command = lambda: first_language(0,'POLISH')
)
PL_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

#FR button
FR_button = ttk.Button(
    root,
    text = 'FR',
    command = lambda: first_language(0,'FRENCH')
)
FR_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

root.mainloop()
