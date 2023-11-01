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

