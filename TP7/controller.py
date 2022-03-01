"""
    controller.py makes the controller part of the MVC model for the phonebook
    homework
"""
from __future__ import absolute_import
import view_obj
import view_cli
from model import Ensemble
from model import Person

__author__ = 'George Alehandro Saad'


class Controller():
    '''
    Defining the controller class and its methods.
    '''

    def __init__(self):
        '''
        Controller class constructor.
        '''
        self.view = view_cli.View(self)
        self.model = Ensemble()

    def start_view(self):
        '''
        Calls for the view interface.
        '''
        self.view.main()

    def switch_view(self):
        '''
        Switches from the CLI view into graphical one (Tkinter).
        '''
        self.view = view_obj.View(self)
        self.start_view()

    def search(self):
        '''
        Processes the search request of a person inside the notebook.
        '''
        values_unpack = self.view.get_value()
        if values_unpack:
            fetching = self.model.search_person(values_unpack)
            # if fetching is not None:
            # if fetching is not None:
            self.view.result_presentation(fetching)

    def delete(self, specific=None):
        '''
        Processes the removal request of a person inside the notebook.
        '''
        if specific is None:
            values_unpack = self.view.get_value()
        else:
            values_unpack = specific
        person = Person(*values_unpack)
        deleted = self.model.delete_person(person)
        print(deleted)
        self.view.delete_display('Deleted', deleted)

    def reset_id(self):
        '''
        Used to reset the ID incrementation
        '''
        message = self.model.reset_id()
        self.view.message_display('Operation', message)

    def insert(self):
        '''
        Processes the insert request of a person inside the notebook.
        '''
        values_unpack = self.view.get_value()
        if values_unpack:
            person = Person(*values_unpack)
            inserted = self.model.insert_person(person)
            self.view.message_display('Operation', inserted)

    def display(self):
        '''
        Displays the content of the notebook.
        '''
        contain = self.model.display_all()
        self.view.result_presentation(contain)
