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

BLENDING_CONSONANTS = th_all.blending_consonants
BLEND_LEADS = th_all.blend_initials

INITIAL_VOWELS = th_all.initial_vowels

K_FINAL_SOUND = th_all.k_final_sound
P_FINAL_SOUND = th_all.p_final_sound
T_FINAL_SOUND = th_all.t_final_sound
N_FINAL_SOUND = th_all.n_final_sound
M_FINAL_SOUND = th_all.m_final_sound
Y_FINAL_SOUND = th_all.y_final_sound
W_FINAL_SOUND = th_all.w_final_sound
NG_FINAL_SOUND = th_all.ng_final_sound

class Character():
    def __init__(self, char, position, syllable, before=[], after=[], cluster='unknown', char_role='unknown'):
        self.char = char
        self.position = position
        self.syllable = syllable
        self.before = before
        self.after = after
        self.cluster = cluster
        self.role = char_role
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
        if len(self.after) <= distance:
            return None
        return self.after[distance]
    def selfCluster(self, cluster):
        return self.syllable.assignCluster(self, cluster)
    def selfRole(self, role):
        return self.syllable.assignRole(self, role)

class Syllable:
    def __init__(self, string):
        self.string = string
        self.chars = []
        
        self.initial_vowels_cluster = []
        self.initial_consonants_cluster = []
        self.tone_marks_cluster = []
        self.final_vowels_cluster = []
        self.final_consonants_cluster = []

        self.leading_consonants = []
        self.initial_consonants = []
        self.blending_consonants = []
        self.vowels = []
        self.tone_marks = []
        self.final_consonants = []
        self.silent_characters = []

        self.final_sound = ''

        for index, char in enumerate(string):
            thischar = Character(char, index, self)
            self.chars.append(thischar)
        for index, char in enumerate(self.chars):
            char.before = self.chars[:index]
            char.after = self.chars[index+1:]
    def getInformation(self):
        initial_vowels = []
        initial_consonants = []
        tone_marks = []
        final_vowels = []
        final_consonants = []
        initial_vowels_roles = []
        for initial_vowel in self.initial_vowels_cluster:
            initial_vowels.append([initial_vowel.char, initial_vowel.role])
        for initial_consonant in self.initial_consonants_cluster:
            initial_consonants.append([initial_consonant.char, initial_consonant.role])
        for tone_mark in self.tone_marks_cluster:
            tone_marks.append([tone_mark.char, tone_mark.role])
        for final_vowel in self.final_vowels_cluster:
            final_vowels.append([final_vowel.char, final_vowel.role])
        for final_consonant in self.final_consonants_cluster:
            final_consonants.append([final_consonant.char, final_consonant.role])
        information = f'''\
            Syllable String: {self.string}
            Initial Vowels Cluster: {initial_vowels}
            Initial Consonants Cluster: {initial_consonants}
            Tone Marks Cluster: {tone_marks}
            Final Vowels Cluster: {final_vowels}
            Final Consonants Cluster: {final_consonants}
            '''
        return information
    def assignCluster(self, char, cluster):
        if cluster == 'initial_vowels_cluster':
            char.cluster = cluster
            self.initial_vowels_cluster.append(char)
        elif cluster == 'initial_consonants_cluster':
            char.cluster = cluster
            self.initial_consonants_cluster.append(char)
        elif cluster == 'tone_marks_cluster':
            char.cluster = cluster
            self.tone_marks_cluster.append(char)
        elif cluster == 'final_vowels_cluster':
            char.cluster = cluster
            self.final_vowels_cluster.append(char)
        elif cluster == 'final_consonants_cluster':
            char.cluster = cluster
            self.final_consonants_cluster.append(char)
        else:
            return None
    def assignRole(self, char, role):
        if role == 'leading_consonant':
            char.role = role
            self.leading_consonants.append(char)
        elif role == 'initial_consonant':
            char.role = role
            self.initial_consonants.append(char)    
        elif role == 'blending_consonant':
            char.role = role
            self.blending_consonants.append(char)
        elif role == 'vowel':
            char.role = role
            self.vowels.append(char)
        elif role == 'tone_mark':
            char.role = role
            self.tone_marks.append(char)
        elif role == 'final_consonant':
            char.role = role
            self.final_consonants.append(char)
        elif role == 'silent_character':
            char.role = role
            self.silent_characters.append(char)
        else:
            return None
    def getVowel(self):
        return self.initial_vowels_cluster + self.final_vowels_cluster

def find_initial_vowels_cluster(syllable):
    initial_vowels = []
    current_index = 0
    if syllable.chars[0].char in INITIAL_VOWELS:
        initial_vowels = [syllable.chars[0]]
        current_index += 1

    return [current_index, initial_vowels]

def find_initial_consonants_cluster(syllable, current_index, ee_initial, ai_initial):
    w_vowel = False

    first_consonant = syllable.chars[current_index]

    initial_consonants = [first_consonant]
    current_index += 1

    if first_consonant.getAfter(0):
        potential_second_consonant = first_consonant.getAfter(0)
        if potential_second_consonant.char in CONSONANTS:

            if potential_second_consonant.char == 'อ':
                return [current_index, initial_consonants, w_vowel]
            
            if potential_second_consonant.char == 'ย' and (ee_initial or ai_initial):
                return [current_index, initial_consonants, w_vowel]

            if potential_second_consonant.char == 'ว':
                for chars in syllable.chars:
                    if chars.char in VOWELS:
                        initial_consonants.append(potential_second_consonant)
                        current_index += 1
                        return [current_index, initial_consonants, w_vowel]
                w_vowel = True
                return [current_index, initial_consonants, w_vowel]
            
            if potential_second_consonant.getAfter(0):
                if potential_second_consonant.char == 'ร' and potential_second_consonant.getAfter(0).char == 'ร':
                    return [current_index, initial_consonants, w_vowel]
                initial_consonants.append(potential_second_consonant)
                current_index += 1
                return [current_index, initial_consonants, w_vowel]
            
            initial_consonants.append(potential_second_consonant)
            current_index += 1
            return [current_index, initial_consonants, w_vowel]

    return [current_index, initial_consonants, w_vowel]

def find_final_vowels_and_tone_marks_clusters(syllable, current_index, ee_initial, ai_initial, w_vowel):
    final_vowels = []
    tone_marks = []

    if len(syllable.chars) <= current_index:
        return [current_index, final_vowels, tone_marks]

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
                if y.getAfter(0):
                    if y.getAfter(0).char == '์':
                        break
                current_index = append_loop(current_index, potential_y_index)
                return [current_index, final_vowels, tone_marks]

    after0_char = ''
    if current_index + 1 < len(syllable.chars):
        after0_char = syllable.chars[current_index].getAfter(0).char

    after1_char = ''
    if current_index + 2 < len(syllable.chars):
        after1_char = syllable.chars[current_index].getAfter(1).char

    if syllable.chars[current_index].char == 'ร' and after0_char == 'ร':
        final_vowels.append(syllable.chars[current_index])
        final_vowels.append(syllable.chars[current_index].getAfter(0))
        current_index += 2
        return [current_index, final_vowels, tone_marks]

    if (syllable.chars[current_index].char in TONE_MARKS and after0_char == 'ว') or \
        (syllable.chars[current_index].char == 'ั' and after0_char == 'ว') or \
        (syllable.chars[current_index].char == 'ั' and after0_char in TONE_MARKS and after1_char == 'ว'):
            w_vowel = True

    if w_vowel:
        w_index = None
        for potential_w_index in range(current_index, len(syllable.chars)):
            if syllable.chars[potential_w_index].char == 'ว':
                w_index = potential_w_index
        current_index = append_loop(current_index, w_index)
        return [current_index, final_vowels, tone_marks]
    
    if syllable.chars[current_index].char in TONE_MARKS and after0_char in VOWELS:
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
        if initial_vowels_cluster[0].char == 'เ':
            ee_initial = True
        if initial_vowels_cluster[0].char == 'ไ':
            ai_initial = True

    initial_consonants_cluster_info = find_initial_consonants_cluster(syllable, current_index, ee_initial, ai_initial)
    current_index = initial_consonants_cluster_info[0]
    initial_consonants_cluster = initial_consonants_cluster_info[1]
    w_vowel = initial_consonants_cluster_info[2]

    final_vowels_and_tone_marks_clusters_info = find_final_vowels_and_tone_marks_clusters(syllable, current_index, ee_initial, ai_initial, w_vowel)
    current_index = final_vowels_and_tone_marks_clusters_info[0]
    final_vowels_cluster = final_vowels_and_tone_marks_clusters_info[1]
    tone_marks_cluster = final_vowels_and_tone_marks_clusters_info[2]

    final_consonants_cluster = find_final_consonants_cluster(syllable, current_index)

    for char in initial_vowels_cluster:
        char.selfCluster('initial_vowels_cluster')
    for char in initial_consonants_cluster:
        char.selfCluster('initial_consonants_cluster')
    for char in tone_marks_cluster:
        char.selfCluster('tone_marks_cluster')
    for char in final_vowels_cluster:
        char.selfCluster('final_vowels_cluster')
    for char in final_consonants_cluster:
        char.selfCluster('final_consonants_cluster')

def extract_initial_consonants_cluster(syllable):
    initial_consonants_cluster = syllable.initial_consonants_cluster

    if len(initial_consonants_cluster) == 1:
        initial_consonants_cluster[0].selfRole('initial_consonant')
        return

    if (initial_consonants_cluster[0].char == 'ห' or initial_consonants_cluster[0].char == 'อ') and \
        initial_consonants_cluster[1].char in UNPAIRED_LOW_CONSONANTS:
        initial_consonants_cluster[0].selfRole('leading_consonant')
        initial_consonants_cluster[1].selfRole('initial_consonant')
        return
    
    initial_consonants_cluster[0].selfRole('initial_consonant')
    initial_consonants_cluster[1].selfRole('blending_consonant')

def extract_final_consonants_cluster(syllable):
    final_consonants_cluster = syllable.final_consonants_cluster

    if not final_consonants_cluster:
        return
    
    if final_consonants_cluster[-1].char == '์':
        final_consonants_cluster[-1].selfRole('silent_character')
        final_consonants_cluster[-2].selfRole('silent_character')
        return
    if len(final_consonants_cluster) == 2 and final_consonants_cluster[0].char == 'ร':
        final_consonants_cluster[0].selfRole('silent_character')
        final_consonants_cluster[1].selfRole('final_consonant')
        return
    
    final_consonants_cluster[0].selfRole('final_consonant')
    for char in final_consonants_cluster[1:]:
        char.selfRole('silent_character')

def extract_roles(syllable):
    for char in syllable.initial_vowels_cluster + syllable.final_vowels_cluster:
        char.selfRole('vowel')
    for char in syllable.tone_marks_cluster:
        char.selfRole('tone_mark')
    extract_initial_consonants_cluster(syllable)
    extract_final_consonants_cluster(syllable)
    return

def get_final_sound(syllable):
    if not syllable.final_consonants:
        return 'open'
    if syllable.final_consonants[0].char in K_FINAL_SOUND:
        return 'k'
    if syllable.final_consonants[0].char in P_FINAL_SOUND:
        return 'p'
    if syllable.final_consonants[0].char in T_FINAL_SOUND:
        return 't'
    if syllable.final_consonants[0].char in N_FINAL_SOUND:
        return 'n'
    if syllable.final_consonants[0].char in M_FINAL_SOUND:
        return 'm'
    if syllable.final_consonants[0].char in Y_FINAL_SOUND:
        return 'y'
    if syllable.final_consonants[0].char in W_FINAL_SOUND:
        return 'w'
    if syllable.final_consonants[0].char in NG_FINAL_SOUND:
        return 'ng'
    return 'open'

syllable = Syllable('มารถ')
print(f'Syllable Length: {len(syllable.chars)}')
extract_clusters(syllable)
extract_roles(syllable)
print(syllable.getInformation())
syllable.final_sound = get_final_sound(syllable)
print(syllable.final_sound)