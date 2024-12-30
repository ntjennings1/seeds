""" Import objects. """
from person import Person

""" Gathers the persons name.

@return name : The persons name
@rtype name: str
"""
def get_name():

    name = input('Enter a name (e to exit): ')
    return name

""" Repetitively creates people. 

@returns null
"""
def main():
    
    go = True

    while go:

        person = Person() 
        person.name = get_name()

        if person.name.strip() == 'e':
            go = False
        else:
            print(person.name + " was here!")

""" Runs the main function. """
main()