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
        self.memory_generator()
        self.start_view()

    def search(self):
        '''
        Processes the search request of a person inside the notebook.
        '''
        values_unpack = self.view.get_value()
        if values_unpack:
            fetching = self.model.search_person(values_unpack)
            # if fetching is not None:
            self.view.result_presentation(fetching)

    def delete(self):
        '''
        Processes the removal request of a person inside the notebook.
        '''
        values_unpack = self.view.get_value()
        if values_unpack:
            deleted = self.model.delete_person(values_unpack)
            self.view.delete_display('Deleted', deleted)

    def insert(self):
        '''
        Processes the insert request of a person inside the notebook.
        '''
        values_unpack = self.view.get_value()
        if values_unpack:
            person = Person(*values_unpack)
            inserted = self.model.insert_person(person)
            self.view.insertion_display('Insertion', inserted)

    def save_notebook(self):
        '''
        Controller call for saving the model.
        '''
        print('Progress saved.')
        self.model.save()

    def display(self):
        '''
        Displays the content of the notebook.
        '''
        contain = self.model.display_all()
        self.view.result_presentation(contain)

    def memory_generator(self):
        '''
        Returns a list for each that will then be used for the
        autcompleteEntry
        '''
        list_name = []
        list_surname = []
        list_telephone = []
        list_address = []
        list_city = []
        contain = self.model.display_all()
        for item in contain:
            list_surname.append(item['surname'])
            list_name.append(item['name'])
            list_telephone.append(item['telephone'])
            list_address.append(item['address'])
            list_city.append(item['city'])
        return list_surname, list_name, list_telephone, list_address, list_city
