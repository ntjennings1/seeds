""" Import objects. """
from obj.system import System

""" Gathers the system's name.

@return name : The system's name
@rtype name: str
"""
def get_name():

    name = input('Enter a name (e to exit): ')
    return name

""" Repetitively creates a system. 

@returns null
"""
def systems():
    
    go = True

    while go:

        system = System()
        system.name = get_name()

        if system.name.strip() == 'e':
            go = False
        else:
            print(system.name + " was here!")

""" Runs the system function. """
systems()