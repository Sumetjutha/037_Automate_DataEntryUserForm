# import library
from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
from tkinter import messagebox
import openpyxl, xlrd
from openpyxl import Workbook
import pathlib

root=Tk()
root.title("Data Entry")
root.geometry('700x400+300+200')
root.resizable(False,False)
root.configure(bg="#326273")

#icon
icon_image=PhotoImage(file="free.png")
root.iconphoto(False,icon_image)

#heading
Label(root,text="Please fill out this entry form: ", font="arial 13", bg="#326273", fg="#fff").place(x=20, y=20)

root.mainloop()