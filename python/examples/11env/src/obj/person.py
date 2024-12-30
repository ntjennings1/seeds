""" Import objects. """
from obj.mammal import Mammal

class Person(Mammal): 

    """ 
        A class representation of a person. 

        ```
        Attributes
        ----------
        name : str 
            The person's name. 
    """

    """ Initialize a new person.
    
    @return null
    """
    def __init__(self): 
        super().__init__()
        self.name = ""

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name