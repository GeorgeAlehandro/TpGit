# coding: utf-8
"""
CLI View of the project

"""
from __future__ import absolute_import
import argparse
from view import SuperView


class View(SuperView):
    '''
    Class for the CLI view (inherits from SuperView)
    '''

    def __init__(self, controller):
        '''
        Constructor for the cli view.
        '''
        super().__init__(controller)
        self.args = []
        self.status = False
        self.parser = self.create_parser()

    def create_parser(self):
        """ Declares new parser and adds parser arguments
        Two group of parsers: Optional and required"""
        program_description = ''' Phonebook MVC model.
        For inserting, deleting, and searching, using the order:
              'Surname, Name, Telephone, Address, City' '''
        self.parser = argparse.ArgumentParser(
            add_help=True, description=program_description)
        exclsv_args = self.parser.add_mutually_exclusive_group()
        exclsv_args.add_argument('-r', '--removeperson',
                                 help="to delete person",
                                 action='store_true')
        exclsv_args.add_argument('-i', '--insertperson',
                                 help="to insert person",
                                 action='store_true')
        exclsv_args.add_argument('-s', '--searchperson',
                                 help="to search person",
                                 action='store_true')
        exclsv_args.add_argument('-d', '--displaydata',
                                 help="to show all data", action='store_true')
        exclsv_args.add_argument('-reset', '--resetID',
                                 help="to reset ID incrementation", action='store_true')
        exclsv_args.add_argument('-g', '--GUI', help="switch to GUI mode",
                                 action='store_true')
        return self.parser

    def run(self, args):
        '''
        Assign a command for each called argument.
        '''
        if args.displaydata:
            self.controller.display()
        if args.insertperson:
            self.controller.insert()
            # self.controller.save_notebook()
        if args.removeperson:
            self.controller.delete()
           # self.controller.save_notebook()
        if args.searchperson:
            self.controller.search()
        if args.resetID:
            self.controller.reset_id()
        if args.GUI:
            self.controller.switch_view()

    def get_value(self):
        '''
        Fetching the value for each user-entry.
        '''
        entry_fetch = ["", '', '', '', '', '']
        i = 0
        for element in self.entries:
            entry_fetch[i] = input('What is the ' + element + '?'+'\n')
            i += 1
        if all(item == '' for item in entry_fetch):
            print(self.error_messages[3])
            return False
        if not entry_fetch[3].isdigit() and entry_fetch[3] != '':
            print(self.error_messages[2])
            return False
        return entry_fetch

    def delete_display(self, title, result):
        '''
        Message display after delete.
        '''
        if result is not None:
            print(title, result)
        else:
            print(self.error_messages[1])

    def message_display(self, title, result):
        '''
        Message display after insertion
        '''
        if result is not None:
            print(title, result)
        else:
            print(self.error_messages[0])

    def result_presentation(self, items_list):
        '''
        Results presentation after fetching.
        '''
        if items_list is not None:
            print('ID'+'\t'+'Surname'+'\t'+'Name' +
                  '\t'+'Tel'+'\t'+'Address'+'\t'+'City')
            print('------------------------------------------------')
            for person in items_list:
                print(str(person[0]) + '\t' +
                      person[1]+'\t'+person[2]+'\t' +
                      person[3]+'\t' + person[4]+'\t' +
                      person[5])

    def main(self):
        '''
        Main execution of the cli view.
        '''
        # self.create_interface()
        self.parser.set_defaults(func=self.run)
        args = self.parser.parse_args()
        args.func(args)
