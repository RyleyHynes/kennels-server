class Location():

    """Defining a class for Locations"""

    # Class initializer. It has parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address
