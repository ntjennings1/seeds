class Mammal():

    """ 
        A class representation of a mammal. 

        ```
        Attributes
        ----------
        size : str 
            The mammal's size. 
        type : str
            The mammal's type.
        name : str
            The mammal's name.
    """

    """ Initialize a new mammal.
    
    @return null
    """
    def __init__(self): 
        self.size = 0
        self.type = ''
        self.name = ''

    """ Returns the mammal's size.
    
    @return size : The mammal's size
    @rtype size : int
    """
    def get_size(self):
        return self.size

    """ Sets the mammal's size.
    
    @param size : The mammal's size
    @type size : int
    """
    def set_size(self, size):
        self.size = size

    """ Returns the mammal's type.
    
    @return type : The mammal's type
    @rtype type : str
    """
    def get_type(self):
        return self.type

    """ Sets the mammal's type.
    
    @param type : The mammal's type
    @type type : str
    """
    def set_type(self, type):
        self.type = type
    
    """ Returns the mammal's name.
    
    @return name : The mammal's name
    @rtype name : str
    """
    def get_name(self):
        return self.name

    """ Sets the mammal's name.
    
    @param name : The mammal's name
    @type name : str
    """
    def set_name(self, name):
        self.name = name