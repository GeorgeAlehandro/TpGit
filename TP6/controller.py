from view_obj import View
from model import Ensemble
from model import Person


class Controller():
    def __init__(self):
        self.view = View(self)
        self.model = Ensemble()

    def start_view(self):
        self.view.create_fields()
        self.view.main()

    def search(self):
        values_unpack = self.view.get_value()
        if values_unpack:
            a = self.model.search_person(values_unpack)
            self.view.result_display('Found', a)
            self.view.result_presentation(a)

    def delete(self):
        values_unpack = self.view.get_value()
        if values_unpack:
            deleted = self.model.delete_person(values_unpack)
            self.view.result_display('Deleted', deleted)

    def insert(self):
        values_unpack = self.view.get_value()
        person = Person(*values_unpack)
        inserted = self.model.insert_person(person)
        self.view.result_display('Successfuly inserted', inserted)

    def save_notebook(self):
        print('Tried to save.')
        self.model.save()

    def display(self):
        contain = self.model.display_all()
        self.view.result_presentation(contain)

    def button_press_handle(self, buttonId):
        print("[Controller][button_press_handle] " + buttonId)
        if buttonId == "Chercher":
            self.search()
        elif buttonId == "Effacer":
            self.delete()
        elif buttonId == "Inserer":
            self.insert()
        elif buttonId == "Display":
            self.display()
        else:
            pass


if __name__ == "__main__":
    controller = Controller()
    controller.start_view()
