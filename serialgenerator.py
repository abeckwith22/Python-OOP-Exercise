""" Serial Generator
Classes are a great way to combine data and functionality

We'll use a class to make a "serial number generator" -- you should be able to initialize it with a start number
"""


class Serial_Generator:
    """Class creates a serial number generator with start of start

    >>> sg = Serial_Generator(start=100)

    >>> sg.generate()
    101

    >>> sg.generate()
    102

    >>> sg.reset()
    100

    >>> sg.generate()
    101
    """
    def __init__(self, start=0):
        "start number (cannot be changed) and value (can be changed)"
        self.start = start
        self.value = start
    
    def generate(self):
        "Increments self.value by 1 and returns value"
        self.value += 1
        return self.value

    def reset(self):
        "Resets value to start"
        self.value = self.start
        return self.value


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    