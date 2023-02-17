import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

#use excel file with words
dict = pd.read_excel('dictionary.ods')

#PL
def first_PL():
    for i in range(len(dict)):
        fig = plt.figure()
        ax = fig.add_subplot()
        ax.axis('off')
        ax.text(0.1, 0.5, dict.at[i, 'POLISH'], fontsize=40, fontweight='bold')
        plt.show()
        fig = plt.figure()
        ax = fig.add_subplot()
        ax.axis('off')
        ax.text(0.1, 0.5, dict.at[i, 'FRENCH'], fontsize=40, fontweight='bold')
        plt.show()

#FR
def first_FR():
    for i in range(len(dict)):
        fig = plt.figure()
        ax = fig.add_subplot()
        ax.axis('off')
        ax.text(0.1,0.5,dict.at[i, 'FRENCH'], fontsize=40, fontweight='bold')
        plt.show()
        fig = plt.figure()
        ax = fig.add_subplot()
        ax.axis('off')
        ax.text(0.1, 0.5, dict.at[i, 'POLISH'], fontsize=40, fontweight='bold')
        plt.show()

#root window
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('LearnFrench')

#exit button
exit_button = ttk.Button(
    root,
    text='Exit',
    command=lambda: root.quit()
)

exit_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

#PL button
PL_button = ttk.Button(
    root,
    text='PL',
    command= first_PL
)

PL_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

#FR button
FR_button = ttk.Button(
    root,
    text='FR',
    command= first_FR
)

FR_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

root.mainloop()
