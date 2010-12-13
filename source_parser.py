from source_class import SourceClass
import tokenize
import compiler

class SourceParser():
    def __init__(self, source_file):
        self.source_classes = []
        self.source = compiler.parseFile('test/test_class.py')

        self._get_classes()

    def _get_classes(self):
        walked_classes = compiler.walk(self.source, ClassVisitor())
        self.source_classes = walked_classes.class_names

        self.source_classes[0].set_num_props(compiler.walk(walked_classes.classes[0], PropertyVisitor()).num_props)


    def get_classes(self):
        return self.source_classes

class ClassVisitor(compiler.visitor.ASTVisitor):
    def __init__(self):
        self.class_names = []
        self.classes = []

    def visitClass(self, node):
        self.class_names.append(SourceClass(node.name))
        self.classes.append(node)


class PropertyVisitor(compiler.visitor.ASTVisitor):
    def __init__(self):
        self.num_props = 0

    def visitAssAttr(self, node):
        self.num_props += 1
        
