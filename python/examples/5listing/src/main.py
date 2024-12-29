""" Creates a list of numbers.

@returns null
"""
def catalog():

    size = 5
    catalog = []

    while size > 0:
        catalog.append(size)
        size -= 1

    print("The list created was: ", catalog)
        
""" Runs the catalog function. """
catalog()