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

    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size