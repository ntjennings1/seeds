""" Import objects. """
from obj.person import Person
from obj.mammal import Mammal

class Zoo(): 

    """ 
        A class representation of a zoo. 

        ```
        Attributes
        ----------
        name : str 
            The zoo's name.
        occupancy : int
            The zoo's occupancy.
        creatures : list
            The zoo's creatures.

        Methods
        -------
        create : Sets the zoo's initial characteristics.
        populate : Populates the zoo with people and mammals.
        show : Displays the zoo's creatures and their characteristics.
    """

    """ Initialize a new zoo.
    
    @return null
    """
    def __init__(self): 
        self.name = ""
        self.occupancy = 0
        self.creatures = []
        
        self.create()

    """ Returns the zoo's name.
    
    @return name : The zoo's name
    @rtype name : str
    """
    def get_name(self):
        return self.name

    """ Sets the zoo's name.
    
    @param name : The zoo's name
    @type name : str
    """
    def set_name(self, name):
        self.name = name
    
    """ Returns the zoo's occupancy.
    
    @return occupancy : The zoo's occupancy
    @rtype occupancy : int
    """
    def get_occupancy(self):
        return self.occupancy
    
    """ Sets the zoo's occupancy.
    
    @param occupancy : The zoo's occupancy
    @type occupancy : int
    """
    def set_occupancy(self, occupancy):
        self.occupancy = occupancy

    """ Returns the zoo's creatures.
    
    @return creatures : The zoo's creatures
    @rtype creatures : list
    """
    def get_creatures(self):
        return self.creatures
    
    """ Sets the zoo's creatures.

    @param creatures : The zoo's creatures
    @type creatures : list
    """
    def set_creatures(self, creatures):
        self.creatures = creatures

    """ Sets the zoo's initial characteristics.
    
    @return null
    """
    def create(self):

        try:
            self.set_name(input('Enter a zoo name: '))
            self.set_occupancy(int(input('Enter an occupancy: ')))
        except Exception as ex:
            print('Error creating zoo. Check inputs')
            exit(0)

    """ Populates the zoo with people and mammals.
    
    @return null
    """
    def populate(self):

        print('\nLets populate our zoo with people and mammals\n')

        i=0
        while i < self.get_occupancy():

            try:
                self.get_creatures().append(input('Enter a human name (F L) or mammal type (T): '))

                if len(self.get_creatures()[i].split()) > 1:
                    try:
                        person = Person()
                        person.set_name(self.get_creatures()[i])
                        person.set_size(int(input('Enter ' + person.get_name() + "'s weight in kg: ")))
                        person.set_type('Human')

                        self.get_creatures()[i] = person
                    except Exception as ex:
                        print('Error creating human. Check input')
                        exit(0)
                else:
                    try:
                        mammal = Mammal()
                        mammal.set_type(self.get_creatures()[i])
                        mammal.set_name(str(input('Enter the ' + mammal.get_type() + "'s name: ")))
                        mammal.set_size(int(input('Enter the ' + mammal.get_type() + "'s weight in kg: ")))
                        
                        self.get_creatures()[i] = mammal
                    except Exception as ex:
                        print('Error creating mammal. Check input')
                        exit(0)

            except Exception as ex:
                print('Error creating creature. Check input')
                exit(0)

            i += 1

    """ Displays the zoo's creatures and their characteristics.
    
    @return null
    """
    def show(self):

        print()
        print('These are the creatures in', self.get_name(), ':')
        for creature in self.get_creatures():
            
            print(creature.get_name(), 'weighs', creature.get_size(), 'kgs and is a', creature.get_type())