import unittest
from source_parser import SourceParser
from tools import *

class SourceParserTest(unittest.TestCase):
    def setUp(self):
        parser = SourceParser('test/test_class.py')
        self.source_classes = parser.get_classes()

    def test_class_name(self):
        self.assertEqual('TestClass', self.source_classes[0].get_name())
        self.assertEqual('TestClass2', self.source_classes[1].get_name())

    def test_class_properties(self):
        self.assertEqual(8, self.source_classes[0].get_num_properties())
        self.assertEqual(2, self.source_classes[1].get_num_properties())

    def test_inheritance(self):
        parser = SourceParser('test/test_inheritance.py')
        self.assertEqual(10, parser.get_classes()[1].get_num_properties())
        


class ToolsTest(unittest.TestCase):
    def setUp(self):
        self.tools = ProgrammingTools('test/test_class.py')

    def test_too_many_properties_warning(self):
        self.assertEqual(TOO_MANY_PROPERTIES % ('TestClass', 8), self.tools.get_warnings()[0])


if __name__ == '__main__':
    unittest.main()
