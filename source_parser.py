from source_class import SourceClass
import tokenize
import compiler

class SourceParser():
    def __init__(self, source_file):
        self.source_classes = []
        self.source = compiler.parseFile('test/test_class.py')

        self._get_classes()

    def _get_classes(self):
        mama = compiler.walk(self.source, Visitor())
        self.source_classes = mama._class_names

        self.source_classes[0].set_num_props(compiler.walk(mama._classes[0], Visitor2())._num_props)


    def get_classes(self):
        return self.source_classes

class Visitor(compiler.visitor.ASTVisitor):
    def __init__(self):
        self._class_names = []
        self._classes = []

    def visitName(self, node):
        import pdb; pdb.set_trace()

    def visitFunction(self, node):
        import pdb; pdb.set_trace()
        print node.name

    def visitClass(self, node):
        self._class_names.append(SourceClass(node.name))
        self._classes.append(node)


class Visitor2(compiler.visitor.ASTVisitor):
    def __init__(self):
        self._num_props = 0

    def visitAssAttr(self, node):
        self._num_props += 1
        
