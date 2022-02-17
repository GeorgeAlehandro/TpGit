# coding: utf-8

import os
from tkinter import Button
from tkinter import Entry
from tkinter import filedialog
from tkinter import Label
from tkinter import Menu
from tkinter import StringVar
from tkinter import Tk
from tkinter import Toplevel
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Treeview
"""
Class View of the project

@author : Olivier CHABROL
"""


class View(Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.widgets_labs = {}
        self.widgets_entry = {}
        self.widgets_button = {}
        self.entries = ["Nom", "Prenom", "Telephone", "Adresse", "Ville"]
        self.buttons = ["Chercher", "Inserer", "Effacer", "Display"]
        self.modelListFields = []
        self.fileName = None
        self.windows = {}
        self.windows["fenetreResult"] = ...
        self.windows["fenetreErreur"] = ...

    def get_value(self):
        entry_fetch = self.widgets_entry["Nom"].get(), self.widgets_entry["Prenom"].get(
        ), self.widgets_entry["Telephone"].get(), self.widgets_entry["Adresse"].get(), self.widgets_entry["Ville"].get()
        if all(item == '' for item in entry_fetch):
            messagebox.showerror('Entry unavailable',
                                 'Entries cannot be all empty.')
            return False
        return entry_fetch

    def create_fields(self):
        i, j = 0, 0

        for idi in self.entries:
            lab = Label(self, text=idi.capitalize())
            self.widgets_labs[idi] = lab
            lab.grid(row=i, column=0)

            var = StringVar()
            entry = Entry(self, text=var)
            self.widgets_entry[idi] = entry
            entry.grid(row=i, column=1)

            i += 1

        for idi in self.buttons:
            buttonW = Button(self, text=idi, command=(
                lambda button=idi: self.controller.button_press_handle(button)))
            self.widgets_button[idi] = buttonW
            buttonW.grid(row=i+1, column=j)
            # self.widgets_button[idi].config(command = idi)

            j += 1

    def result_display(self, title, result):
        if result is not None:
            messagebox.showinfo(title, result)
        else:
            messagebox.showerror(title, 'not found')

    def on_closing(self):
        message_closing = "Do you want to quit? Modifications will be saved."
        if messagebox.askokcancel("Quit", message_closing):
            self.controller.save_notebook()
            self.destroy()

    def result_presentation(self, items_list):
        treepresentation = Toplevel(self)
        treepresentation.title("Addresse Book")
        columns = ("Name", "Prenom", "Telephone", "Adresse", "Ville")
        tree = Treeview(treepresentation, columns=columns, show='headings')
        tree.heading("Name", text="Name")
        tree.heading("Prenom", text="Prenom")
        tree.heading("Telephone", text="Telephone")
        tree.heading("Adresse", text="Adresse")
        tree.heading("Ville", text="Ville")

        for person in items_list:
            tree.insert("", "end", values=(
                person['name'], person['prenom'], person['telephone'], person['adresse'], person['ville']))

        tree.grid(row=0, column=0, sticky='nsew')

        def item_selected(event):
            for selected_item in tree.selection():
                item = tree.item(selected_item)
                record = item['values']
                print(record)
                messagebox.showinfo(title='Information',
                                    message=record, parent=treepresentation)
        tree.bind('<<TreeviewSelect>>', item_selected)
        quit_button = Button(treepresentation,  text="Quit",
                             command=lambda: treepresentation.destroy())
        quit_button.grid(row=1, column=0, sticky='s')

    def main(self):
        print("[View] main")
        self.title("Annuaire")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.mainloop()
        self.mainloop()
        self.mainloop()
