from dict import *

text = ('เคราะห์')
no_tones = []
text_lists = []
text_vowels = []
split_indexes = []
syllables = []

class ThaiCharacter:
    def __init__(self, character, position, before, after):
        self.character = character
        self.position = position
        self.before = before
        self.after = after
    def information(self):
        information = f"Character: {self.position}\nPosition: {self.character}\nChracters Before: {self.before}\nCharacters After: {self.after}"
        return information
    def getBefore(self, distance):
        if len(self.before):
            return "No character there"
        return self.before[-distance]
    def getAfter(self, distance):
        if len(self.after) < distance:
            return "No character there"
        return self.after[distance]

char = ThaiCharacter('ก', 1, ['เ'], ['ร','ี','ย','น'])
print(char.getAfter(2))