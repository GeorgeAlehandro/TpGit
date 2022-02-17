# coding: utf-8
"""
CLI View of the project

"""
import argparse
import sys
import os


class View():
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.args = []

    def create_parser(self):
        """ Declares new parser and adds parser arguments
        Two group of parsers: Optional and required"""
        program_description = ''' reading fasta file and checking sequence
        format '''
        parser = argparse.ArgumentParser(
            add_help=True, description=program_description)
        requiredarg = parser.add_argument_group('required named arguments')
        # requiredarg.add_argument('-i', '--inputfile', default=sys.stdin,
        #                          help="required input file in fasta format",
        #                          type=self.FileType("r"), required=True)
        parser.add_argument('-r', '--removeperson',
                            help="to delete person",
                            type=tuple, required=False)
        parser.add_argument('-i', '--insertperson',
                            help="to insert person",
                            nargs='+', required=False)
        parser.add_argument('-s', '--searchperson',
                            help="to search person",
                            nargs='+', required=False)
        parser.add_argument('-d', '--displaydata',
                            help="to show all data", action='store_true')
        return parser

    def run(self, args):
        if args.displaydata:
            self.controller.display()
        if args.insertperson:
            self.controller.insert()
            self.controller.save_notebook()
        if args.removeperson:
            self.controller.delete()
            self.controller.save_notebook()
        if args.searchperson:
            self.controller.search()

    def get_value(self):
        entry_fetch = ['', '', '', '', '']
        i = 0
        if len(sys.argv) < 2:
            print('Error entry empty')
            return False
        for item in sys.argv:
            try:
                entry_fetch[0+i] = sys.argv[2+i]
                i += 1
            except IndexError:
                break
        return entry_fetch

    def tuple_changer(self, a, b, c, d, e):
        query = (a, b, c, d, e)
        return query

    def create_fields(self):
        pass

    def result_display(self, title, result):
        if result is not None:
            print(title, result)
        else:
            print('Error not found')

    def on_closing(self):
        pass

    def result_presentation(self, items_list):
        for item in items_list:
            print(item)
    # should find a different to present the results in the cmd, for example use a tabular form

    def main(self):
        print("[View] cli")
        parser = self.create_parser()
        parser.set_defaults(func=self.run)
        args = parser.parse_args()
        args.func(args)
# TODO FIND A SIMPLER STRUCTURE OF ARGUMENTS, SHI ENNO BYE2BAL GET VALUE MASALAN
