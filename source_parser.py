from source_class import SourceClass
import tokenize
import compiler

class SourceParser():
    def __init__(self, source_file):
        self.source_classes = []
        self.source = compiler.parseFile('test/test_class.py')

        self._get_classes()

    def _get_classes(self):
        self.source_classes = compiler.walk(self.source, Visitor())._class_names

    def get_classes(self):
        return self.source_classes

class Visitor(compiler.visitor.ASTVisitor):
    def __init__(self):
        self._class_names = []

    def visitName(self, node):
        import pdb; pdb.set_trace()

    def visitFunction(self, node):
        import pdb; pdb.set_trace()
        print node.name

    def visitClass(self, node):
        self._class_names.append(SourceClass(node.name))
    
