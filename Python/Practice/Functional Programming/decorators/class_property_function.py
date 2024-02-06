class Generic:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected a string")
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")

class Generic2:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected a string")
        self._name = value

    def del_name(self):
        raise AttributeError("Can't delete attribute")

    name = property(get_name, set_name, del_name)
    

class SubGeneric(Generic):
    @property
    def name(self):
        print("Getting name")
        return super().name

    @name.setter
    def name(self, value):
        print("Setting name to", value)
        super(SubGeneric, SubGeneric).name.__set__(self, value)

    @name.deleter
    def name(self):
        print("Deleting name")
        super(SubGeneric, SubGeneric).name.__delete__(self)
