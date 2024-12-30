""" Import objects. """
from person import Person

""" Gathers a persons name.

@return name : The persons name
@rtype name: str
"""
def get_name():

    name = input('Enter a name (e to exit): ')
    return name

""" Repetitively creates people

@returns null
"""
def main():
    
    go = True

    while go:

        person = Person() 
        person.set_name(get_name())

        if person.get_name().strip() == 'e':
            go = False
        else:
            print(person.get_name() + " was here!")

""" Runs the main function. """
main()