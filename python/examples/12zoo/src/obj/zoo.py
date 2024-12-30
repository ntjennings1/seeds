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
    """

    """ Initialize a new zoo.
    
    @return null
    """
    def __init__(self): 
        self.name = ""
        self.occupancy = 0
        self.creatures = []
        
        self.create()

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
    
    def get_occupancy(self):
        return self.occupancy
    
    def set_occupancy(self, occupancy):
        self.occupancy = occupancy

    def get_creatures(self):
        return self.creatures
    
    def set_creatures(self, creatures):
        self.creatures = creatures

    def create(self):

        try:
            self.set_name(input('Enter a zoo name: '))
            self.set_occupancy(int(input('Enter an occupancy: ')))
        except Exception as ex:
            print('Error creating zoo. Check inputs')
            exit(0)

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

    def show(self):

        print()
        print('These are the creatures in', self.get_name(), ':')
        for creature in self.get_creatures():
            
            print(creature.get_name(), 'weighs', creature.get_size(), 'kgs and is a', creature.get_type())