import csv


def ClassFactory(class_name, dictionary):
    return type(class_name, (object,), dictionary)


class Csv1:
    data = []

    def __init__(self, filepath):

        """Class Constructor"""
        self.data = []
        with open(filepath) as text_data:
            csv_data = csv.DictReader(text_data, delimiter=',')
            for row in csv_data:
                self.data.append(row)

    def return_data_as_objects(self, class_name):
        objects = []
        for row in self.data:
            # Append type objects created by ClassFactory function
            # ClassFactory function uses type(class_name, (object, ), {})
            objects.append(ClassFactory(class_name, row))
        return objects

