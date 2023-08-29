import re

from th_utils_classes import *
from th_utils_regex import *

pattern = f'เ[{C}]([{C}]|)ี([{T}]|)ยะ'

syllable = ThaiSyllable("เยีย")
syllable_string = syllable.syllable_string
print(syllable_string)
print(syllable.thchars)

#Final Con Shenanigans not supported เลย์
def process_cluster(syllable, init_vowel_char='', vert_vowel_char='', fin_vowel_chars='', has_tone=True):
    init_vowel_index = -1
    vert_vowel_index = len(syllable.thchars) + 1
    fin_vowel_indexes = [len(syllable.thchars) + 1]
    for thchar in syllable.thchars:
        if init_vowel_char:
            if thchar.char == init_vowel_char:
                thchar.selfCluster('initial_vowels_cluster')
                init_vowel_index = thchar.getPosition()
        if vert_vowel_char:
            if thchar.char == vert_vowel_char:
                thchar.selfCluster('final_vowels_cluster')
                vert_vowel_index = thchar.getPosition()
        if fin_vowel_chars:
            if len(fin_vowel_chars) == 2:
                if thchar.char == fin_vowel_chars[0] and thchar.getAfterChar(0) == fin_vowel_chars[1]:
                    thchar.selfCluster('final_vowels_cluster')
                    thchar.getAfter(0).selfCluster('final_vowels_cluster')
                    fin_vowel_indexes[0] = thchar.getPosition()
                    fin_vowel_indexes.append(thchar.getAfter(0).getPosition())
            elif thchar.char == fin_vowel_chars[0]:
                thchar.selfCluster('final_vowels_cluster')
                fin_vowel_indexes[0] = thchar.getPosition()
    
    for i, thchar in enumerate(syllable.thchars):
        if i > init_vowel_index and i < vert_vowel_index and i < fin_vowel_indexes[0]:
            if has_tone and thchar.char in TONE_MARKS:
                thchar.selfCluster('tone_marks_cluster')
                continue
            thchar.selfCluster('initial_consonants_cluster')
            continue
        if i > vert_vowel_index and i < fin_vowel_indexes[0]:
            if has_tone and thchar.char in TONE_MARKS:
                thchar.selfCluster('tone_marks_cluster')
                continue
            thchar.selfCluster('final_consonants_cluster')
            continue
        if i > fin_vowel_indexes[-1]:
            thchar.selfCluster('final_consonants_cluster')

if re.search(f'[{C}]ึ', syllable_string):
    syllable.vowel_default = '-ึ'
    process_cluster(syllable, vert_vowel_char='ึ')
    print(syllable.vowel_default)
elif re.search(f'[{C}]ุ', syllable_string):
    process_cluster(syllable, vert_vowel_char='ุ')
    print(syllable_string)
elif re.search(f'[{C}]ู', syllable_string):
    process_cluster(syllable, vert_vowel_char='ู')
    print(syllable_string)
elif re.search(f'[{C}]รร', syllable_string):
    process_cluster(syllable, fin_vowel_chars='รร', has_tone=False)
    print(syllable_string)
elif re.search(f'[{C}]([{T}]|)ำ', syllable_string):
    process_cluster(syllable, fin_vowel_chars='ำ')
    print(syllable_string)
elif re.search(f'[{C}]ฤ', syllable_string):
    process_cluster(syllable, fin_vowel_chars='ฤ', has_tone=False)
    print(syllable_string)

elif re.search(f'แ[{C}]([{C}]|)็[{C}]', syllable_string):
    process_cluster(syllable, fin_vowel_chars='็', has_tone=False)
    print(syllable_string)
elif re.search(f'แ[{C}]([{C}]|)([{T}]|)ะ', syllable_string):
    process_cluster(syllable, init_vowel_char='แ', fin_vowel_chars='ะ')
    print(syllable_string)
elif re.search(f'แ[{C}]', syllable_string):
    process_cluster(syllable, init_vowel_char='แ')
    print(syllable_string)

elif re.search(f'เ[{C}]([{C}]|)ี([{T}]|)ยะ', syllable_string):
    process_cluster(syllable, init_vowel_char='เ', vert_vowel_char='ี', fin_vowel_chars='ยะ')
    print(syllable_string)
elif re.search(f'เ[{C}]([{C}]|)ื([{T}]|)อะ', syllable_string):
    process_cluster(syllable, init_vowel_char='เ', vert_vowel_char='ื', fin_vowel_chars='อะ')
    print(syllable_string)
elif re.search(f'เ[{C}]([{C}]|)([{T}]|)อะ', syllable_string):
    process_cluster(syllable, init_vowel_char='เ', fin_vowel_chars='อะ')
    print(syllable_string)
elif re.search(f'เ[{C}]([{C}]|)([{T}]|)าะ', syllable_string):
    process_cluster(syllable, init_vowel_char='เ', fin_vowel_chars='าะ')
    print(syllable_string)
elif re.search(f'เ[{C}]([{C}]|)([{T}]|)ะ', syllable_string):
    process_cluster(syllable, init_vowel_char='เ', fin_vowel_chars='ะ')
    print(syllable_string)
elif re.search(f'เ[{C}]([{C}]|)ี([{T}]|)ย', syllable_string):
    process_cluster(syllable, init_vowel_char='เ', vert_vowel_char='ี', fin_vowel_chars='ย')
    print(syllable_string)
elif re.search(f'เ[{C}]([{C}]|)ื([{T}]|)อ', syllable_string):
    process_cluster(syllable, init_vowel_char='เ', vert_vowel_char='ื', fin_vowel_chars='อ')
    print(syllable_string)
elif re.search(f'เ[{C}]([{C}]|)([{T}]|)อ', syllable_string):
    process_cluster(syllable, init_vowel_char='เ', fin_vowel_chars='อ')
    print(syllable_string)
elif re.search(f'เ[{C}]([{C}]|)([{T}]|)า', syllable_string):
    process_cluster(syllable, init_vowel_char='เ', fin_vowel_chars='า')
    print(syllable_string)
elif re.search(f'เ[{C}]([{C}]|)ิ([{T}]|)[{C}]', syllable_string):
    process_cluster(syllable, init_vowel_char='เ', vert_vowel_char='ิ')
    print(syllable_string)
elif re.search(f'เ[{C}]', syllable_string):
    process_cluster(syllable, init_vowel_char='เ', vert_vowel_char='ีิ')
    print(syllable_string)
elif re.search(f'[{C}]([{T}]|)า', syllable_string):
    process_cluster(syllable, fin_vowel_chars='า')
    process_cluster_one_final(syllable, 'า')
    print(syllable_string)
elif re.search(f'[{C}]ิ', syllable_string):
    process_cluster(syllable, vert_vowel_char='ิ')
    print(syllable_string)
elif re.search(f'[{C}]ี', syllable_string):
    process_cluster(syllable, vert_vowel_char='ี')
    print(syllable_string)

elif re.search(f'[{C}]([{C}]|)ื([{T}]|)อ', syllable_string):
    process_cluster(syllable, vert_vowel_char='ื', fin_vowel_chars='อ')
    print(syllable_string)
elif re.search(f'[{C}]ื([{T}]|)[{C}]', syllable_string):
    process_cluster(syllable, vert_vowel_char='ื')
    print(syllable_string)

elif re.search(f'โ[{C}]([{C}]|)([{T}]|)ะ', syllable_string):
    process_cluster(syllable, init_vowel_char='โ', fin_vowel_chars='ะ')
    print(syllable_string)
elif re.search(f'โ[{C}]', syllable_string):
    process_cluster(syllable, init_vowel_char='โ')
    print(syllable_string)

elif re.search(f'ไ[{C}]ย', syllable_string):
    process_cluster(syllable, init_vowel_char='ไ', fin_vowel_chars='ย')
    print(syllable_string)
elif re.search(f'ไ[{C}]', syllable_string):
    process_cluster(syllable, init_vowel_char='ไ')
    print(syllable_string)
elif re.search(f'ใ[{C}]', syllable_string):
    process_cluster(syllable, init_vowel_char='ใ')
    print(syllable_string)

elif re.search(f'[{C}]ั([{T}]|)วะ', syllable_string):
    process_cluster(syllable, vert_vowel_char='ั', fin_vowel_chars='วะ')
    print(syllable_string)
elif re.search(f'[{C}]ั([{T}]|)ว', syllable_string):
    process_cluster(syllable, vert_vowel_char='ั', fin_vowel_chars='ว')
    print(syllable_string)
elif re.search(f'[{C}]ั([{T}]|)[{C}]', syllable_string):
    process_cluster(syllable, vert_vowel_char='ั')
    process_cluster_one_final(syllable, 'ั')
    print(syllable_string)
elif re.search(f'[{C}]([{T}]|)ะ', syllable_string):
    process_cluster(syllable, fin_vowel_chars='ะ')
    process_cluster_one_final(syllable, 'ะ')
    print(syllable_string)

elif re.search(f'[{C}]็อ[{C}]', syllable_string):
    process_cluster(syllable, vert_vowel_char='็', fin_vowel_chars='อ', has_tone=False)
    print(syllable_string)
elif re.search(f'[{C}]([{T}]|)อ', syllable_string):
    process_cluster(syllable, fin_vowel_chars='อ')
    print(syllable_string)

elif re.search(f'[{C}]([{T}]|)ว[{C}]', syllable_string):
    process_cluster(syllable, fin_vowel_chars='ว')
    process_cluster_one_final(syllable, 'ว')
    print(syllable_string)

elif re.search(f'[{C}][{C}]', syllable_string):
    print(syllable_string)

for thchar in syllable.thchars:
    print(thchar.cluster)