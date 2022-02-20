# coding: utf-8
"""
Tkinter View of the project.

"""

from __future__ import absolute_import
from tkinter import Button
from tkinter import Label
from tkinter import Tk
from tkinter import Toplevel
from tkinter import messagebox
from tkinter.ttk import Treeview
from ttkwidgets.autocomplete import AutocompleteEntry
from view import SuperView


class View(Tk, SuperView):
    '''
    Class for the Tkinter view (inherits from SuperView)
    '''

    def __init__(self, controller):
        '''
        Constructor for the Tkinter view.
        '''
        super().__init__()
        SuperView.__init__(self, controller)
        self.widgets_labs = {}
        self.widgets_entry = {}
        self.widgets_button = {}
        self.buttons = ["Search", "Insert", "Remove"]
        self.extrabuttons = ["Content", "Clear"]
        self.autocomplete_values = []

    def fetch_autocomplete_values(self):
        '''
        Returns a list containing the elements to be used in the autocompletion
        entry. Elements are inside the memory.
        '''
        (list_surname, list_name,
         list_telephone, list_address,
         list_city) = self.controller.memory_generator()
        self.autocomplete_values = [list_surname, list_name,
                                    list_telephone,
                                    list_address, list_city]
        print(self.autocomplete_values)

    def get_value(self):
        '''
        Returns the values introduced by the user.
        '''
        entry_fetch = (self.widgets_entry["Surname"].get(),
                       self.widgets_entry["Name"].get(
        ), self.widgets_entry["Telephone"].get(),
            self.widgets_entry["Address"].get(),
            self.widgets_entry["City"].get())
        if all(item == '' for item in entry_fetch):
            messagebox.showerror('Entry unavailable',
                                 'Entries cannot be all empty.')
            return False
        if (not self.widgets_entry["Telephone"].get().isdigit() and
                self.widgets_entry["Telephone"].get() != ''):
            messagebox.showerror(
                'Insertion error', "Telephone should be only digits.")
            return False
        # self.list_surname.append(entry_fetch[0])
        # self.list_name.append(entry_fetch[1])
        # self.list_telephone.append(entry_fetch[2])
        # self.list_address.append(entry_fetch[3])
        # self.list_city.append(entry_fetch[4])
        # self.fetch_autocomplete_values()
        return entry_fetch

    def create_fields(self):
        '''
        Creates the different elements of the graphical interface.
        '''
        i, j, k = 0, 0, 0

        for idi in self.entries:
            lab = Label(self, text=idi.capitalize())
            self.widgets_labs[idi] = lab
            lab.grid(row=i, column=0)
            entry = AutocompleteEntry(
                self,
                width=30,
                font=('Times', 12),
                completevalues=self.autocomplete_values[i]

            )
            print(self.autocomplete_values[i])
            self.widgets_entry[idi] = entry
            entry.grid(row=i, column=1)

            i += 1

        for idi in self.buttons:
            buttown = Button(self, text=idi, command=(
                lambda button=idi: self.button_press_handle(button)))
            self.widgets_button[idi] = buttown
            buttown.grid(row=i+1, column=j)
            # self.widgets_button[idi].config(command = idi)

            j += 1
        for idi in self.extrabuttons:
            buttown = Button(self, text=idi, command=(
                lambda button=idi: self.button_press_handle(button)))
            self.widgets_button[idi] = buttown
            buttown.grid(row=k, column=2, rowspan=2)
            # self.widgets_button[idi].config(command = idi)

            k += 2

    def delete_display(self, title, result):
        '''
        Message display after delete.
        '''
        if result is not None:
            messagebox.showinfo(title, result)
        else:
            messagebox.showerror(title, 'Surname Name not found in phonebook.')

    def insertion_display(self, title, result):
        '''
        Message display after insertion
        '''
        if result is not None:
            messagebox.showinfo(title, result)
        else:
            messagebox.showerror(
                title, 'You need to specify name and surname.')

    def on_closing(self):
        '''
        Function that sets the behavior when closing the graphical interface.
        '''
        message_closing = "Do you want to quit? Modifications will be saved."
        if messagebox.askokcancel("Quit", message_closing):
            self.controller.save_notebook()
            self.destroy()

    def result_presentation(self, items_list):
        '''
        Results presentation after fetching.
        '''
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

    def button_press_handle(self, buttonid):
        '''
        Assign a command for each pressed button.
        '''
        if buttonid == "Search":
            self.controller.search()
        elif buttonid == "Remove":
            self.controller.delete()
        elif buttonid == "Insert":
            self.controller.insert()
        elif buttonid == "Content":
            self.controller.display()
        elif buttonid == "Clear":
            for value in self.widgets_entry.values():
                value.delete(0, 'end')

    def main(self):
        '''
        Main execution of the Tkinter view.
        '''
        self.title("Phone Notebook")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.fetch_autocomplete_values()
        self.create_fields()
        self.mainloop()
