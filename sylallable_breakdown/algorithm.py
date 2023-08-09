# from classes import Character, Syllable

from dict import th_all

CONSONANTS = th_all.consonants
VOWELS = th_all.vowels
TONE_MARKS = th_all.tone_marks

LOW_CONSONANTS = th_all.low_consonants
UNPAIRED_LOW_CONSONANTS = th_all.unpaired_low_consonants
PAIRED_LOW_CONSONANTS = th_all.paired_low_consonants
HIGH_CONSONANTS = th_all.high_consonants
MID_CONSONANTS = th_all.mid_consonants

LEADING_CONSONANTS = th_all.leading_consonants

BLENDS = th_all.blends
BLEND_LEADS = th_all.blend_initials

INITIAL_VOWELS = th_all.initial_vowels

class Character:
    def __init__(self, char, position, cluster_role, char_role, before, after):
        self.char = char
        self.position = position
        self.cluster_role = cluster_role
        self.char_role = char_role
        self.before = before
        self.after = after
    def getInformation(self):
        chars_before = []
        chars_after = []
        for char in self.before:
            chars_before.append(char.char)
        for char in self.after:
            chars_after.append(char.char)
        return f'Character: {self.char}\nPosition: {self.position}\nIn Cluster: {self.cluster_role}\nRole: {self.char_role}\nChracters Before: {chars_before}\nCharacters After: {chars_after}'
    def getBefore(self, distance):
        distance += 1
        if len(self.before) < distance:
            return None
        return self.before[-distance]
    def getAfter(self, distance):
        if len(self.after) < distance:
            return None
        return self.after[distance]

class SyllableCharacters:
    def __init__(self, string):
        self.chars = []
        chars = []
        for index, char in enumerate(string):
            thischar = Character(char, index, 'unknown', 'unknown', [], [])
            self.chars.append(thischar)
        for index, char in enumerate(self.chars):
            char.before = self.chars[:index]
            char.after = self.chars[index+1:]
    def getInformation(self):
        information = f''
        return information

class SyllableClusters:
    def __init__(self, initial_vowel, initial_consonants, tone_mark, final_vowels, final_consonants):
        self.initial_vowel_cluster = initial_vowel
        self.initial_consonants_cluster = initial_consonants

class Cluster:
    def __init__(self, cluster_role, chars):
        self.cluster_role = cluster_role
        self.chars = chars
    def findCharRole(self, target_char_role):
        return next((char for char in self.chars if char.char_role == target_char_role), None)

def extract_roles(syllable):
    current_index = 0
    initial_vowel = ''
    initial_consonants = []
    final_vowels = []
    final_consonants = []

    if syllable.chars[0].char in INITIAL_VOWELS:
        initial_vowel = syllable.chars[0]
        current_index += 1
        print('Found initial vowel', current_index)
    
    if syllable.chars[current_index].char in LEADING_CONSONANTS and syllable.chars[current_index].getAfter(0) in UNPAIRED_LOW_CONSONANTS:
        #if not actually lead (Next one is vowel)
        if initial_vowel and syllable.chars[current_index].getAfter(0) in BLENDS:
            initial_consonants = [syllable.chars[current_index]]
            current_index += 1
        initial_consonants = [syllable.chars[current_index], syllable.chars[current_index].getAfter(0)]
        current_index += 2
    elif syllable.chars[current_index].char in CONSONANTS and syllable.chars[current_index].getAfter(0).char in BLENDS:
        #has to check if next one is vowel
        initial_consonants = [syllable.chars[current_index], syllable.chars[current_index].getAfter(0)]
        current_index += 2
    elif syllable.chars[current_index].char is 'ร' and syllable.chars[current_index].getAfter(0).char is 'ร':
        initial_consonants = [syllable.chars[current_index], syllable.chars[current_index].getAfter(0)]
        current_index += 2

    else:
        initial_consonants = [syllable.chars[current_index]]
        current_index += 1

    if syllable.chars[current_index].char in VOWELS:
        #if one vowel
        #if followed by อ ย
        current_index +=0
    
    if syllable.chars[current_index].char:
        current_index +=0

    final_consonants = syllable.chars[current_index+1:]

def test(syllable):
    current_index = 0
    initial_vowel = ''
    initial_consonants = []
    final_vowels = []
    final_consonants = []
    print(syllable.chars[0].char)
    print(syllable.chars[0].getAfter(1).char)
    if syllable.chars[0].char == 'โ' and syllable.chars[0].getAfter(1).char == 'ย':
        print("yse")
        initial_vowel = [syllable.chars[0]]
        final_vowels = [syllable.chars[0].getAfter(1)]
    print(initial_vowel[0].getInformation)
    print(final_vowels[0].getInformation())

syl = SyllableCharacters('โดย')
test(syl)