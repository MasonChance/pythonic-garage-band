

class Band:
    lineup = []

    def __init__(self, name, members=[]):
        self.name = name
        self.members = members
        lineup.append(self.name)

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"

    #TODO: clarify- what factors decide weather to use dunder in declaring a fn:

    def play_solos(self) -> list:

        jam = []

        for idol in self.members:
            jam.append(idol.play_solo()) 
        return jam

    @classmethod
    def to_list(cls):
        return cls.lineup
        

# TODO: Clarify- is `.instances` a reserved attr. of the python class object??? 

class Musician:
    # def __init__(self): TODO: clarify- do super classes not need an init function as their only purpose is to pass common attributes to instances of the subclasses that inherit from it???? 
   
    def get_instrument(self):
        return f'{self.instrument}'

    # if each instance of subclass is to share a method between them, why am I continually getting linter errors "instance of class has no attribute {attr.name as self.attr}. the tests pass regardless of decorator or lack thereof but linter still throws. 

    def play_solo(self):
        return f'{self.solo}'


class Guitarist(Musician):
    instrument = 'guitar'
    solo = 'face melting guitar solo'

    def __init__(self, name='None'):
        self.name = name
        # self.instrument = 'guitar'
        # attributes that are static, ie: not-assigned as arguments to the function, must be assigned prior or outside of the __init__ fn:
    
    def __str__(self):
        return f'My name is {self.name} and I play guitar'

    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'


class Bassist(Musician):

    instrument = 'bass'
    solo = 'bom bom buh bom'

    def __init__(self, name='none'):
        self.name = name
        self.instrument = 'bass'
    def __str__(self):
        return f'My name is {self.name} and I play bass'

    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'



class Drummer(Musician):

    instrument = 'drums'
    solo = 'rattle boom crash'

    def __init__(self, name='None'):
        self.name = name
        self.instrument = 'drums'
    def __str__(self):
        return f'My name is {self.name} and I play drums'
    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'