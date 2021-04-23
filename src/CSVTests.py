import unittest
from CsvReader import Csv1, ClassFactory


class Csv1Test(unittest.TestCase):

    # def setUp(self):
    #     self.file_name='squareRoot.csv'
    #     self.class_name = "square_root"
    #     self.csvReader = CsvReader(self.file_name)

    def test_AdditionCsv(self):
        """Test function for addition"""

        self.file_name = "addition.csv"
        self.class_name = "addition"
        self.csvReader = Csv1(self.file_name)

        self.return_data_as_objects()

    def test_SubtractionCsv(self):
        self.file_name = "subtraction.csv"
        self.class_name = "subtraction"
        self.csvReader = Csv1(self.file_name)

        self.return_data_as_objects()

    def test_MultiplicationCsv(self):
        self.file_name = "multiplication.csv"
        self.class_name = "multiplication"
        self.csvReader = Csv1(self.file_name)

        self.return_data_as_objects()

    def test_DivisionCsv(self):
        self.file_name = "division.csv"
        self.class_name = "division"
        self.csvReader = Csv1(self.file_name)

        self.return_data_as_objects()

    def test_SquareCsv(self):
        self.file_name = "square.csv"
        self.class_name = "square"
        self.csvReader = Csv1(self.file_name)

        self.return_data_as_objects()

    def test_SquareRootCsv(self):
        """Test function for square root"""

        self.file_name = "squareRoot.csv"
        self.class_name = "square_root"
        self.csvReader = Csv1(self.file_name)

        self.return_data_as_objects()

    def return_data_as_objects(self):
        # Return list of list objects having the values and result

        # class_obj is a list
        class_obj = self.csvReader.return_data_as_objects(self.class_name)

        # Assert class_obj a list or not
        self.assertIsInstance(class_obj, list)

        # Call ClassFactory method from CsvReader class
        # Return a type object of class addition with dictionary csv value

        test_class = ClassFactory(self.class_name, self.csvReader.data[0])

        for obj in class_obj:
            self.assertEqual(obj.__name__, test_class.__name__)


if __name__ == '__main__':
    unittest.main()