from dict import *
LEADING_CHARACTERS = dict[consonant_classes]

class Character:
    def __init__(self, char, position, cluster_role, char_role, before, after):
        self.character = char
        self.position = position
        self.role = role
        self.before = before
        self.after = after
    def getInformation(self):
        return f'Character: {self.char}\nPosition: {self.position}\nRole: {self.role}\nChracters Before: {self.before}\nCharacters After: {self.after}'
    def getBefore(self, distance):
        distance += 1
        if len(self.before) < distance:
            return None
        return self.before[-distance]
    def getAfter(self, distance):
        if len(self.after) < distance:
            return None
        return self.after[distance]

class Syllable:
    def __init__(self, string):
        self.chars = []
        for index, char in enumerate(string):
            before = string[:index]
            after = string[index+1:]
            self.chars.append(Character(char, index, 'unknown', 'unknown', before, after))
    def getInformation(self):
        information = f''
        return information

class Cluster:
    def __init__(self, cluster_role, chars):
        self.cluster_role = cluster_role
        self.chars = chars
    def findCharRole(self, target_char_role):
        return next((char for char in self.chars if char.char_role == target_char_role), None)