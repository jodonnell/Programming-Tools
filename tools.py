
# get path
# get all python files within
# scan
# look for high amounts of properties
# look for deep inheritance
# high fan in
# deep nesting
# long methods
# long lines
# unused imports?
# long files
# long classes

from source_parser import SourceParser

TOO_MANY_PROPERTIES = 'In class %s there are %d properties which seems like too much.'

class ProgrammingTools():
    def __init__(self, the_file):
        parser = SourceParser(the_file)
        self.source_classes = parser.get_classes()

    def get_warnings(self):
        warnings = []

        for source_class in self.source_classes:
            if source_class.get_num_properties() > 7:
                warnings.append(TOO_MANY_PROPERTIES % (source_class.get_name(), source_class.get_num_properties()))

        return warnings
