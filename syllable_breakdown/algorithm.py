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
    def __init__(self, char, position, before, after, cluster='unknown', char_role='unknown'):
        self.char = char
        self.position = position
        self.cluster = cluster
        self.role = char_role
        self.before = before
        self.after = after
    def getInformation(self):
        chars_before = []
        chars_after = []
        for char in self.before:
            chars_before.append(char.char)
        for char in self.after:
            chars_after.append(char.char)
        return f'Character: {self.char}\nPosition: {self.position}\nIn Cluster: {self.cluster}\nRole: {self.role}\nChracters Before: {chars_before}\nCharacters After: {chars_after}'
    def getBefore(self, distance):
        distance += 1
        if len(self.before) < distance:
            return None
        return self.before[-distance]
    def getAfter(self, distance):
        print(len(self.after) < distance)
        if len(self.after) < distance:
            return None
        return self.after[distance]

class SyllableCharacters:
    def __init__(self, string):
        self.string = string
        self.chars = []
        for index, char in enumerate(string):
            thischar = Character(char, index)
            self.chars.append(thischar)
        for index, char in enumerate(self.chars):
            char.before = self.chars[:index]
            char.after = self.chars[index+1:]
    def getInformation(self):
        information = f''
        return information

class Cluster:
    def __init__(self, string, inital_vowels, initial_consonants, tone_marks, final_vowels, final_consonants):
        self.string = string
        self.initial_vowel_cluster = inital_vowels
        self.initial_consonants_cluster = initial_consonants
        self.tone_marks_cluster = tone_marks
        self.final_vowels_cluster = final_vowels
        self.final_consonants_cluster = final_consonants


def find_initial_vowels_cluster(syllable):
    initial_vowels = []
    current_index = 0
    if syllable.chars[0].char in INITIAL_VOWELS:
        initial_vowels = [syllable.chars[0]]
        current_index += 1

    return [current_index, initial_vowels]

def find_initial_consonants_cluster(syllable, current_index, ee_initial):
    w_vowel = False

    first_consonant = syllable.chars[current_index]
    potential_second_consonant = first_consonant.getAfter(0)

    initial_consonants = [first_consonant]
    current_index += 1

    if potential_second_consonant.char in CONSONANTS:

        if potential_second_consonant.char == 'อ':
            return [current_index, initial_consonants, w_vowel]
        
        if potential_second_consonant.char == 'ย' and ee_initial:
            return [current_index, initial_consonants, w_vowel]

        if potential_second_consonant.char == 'ว':
            for chars in syllable.chars:
                if chars.char in VOWELS:
                    initial_consonants.append(potential_second_consonant)
                    current_index += 1
                    return [current_index, initial_consonants, w_vowel]
            w_vowel = True
            return [current_index, initial_consonants, w_vowel]
        
        initial_consonants.append(potential_second_consonant)
        current_index += 1

        #Support implied oh pls
    return [current_index, initial_consonants, w_vowel]

def find_final_vowels_and_tone_marks_clusters(syllable, current_index, ee_initial, ai_initial, w_vowel):
    final_vowels = []
    tone_marks = []

    def append_loop(first_index, final_index):
        final_index += 1
        for index in range(first_index, final_index):
            if syllable.chars[index].char in TONE_MARKS:
                tone_marks.append(syllable.chars[index])
                continue
            final_vowels.append(syllable.chars[index])
        return final_index

    for potential_a_index in range(current_index, len(syllable.chars)):
        if syllable.chars[potential_a_index].char == 'ะ':
            current_index = append_loop(current_index, potential_a_index)
            return [current_index, final_vowels, tone_marks]
    
    for potential_oo_index in range(current_index, len(syllable.chars)):
        if syllable.chars[potential_oo_index].char == 'อ':
            current_index = append_loop(current_index, potential_oo_index)
            return [current_index, final_vowels, tone_marks]
    
    for potential_y_index in range(current_index, len(syllable.chars)):
        if syllable.chars[potential_y_index].char == 'ย':
            y = syllable.chars[potential_y_index]
            if ai_initial:
                current_index = append_loop(current_index, potential_y_index)
                return [current_index, final_vowels, tone_marks]
            if ee_initial:
                for potential_ii_index in range(current_index, potential_y_index):
                    if syllable.chars[potential_ii_index].char == 'ี':
                        current_index = append_loop(current_index, potential_y_index)
                        return [current_index, final_vowels, tone_marks]
                if y.getAfter[0] == '์':
                    break
                current_index = append_loop(current_index, potential_y_index)
                return [current_index, final_vowels, tone_marks]

    if (syllable.chars[current_index].char in TONE_MARKS and syllable.chars[current_index].getAfter(0).char == 'ว') or \
        (syllable.chars[current_index].char == 'ั' and syllable.chars[current_index].getAfter(0).char == 'ว') or \
        (syllable.chars[current_index].char == 'ั' and syllable.chars[current_index].getAfter(0).char in TONE_MARKS and syllable.chars[current_index].getAfter(1).char == 'ว'):
            w_vowel = True

    if w_vowel:
        w_index = None
        for potential_w_index in range(current_index, len(syllable.chars)):
            if syllable.chars[potential_w_index].char == 'ว':
                w_index = potential_w_index
        current_index = append_loop(current_index, w_index)
        return [current_index, final_vowels, tone_marks]
    
    if syllable.chars[current_index].char in TONE_MARKS and syllable.chars[current_index].getAfter(0).char in VOWELS:
        tone_marks.append(syllable.chars[current_index])
        final_vowels.append(syllable.chars[current_index].getAfter(0))
        current_index += 2
        return [current_index, final_vowels, tone_marks]
    
    if syllable.chars[current_index].char in VOWELS:
        final_vowels.append(syllable.chars[current_index])
        current_index += 1
        return [current_index, final_vowels, tone_marks]
    
    if syllable.chars[current_index].char in TONE_MARKS:
        tone_marks.append(syllable.chars[current_index])
        current_index += 1
        return [current_index, final_vowels, tone_marks]

    return [current_index, final_vowels, tone_marks]

def find_final_consonants_cluster(syllable, current_index):
    return syllable.chars[current_index:]

def extract_clusters(syllable):
    ee_initial = False
    ai_initial = False

    initial_vowels_cluster_info = find_initial_vowels_cluster(syllable)
    current_index = initial_vowels_cluster_info[0]
    initial_vowels_cluster = initial_vowels_cluster_info[1]

    if initial_vowels_cluster:
        if initial_vowels_cluster[0] == 'เ':
            ee_initial == True
        if initial_vowels_cluster[0] == 'ไ':
            ai_initial == True
    
    initial_consonants_cluster_info = find_initial_consonants_cluster(syllable, current_index, ee_initial)
    current_index = initial_consonants_cluster_info[0]
    initial_consonants_cluster = initial_consonants_cluster_info[1]
    w_vowel = initial_consonants_cluster_info[2]

    final_vowels_and_tone_marks_clusters_info = find_final_vowels_and_tone_marks_clusters(syllable, current_index, ee_initial, ai_initial, w_vowel)
    current_index = final_vowels_and_tone_marks_clusters_info[0]
    final_vowels_cluster = final_vowels_and_tone_marks_clusters_info[1]
    tone_marks_cluster = final_vowels_and_tone_marks_clusters_info[2]

    final_consonants_cluster = find_final_consonants_cluster(syllable, current_index)

    for char in initial_vowels_cluster:
        char.cluster = 'initial_vowels_cluster'
    for char in initial_consonants_cluster:
        char.cluster = 'initial_consonants_cluster'
    for char in tone_marks_cluster:
        char.cluster = 'tone_marks_cluster'
    for char in final_vowels_cluster:
        char.cluster = 'final_vowels_cluster'
    for char in final_consonants_cluster:
        char.cluster = 'final_consonants_cluster'


    return [initial_vowels_cluster, initial_consonants_cluster, tone_marks_cluster, final_vowels_cluster, final_consonants_cluster]

syl = SyllableCharacters('ก่อ')
print(f'Syllable Length: {len(syl.chars)}')
extract_clusters(syl)
print(0, syl.chars[1].cluster)