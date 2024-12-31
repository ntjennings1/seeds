""" Import objects. """
from obj.zoo import Zoo

""" Creates a zoo.

@returns null
"""
def zoo():
    
    zoo = Zoo()
    zoo.populate()
    zoo.show()

""" Runs the zoo function. """
zoo()