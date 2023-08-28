import re

from th_utils_classes import *
from th_utils_regex import *

pattern = f'เ[{C}]([{C}]|)ี([{T}]|)ยะ'

syllable = ThaiSyllable("มึ่น")
syllable_string = syllable.syllable_string
print(syllable_string)
print(syllable.thchars)

def process_cluster_one_final(syllable, vowelchar): #Should support 2 chars
    for thchar in syllable.thchars:
        if thchar.char == vowelchar:
            thchar.selfCluster('final_vowels_cluster')
            vowel_index = thchar.getPosition()
    if not vowel_index:
        return None
    for i in range(0, vowel_index):
        if syllable.thchars[i].char in TONE_MARKS:
            syllable.thchars[i].selfCluster('tone_marks_cluster')
            return
        syllable.thchars[i].selfCluster('initial_consonants_cluster')
    for i in range(vowel_index+1, len(syllable.thchars)):
        if syllable.thchars[i].char in TONE_MARKS:
            syllable.thchars[i].selfCluster('tone_marks_cluster')
            return
        syllable.thchars[i].selfCluster('final_consonants_cluster')

def process_cluster(syllable, init_vowel_char='', floating_vowel_char='', fin_vowel_chars=[]):
    init_vowel_index = -1
    floating_vowel_index = len(syllable.thchars) + 1
    fin_vowel_indexes = [len(syllable.thchars) + 1] 
    for thchar in syllable.thchars:
        if init_vowel_char:
            if thchar.char == init_vowel_char:
                thchar.selfCluster('initial_vowels_cluster')
                init_vowel_index = thchar.getPosition()
        if floating_vowel_char:
            if thchar.char == floating_vowel_char:
                thchar.selfCluster('final_vowels_cluster')
                floating_vowel_index = thchar.getPosition()
        if fin_vowel_chars:
            if len(fin_vowel_chars) == 2:
                if thchar.char == fin_vowel_chars[0] and thchar.getAfterChar(0) == fin_vowel_chars[1]:
                    thchar.selfCluster('final_vowels_cluster')
                    thchar.getAfter(0).selfCluster('final_vowels_cluster')
                    fin_vowel_indexes[0] = thchar.getPosition()
                    fin_vowel_indexes[1] = thchar.getAfter(0).getPosition()
            elif thchar.char == fin_vowel_chars[0]:
                thchar.selfCluster('final_vowels_cluster')
                fin_vowel_indexes[0] = thchar.getPosition()
    
    for i, thchar in enumerate(syllable.thchars):
        if i > init_vowel_index and i < floating_vowel_index and i < fin_vowel_indexes[0]:
            if thchar.char in TONE_MARKS:
                thchar.selfCluster('tone_marks_cluster')
                continue
            thchar.selfCluster('initial_consonants_cluster')
            continue
        if i > floating_vowel_index and i < fin_vowel_indexes[0]:
            if thchar.char in TONE_MARKS:
                thchar.selfCluster('tone_marks_cluster')
                continue
            thchar.selfCluster('initial_consonants_cluster')
            continue
        if i > fin_vowel_indexes[-1]:
            thchar.selfCluster('final_consonants_cluster')

if re.search(f'[{C}]ึ', syllable_string):
    syllable.vowel_default = '-ึ'
    process_cluster(syllable, floating_vowel_char='ึ')
    print(syllable.vowel_default)
elif re.search(f'[{C}]ุ', syllable_string):
    process_cluster_one_final(syllable, 'ุ')
    print(syllable_string)
elif re.search(f'[{C}]ู', syllable_string):
    process_cluster_one_final(syllable, 'ู')
    print(syllable_string)
elif re.search(f'[{C}]รร', syllable_string):
    print(syllable_string)
elif re.search(f'[{C}]([{T}]|)ำ', syllable_string):
    process_cluster_one_final(syllable, 'ำ')
    print(syllable_string)
elif re.search(f'[{C}]ฤ', syllable_string):
    process_cluster_one_final(syllable, 'ฤ')
    print(syllable_string)

elif re.search(f'แ[{C}]([{C}]|)็([{T}]|)[{C}]', syllable_string):
    print(syllable_string)
elif re.search(f'แ[{C}]([{C}]|)([{T}]|)ะ', syllable_string):
    print(syllable_string)
elif re.search(f'แ[{C}]', syllable_string):
    print(syllable_string)

elif re.search(f'เ[{C}]([{C}]|)ี([{T}]|)ยะ', syllable_string):
    print(syllable_string)
elif re.search(f'เ[{C}]([{C}]|)ี([{T}]|)ยะ', syllable_string):
    print(syllable_string)
elif re.search(f'เ[{C}]([{C}]|)ื([{T}]|)อะ', syllable_string):
    print(syllable_string)
elif re.search(f'เ[{C}]([{C}]|)([{T}]|)อะ', syllable_string):
    print(syllable_string)
elif re.search(f'เ[{C}]([{C}]|)([{T}]|)าะ', syllable_string):
    print(syllable_string)
elif re.search(f'เ[{C}]([{C}]|)([{T}]|)ะ', syllable_string):
    print(syllable_string)
elif re.search(f'เ[{C}]([{C}]|)ื([{T}]|)อ', syllable_string):
    print(syllable_string)
elif re.search(f'เ[{C}]([{C}]|)([{T}]|)อ', syllable_string):
    print(syllable_string)
elif re.search(f'เ[{C}]([{C}]|)ิ([{T}]|)[{C}]', syllable_string):
    print(syllable_string)
elif re.search(f'เ[{C}]', syllable_string):
    print(syllable_string)
elif re.search(f'[{C}]([{T}]|)า', syllable_string):
    process_cluster_one_final(syllable, 'า')
    print(syllable_string)
elif re.search(f'[{C}]ิ', syllable_string):
    process_cluster_one_final(syllable, 'ิ')
    print(syllable_string)
elif re.search(f'[{C}]ี', syllable_string):
    process_cluster_one_final(syllable, 'ี')
    print(syllable_string)

elif re.search(f'[{C}]([{C}]|)ื([{T}]|)อ', syllable_string):
    print(syllable_string)
elif re.search(f'[{C}]ื([{T}]|)[{C}]', syllable_string):
    print(syllable_string)

elif re.search(f'โ[{C}]([{C}]|)([{T}]|)ะ', syllable_string):
    print(syllable_string)
elif re.search(f'โ[{C}]', syllable_string):
    print(syllable_string)

elif re.search(f'ไ[{C}]ย', syllable_string):
    print(syllable_string)
elif re.search(f'ไ[{C}]', syllable_string):
    print(syllable_string)
elif re.search(f'ใ[{C}]', syllable_string):
    print(syllable_string)

elif re.search(f'[{C}]ั([{T}]|)วะ', syllable_string):
    print(syllable_string)
elif re.search(f'[{C}]ั([{T}]|)ว', syllable_string):
    print(syllable_string)
elif re.search(f'[{C}]ั([{T}]|)[{C}]', syllable_string):
    process_cluster_one_final(syllable, 'ั')
    print(syllable_string)
elif re.search(f'[{C}]([{T}]|)ะ', syllable_string):
    process_cluster_one_final(syllable, 'ะ')
    print(syllable_string)

elif re.search(f'[{C}]็อ[{C}]', syllable_string):
    print(syllable_string)
elif re.search(f'[{C}]([{T}]|)อ', syllable_string):
    process_cluster_one_final(syllable, 'อ')
    print(syllable_string)

elif re.search(f'[{C}]([{T}]|)ว[{C}]', syllable_string):
    process_cluster_one_final(syllable, 'ว')
    print(syllable_string)

elif re.search(f'[{C}][{C}]', syllable_string):
    print(syllable_string)

for thchar in syllable.thchars:
    print(thchar.cluster)