from source_class import SourceClass
import tokenize
import compiler

class SourceParser():
    def __init__(self, source_file):
        self.source_classes = []
        self.source = compiler.parseFile(source_file)

        self._get_classes()

    def _get_classes(self):
        walked_classes = compiler.walk(self.source, ClassVisitor())

        num_props = []
        for class_node in walked_classes.class_nodes:
            num_props.append(compiler.walk(class_node, PropertyVisitor()).num_props)

        self.source_classes = []
        for source_class in zip(walked_classes.class_nodes, num_props):
            self.source_classes.append(SourceClass(source_class[0].name, source_class[1]))


        for class_node in walked_classes.class_nodes:
            if class_node.asList()[1]:
                parent_class_name = class_node.asList()[1].name

                this_class = None
                for source_class in self.source_classes:
                    if source_class.get_name() == class_node.name:
                        this_class = source_class

                for source_class in self.source_classes:
                    if source_class.get_name() == parent_class_name:
                        this_class.set_num_props(source_class.get_num_properties() + this_class.get_num_properties())

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
        
