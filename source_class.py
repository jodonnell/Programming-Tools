
class SourceClass():
    def __init__(self, name):
        self._num_properties = 1
        self._name = name

    def get_num_properties(self):
        return self._num_properties

    def get_name(self):
        return self._name

    def set_num_props(self, num_props):
        self._num_properties = num_props
