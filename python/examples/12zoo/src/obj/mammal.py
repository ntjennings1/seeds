class Mammal():

    """ 
        A class representation of a mammal. 

        ```
        Attributes
        ----------
        size : str 
            The mammal's size. 
    """

    """ Initialize a new mammal.
    
    @return null
    """
    def __init__(self): 
        self.size = 0
        self.type = ''
        self.name = ''

    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size

    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type
    
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name