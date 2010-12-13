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

        num_props = []
        for class_node in walked_classes.class_nodes:
            num_props.append(compiler.walk(class_node, PropertyVisitor()).num_props)

        self.source_classes = []
        for source_class in zip(walked_classes.class_nodes, num_props):
            self.source_classes.append(SourceClass(source_class[0].name, source_class[1]))

    def get_classes(self):
        return self.source_classes

class ClassVisitor(compiler.visitor.ASTVisitor):
    def __init__(self):
        self.class_names = []
        self.class_nodes = []

    def visitClass(self, node):
        self.class_nodes.append(node)


class PropertyVisitor(compiler.visitor.ASTVisitor):
    def __init__(self):
        self.num_props = 0

    def visitAssAttr(self, node):
        self.num_props += 1
        
