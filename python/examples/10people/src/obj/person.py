class Person(): 

    """ 
        A class representation of a person. 

        ```
        Attributes
        ----------
        name : str 
            The person's name. 
    """

    """ Initialize a new person (constructor).
    
    @return null
    """
    def __init__(self): 
        self.name = ""

    """ Returns the person's name.
    
    @return name : The person's name
    @rtype name : str
    """
    def get_name(self):
        return self.name

    """ Sets the person's name.
    
    @param name : The person's name
    @type name : str
    """
    def set_name(self, name):
        self.name = name