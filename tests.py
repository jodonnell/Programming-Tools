import unittest
from source_parser import SourceParser


class ToolsTest(unittest.TestCase):
    def setUp(self):
        source_file = open('test/test_class.py')
        parser = SourceParser(source_file)
        self.source_classes = parser.get_classes()


    def test_class_name(self):
        self.assertEqual('TestClass', self.source_classes[0].get_name())
        self.assertEqual('TestClass2', self.source_classes[1].get_name())

    def test_class_properties(self):
        self.assertEqual(8, self.source_classes[0].get_num_properties())
        self.assertEqual(2, self.source_classes[1].get_num_properties())



if __name__ == '__main__':
    unittest.main()
