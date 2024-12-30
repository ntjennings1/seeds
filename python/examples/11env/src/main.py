""" Import objects. """
from obj.person import Person

""" Gathers a creature size.

@return name : The creatures size
@rtype name: int
"""
def get_size():

    size = input('Enter a weight in kg (e to exit): ')
    return size

""" Gathers a creature name.

@return name : The persons name
@rtype name: str
"""
def get_name():

    name = input('Enter a name (e to exit): ')
    return name

""" Repetitively creates people

@returns null
"""
def env():
    
    go = True

    while go:

        person = Person() 
        person.set_name(get_name())

        if person.get_name().strip() == 'e':
            go = False
        elif person.get_name().strip() == '':
            pass
        else:
            person.set_size(get_size())
            
            if person.get_size().strip() == 'e':
                go = False
            elif person.get_size().strip() == '':
                pass
            else:
                print(person.get_name() + " is here!")
                print("Their size is :", person.get_size(), "kgs")

""" Runs the main function. """
env()