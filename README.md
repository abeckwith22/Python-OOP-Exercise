### Python OOP Exercise

My submission for 22.4 Python OOP Exercises

`serialgenerator.py`
```python
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
```

`randomword.py`
```python
from random import choice
class WordFinder:
    def __init__(self, path='./'):
        self.path = str(path)
        self.wordList = []
        
        self.getLines()
    
    def getTextFile(self):
        return self.path
    
    def getLines(self):
        with open(self.path, 'r') as file:
            for line in file:
                self.wordList.append(line.replace('\n', ''))
    
    def getWordList(self):
        return self.wordList
    
    def random(self):
        return choice(self.wordList)

class SpecialWordFinder(WordFinder):
    def __init__(self, path):
        super().__init__(path)
        self.specialWordList = []

        self.getWordList()
    
    def getTextFile(self):
        return super().getTextFile()
    
    def getLines(self):
        return super().getLines()
    
    def getWordList(self):
        wl = super().getWordList()
        for line in wl:
            if (line.find('#') == -1 and line != '' and line != '\n'):
                self.specialWordList.append(line)
        
        return self.specialWordList
    
    def random(self):
        return choice(self.specialWordList)

if __name__ == '__main__':
    wf = WordFinder('cat')
    print(wf.random())

    swf = SpecialWordFinder('dog')
    print(swf.random())

```
