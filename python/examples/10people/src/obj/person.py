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

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name