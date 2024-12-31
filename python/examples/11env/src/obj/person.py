""" Import objects. """
from obj.mammal import Mammal

class Person(Mammal): 

    """ 
        A class representation of a person. 

        ```
        Attributes
        ----------
        size : str 
            The mammal's size. 
        name : str
            The mammal's name. 
    """

    """ Initialize a new person.
    
    @return null
    """
    def __init__(self): 
        super().__init__()