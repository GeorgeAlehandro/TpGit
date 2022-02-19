# coding: utf-8

import os
from view import SuperView
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
from ttkwidgets.autocomplete import AutocompleteEntry
from autocomplete import AutocompleteEntry
"""
Class View of the project

@author : Olivier CHABROL
"""


class View(Tk, SuperView):
    def __init__(self, controller):
        super().__init__()
        SuperView.__init__(self, controller)
        self.widgets_labs = {}
        self.widgets_entry = {}
        self.widgets_button = {}
        self.buttons = ["Chercher", "Inserer", "Remove"]
        self.extrabuttons = ["Content", "Clear"]
        self.modelListFields = []
        self.fileName = None
        self.windows = {}
        self.windows["fenetreResult"] = ...
        self.windows["fenetreErreur"] = ...

    def get_value(self):
        entry_fetch = self.widgets_entry["Surname"].get(), self.widgets_entry["Name"].get(
        ), self.widgets_entry["Telephone"].get(), self.widgets_entry["Address"].get(), self.widgets_entry["City"].get()
        if all(item == '' for item in entry_fetch):
            messagebox.showerror('Entry unavailable',
                                 'Entries cannot be all empty.')
            return False
        if not self.widgets_entry["Telephone"].get().isdigit() and self.widgets_entry["Telephone"].get() != '':
            messagebox.showerror(
                'Insertion error', "Telephone should be only digits.")
            return False
        return entry_fetch

    def create_fields(self):
        i, j, h = 0, 0, 0

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
                lambda button=idi: self.button_press_handle(button)))
            self.widgets_button[idi] = buttonW
            buttonW.grid(row=i+1, column=j)
            # self.widgets_button[idi].config(command = idi)

            j += 1
        for idi in self.extrabuttons:
            buttonW = Button(self, text=idi, command=(
                lambda button=idi: self.button_press_handle(button)))
            self.widgets_button[idi] = buttonW
            buttonW.grid(row=h, column=2, rowspan=2)
            # self.widgets_button[idi].config(command = idi)

            h += 2

    def delete_display(self, title, result):
        if result is not None:
            messagebox.showinfo(title, result)
        else:
            messagebox.showerror(title, 'Surname Name not found in phonebook.')

    def insertion_display(self, title, result):
        if result is not None:
            messagebox.showinfo(title, result)
        else:
            messagebox.showerror(
                title, 'You need to specify name and surname.')

    def on_closing(self):
        message_closing = "Do you want to quit? Modifications will be saved."
        if messagebox.askokcancel("Quit", message_closing):
            self.controller.save_notebook()
            self.destroy()

    def result_presentation(self, items_list):
        if items_list is not None:
            treepresentation = Toplevel(self)
            treepresentation.title("Address Book")
            columns = ("Surname", "Name", "Telephone", "Address", "City")
            tree = Treeview(treepresentation, columns=columns, show='headings')
            tree.heading("Surname", text="Surname")
            tree.heading("Name", text="Name")
            tree.heading("Telephone", text="Telephone")
            tree.heading("Address", text="Address")
            tree.heading("City", text="City")

            for person in items_list:
                tree.insert("", "end", values=(
                    person['surname'], person['name'], person['telephone'],
                    person['address'], person['city']))

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
        else:
            messagebox.showerror('Results', 'Results were not found')

    def button_press_handle(self, buttonId):
        if buttonId == "Chercher":
            self.controller.search()
        elif buttonId == "Remove":
            self.controller.delete()
        elif buttonId == "Inserer":
            self.controller.insert()
        elif buttonId == "Content":
            self.controller.display()
        elif buttonId == "Clear":
            for value in self.widgets_entry.values():
                value.delete(0, 'end')

    def main(self):
        print("[View] main")
        self.title("Annuaire")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.create_fields()
        self.mainloop()
