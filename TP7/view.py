# coding: utf-8
"""
SuperView

"""


class SuperView():
    '''
    Super class of both views.
    '''

    def __init__(self, controller):
        '''
        constructor of the super class.
        '''
        self.controller = controller
        self.entries = ["ID", "Surname", "Name",
                        "Telephone", "Address", "City"]
        self.error_messages = ["You need to specify name and surname.",
                               "ID not found in phonebook.",
                               "Telephone should be only digits.",
                               'Entries cannot be all empty.',
                               "Deletion is only made based on ID."
                               ]

    # def create_interface(self):
    #     pass

    # def get_value(self):
    #     pass

    # def delete_display(self, title, result):
    #     pass

    # def insertion_display(self, title, result):
    #     pass

    # def result_presentation(self, items_list):
    #     '''
    #     Results presentation after fetching.
    #     '''
    #     pass

    # def main(self):
    #     pass
