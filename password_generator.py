# name: Vivian Chau
# github username: vivianchau1997
# date: 09/10/2023

# This is a password generator in Python.

# The user generates a password length.
# The app returns a password of that length

from tkinter import*

import pyperclip

import random

# initializing Tkinter

root = Tk()

root.title("Password Generator App")

root.geometry("500x300")

# creating a variable to store generated password
pass_str = StringVar()

# creating a variable to take password length input from user
pass_len = IntVar()

# initializing length of the password to 0
pass_len.set(0)


def generate():
    """generates a random password of the length that the user inputs"""
    # storing keys in a list which will be used to generate password
    pass_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                 'p', 'q', 'r', 's', 't', 'u', 'v', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G','H', 'I', 'J', 'K', 'L', 'M',
                 'N', 'O','P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2','3',
                 '4', '5', '6', '7', '8', '9', '0', '', '!', '@', '#', '$', '%', '^', '&',
                 '*', '(', ')']

    # declaring empty string
    password = ""

    # using a loop to generate random characters for the length entered by the user
    for character in range(pass_len.get()):
        password = password + random.choice(pass_char)

    # setting te password to the entry widget
    pass_str.set(password)


def copy_to_clipboard():
    """copies the generated password to the clipboard"""
    random_password = pass_str.get()
    pyperclip.copy(random_password)

# Below are the GUI widgets


Label(root, text="Password Generator Application", font=("Calibri Bold", 20)).pack()

Label(root, text="Enter password length").pack(pady=3)

Entry(root, textvariable=pass_len).pack(pady=3)

Button(root, text="Generate Password", command=generate).pack(pady=7)

Entry(root, textvariable=pass_str).pack(pady=3)

Button(root, text="Copy to clipboard", command=copy_to_clipboard).pack()

root.mainloop()  # runs the application in an infinite loop when it's in ready state
