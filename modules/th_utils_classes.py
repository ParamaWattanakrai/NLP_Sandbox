from th_utils_dict import *

class ThaiCharacter():
    def __init__(self, char, syllable=None, position=None, before=[], after=[], cluster='unknown', char_role='unknown'):
        self.char = char
        self.syllable = syllable
        self.position = position
        self.before = before
        self.after = after
        self.cluster = cluster
        self.role = char_role
        
        self.assignClass()
    def getInformation(self):
        chars_before = []
        chars_after = []
        for char in self.before:
            chars_before.append(char.char)
        for char in self.after:
            chars_after.append(char.char)
        return f'''
            Character: {self.char}
            In Syllable: {self.syllable.string}
            Position: {self.position}
            Class: {self.consonant_class}
            In Cluster: {self.cluster}
            Role: {self.role}\nChracters Before: {chars_before}\nCharacters After: {chars_after}
            '''
    def getChar(self):
        return self.char
    def getPosition(self):
        return self.position
    def getSyllable(self):
        return self.syllable
    def getClass(self):
        if not self.consonant_class:
            return None
    
    def getBefore(self, distance):
        distance += 1
        if len(self.before) < distance:
            return None
        return self.before[-distance]
    def getAfter(self, distance):
        if len(self.after) <= distance:
            return None
        return self.after[distance]
    def getBeforeChar(self, distance):
        if not self.getBefore(distance):
            return None
        return self.getBefore(distance).getChar()
    def getAfterChar(self, distance):
        if not self.getAfter(distance):
            return None
        return self.getAfter[distance].getChar()
    
    def selfCluster(self, cluster):
        return self.syllable.assignCluster(self, cluster)
    def selfRole(self, role):
        return self.syllable.assignRole(self, role)

    def assignClass(self):
        for consonant_class_key in CONSONANT_CLASSES.keys():
            if self.char in CONSONANT_CLASSES[consonant_class_key]:
                self.consonant_class = consonant_class_key

class ThaiSyllable:
    def __init__(self, syllable_string):
        self.syllable_string = syllable_string
        self.thchars = []
        
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

        self.true_blend = False

        self.initial_sound = ''
        self.initial_class = ''
        self.final_sound = ''

        self.vowel_default = ''
        self.vowel_duration = ''
        self.vowel_short = ''
        self.vowel_long = ''
        
        self.live_dead = ''

        self.tone_mark = ''
        self.tone = ''

        self.appendThChars()
        self.appendBeforeAfter()
        
    def appendThChars(self):
        for index, thchar in enumerate(self.thchars):
            thisthchar = ThaiCharacter(thchar, self, index)
            self.thchars.append(thisthchar)
    def appendBeforeAfter(self):
        for index, thchar in enumerate(self.thchars):
            thchar.before = self.thchars[:index]
            thchar.after = self.thchars[index+1:]

    def getInformation(self):
        initial_vowels = []
        initial_consonants = []
        tone_marks = []
        final_vowels = []
        final_consonants = []
        initial_vowels_roles = []

        vowels = []

        for char in self.initial_vowels_cluster:
            initial_vowels.append([char.char, char.role])
        for char in self.initial_consonants_cluster:
            initial_consonants.append([char.char, char.role])
        for char in self.tone_marks_cluster:
            tone_marks.append([char.char, char.role])
        for char in self.final_vowels_cluster:
            final_vowels.append([char.char, char.role])
        for char in self.final_consonants_cluster:
            final_consonants.append([char.char, char.role])

        for char in self.getVowel():
            vowels.append(char.char)

        information = f'''
            Syllable String: {self.string}
            Initial Vowels Cluster: {initial_vowels}
            Initial Consonants Cluster: {initial_consonants}
            Tone Marks Cluster: {tone_marks}
            Final Vowels Cluster: {final_vowels}
            Final Consonants Cluster: {final_consonants}

            Initial Sound: {self.initial_sound}
            Inital Class: {self.initial_class}
            Final Sound: {self.final_sound}
            
            Vowel Form: {vowels}
            Vowel Default Form: {self.vowel_default}
            Vowel Duration: {self.vowel_duration}

            Vowel Short Form: {self.vowel_short}
            Vowel Long Form: {self.vowel_long}

            Live/Dead: {self.live_dead}

            Tone Mark: {self.tone_mark}
            Tone: {self.tone}
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

    # Get Clusters

    def getInitialVowelsClusterList(self):
        if not self.initial_vowels_cluster:
            return None
        return self.initial_vowels_cluster
    def getInitialVowelsClusterString(self):
        if self.getInitialVowelsClusterString():
            return None
        string = ''
        for thchar in self.getInitialVowelsClusterString():
            string = string + thchar.getChar()
        return string
    def getInitialConsonantsClusterList(self):
        if not self.initial_consonants_cluster:
            return None
        return self.initial_consonants_cluster
    def getInitialConsonantsClusterString(self):
        if not self.getInitialConsonantsClusterList():
            return None
        string = ''
        for thchar in self.getInitialConsonantsClusterList():
            string = string + thchar.getChar()
        return string
    def getToneMarksClusterList(self):
        if not self.tone_marks_cluster:
            return None
        return self.tone_marks_cluster
    def getToneMarksClusterString(self):
        if not self.getToneMarksClusterList():
            return None
        string = ''
        for thchar in self.getToneMarksClusterList():
            string = string + thchar.getChar()
        return string
    def getFinalVowelsClusterList(self):
        if not self.final_vowels_cluster:
            return None
        return self.final_vowels_cluster
    def getFinalVowelsClusterString(self):
        if not self.getFinalVowelsClusterList():
            return None
        string = ''
        for thchar in self.getFinalVowelsClusterList():
            string = string + thchar.getChar()
        return string
    def getFinalConsonantsClusterList(self):
        if not self.final_consonants_cluster:
            return None
        return self.final_consonants_cluster
    def getFinalConsonantsClusterString(self):
        if not self.getFinalConsonantsClusterList():
            return None
        string = ''
        for thchar in self.getFinalConsonantsClusterList():
            string = string + thchar.getChar()
        return string
    
    
    def getVowelList(self):
        if not self.initial_vowels_cluster and not self.final_vowels_cluster:
            return None
        return self.initial_vowels_cluster + self.final_vowels_cluster
    def getVowelString(self):
        if not self.getVowel():
            return None
        string = ''
        for thchar in self.getVowel():
            string = string + thchar.getChar()
        return string

a = ThaiSyllable('การ')
print(a.getInitialConsonantsClusterString())