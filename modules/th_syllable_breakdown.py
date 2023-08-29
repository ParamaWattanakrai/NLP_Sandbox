import re

from th_utils_classes import *
from th_utils_regex import *
from th_utils_tables import *

pattern = f'เ[{C}]([{C}]|)ี([{T}]|)ยะ'

syllable = ThaiSyllable("เกว")
syllable_string = syllable.syllable_string
print(syllable_string)

def check_true_blend(first_char, second_char):
    if second_char == 'ร' and first_char in R_BLENDING_INITIALS:
        return True
    if second_char == 'ล' and first_char in L_BLENDING_INITIALS:
        return True
    if second_char == 'ว' and first_char in W_BLENDING_INITIALS:
        return True
    return False

def process_cluster(syllable, init_vowel_char='', vert_vowel_char='', fin_vowel_chars='', has_tone=True):

    def cluster_final_consonants(start_index):
        if len(syllable.thchars) <= start_index:
            return
        for i in range(start_index, len(syllable.thchars)):
            if syllable.thchars[i].char in TONE_MARKS:
                thchar.selfCluster('tone_marks_cluster')
                continue
            syllable.thchars[i].selfCluster('final_consonants_cluster')

    print(init_vowel_char, vert_vowel_char, fin_vowel_chars)
    if init_vowel_char and not vert_vowel_char and not fin_vowel_chars:
        syllable.thchars[0].selfCluster('initial_vowels_cluster')
        if init_vowel_char == 'ไ' or init_vowel_char == 'ใ':
            if check_true_blend(syllable.thchars[1].char, syllable.thchars[1].getAfterChar(0)):
                syllable.thchars[1].selfCluster('initial_consonants_cluster')
                syllable.thchars[1].getAfter(0).selfCluster('initial_consonants_cluster')
                cluster_final_consonants(3)

        elif check_true_blend(syllable.thchars[1].char, syllable.thchars[1].getAfterChar(0)):
            if syllable.thchars[1].getAfterChar(1) in TONE_MARKS:
                syllable.thchars[1].selfCluster('initial_consonants_cluster')
                syllable.thchars[1].getAfter(0).selfCluster('initial_consonants_cluster')
                cluster_final_consonants(3)
            elif syllable.thchars[1].getAfterChar(1) and syllable.thchars[1].getAfterChar(2) != '์':
                syllable.thchars[1].selfCluster('initial_consonants_cluster')
                syllable.thchars[1].getAfter(0).selfCluster('initial_consonants_cluster')
                cluster_final_consonants(3)
            else:
                if check_ambiguous_blend(syllable.thchars[0].char, syllable.thchars[1].char, syllable.thchars[2].char):
                    syllable.thchars[1].selfCluster('initial_consonants_cluster')
                    syllable.thchars[1].getAfter(0).selfCluster('initial_consonants_cluster')
                    cluster_final_consonants(3)
                else:
                    syllable.thchars[1].selfCluster('initial_consonants_cluster')
                    cluster_final_consonants(2)
        if syllable.thchars[-1].char == '์':
            syllable.thchars[-1].selfCluster('final_consonants_cluster')
            syllable.thchars[-2].selfCluster('final_consonants_cluster')
            return
        return

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
        if i > vert_vowel_index and i < fin_vowel_indexes[0]:
            if has_tone and thchar.char in TONE_MARKS:
                thchar.selfCluster('tone_marks_cluster')
                continue
            thchar.selfCluster('final_consonants_cluster')
        if i > fin_vowel_indexes[-1]:
            thchar.selfCluster('final_consonants_cluster')

def process_roles(syllable):

    initial_vowels_cluster = syllable.getInitialVowelsClusterList()
    initial_consonants_cluster = syllable.getInitialConsonantsClusterList()
    final_vowels_cluster = syllable.getFinalVowelsClusterList()
    final_consonants_cluster = syllable.getFinalConsonantsClusterList()

    for thchar in initial_vowels_cluster + final_vowels_cluster:
        thchar.selfRole('vowel')
    
    if syllable.getToneMarksClusterList():
        for thchar in syllable.getToneMarksClusterList():
            thchar.selfRole('tone_mark')

    if (initial_consonants_cluster[0].char == 'ห' and initial_consonants_cluster[-1].char in UNPAIRED_LOW_CONSONANTS) or \
        (initial_consonants_cluster[0].char == 'อ' and initial_consonants_cluster[-1].char == 'ย'):
        initial_consonants_cluster[0].selfRole('leading_consonant')
        initial_consonants_cluster[0].getAfter(0).selfRole('initial_consonant')
    elif initial_consonants_cluster[-1] is not initial_consonants_cluster[0]:
        initial_consonants_cluster[0].selfRole('initial_consonant')
        initial_consonants_cluster[-1].selfRole('blending_consonant')
    elif initial_consonants_cluster[-1] is initial_consonants_cluster[0]:
        initial_consonants_cluster[0].selfRole('initial_consonant')
    
    if final_consonants_cluster:
        final_consonants_cluster[0].selfRole('final_consonant')
        if final_consonants_cluster[-1].char == '์':
            final_consonants_cluster[-1].selfRole('silent_character')
            final_consonants_cluster[-2].selfRole('silent_character')
    
if re.search(f'[{C}]ึ', syllable_string):
    syllable.vowel_default = '-ึ'
    process_cluster(syllable, vert_vowel_char='ึ')
elif re.search(f'[{C}]ุ', syllable_string):
    process_cluster(syllable, vert_vowel_char='ุ')
elif re.search(f'[{C}]ู', syllable_string):
    process_cluster(syllable, vert_vowel_char='ู')
elif re.search(f'[{C}]รร', syllable_string):
    process_cluster(syllable, fin_vowel_chars='รร', has_tone=False)
elif re.search(f'[{C}]([{T}]|)ำ', syllable_string):
    process_cluster(syllable, fin_vowel_chars='ำ')
elif re.search(f'[{C}]ฤ', syllable_string):
    process_cluster(syllable, fin_vowel_chars='ฤ', has_tone=False)

elif re.search(f'แ[{C}]([{C}]|)็[{C}]', syllable_string):
    process_cluster(syllable, fin_vowel_chars='็', has_tone=False)
elif re.search(f'แ[{C}]([{C}]|)([{T}]|)ะ', syllable_string):
    process_cluster(syllable, init_vowel_char='แ', fin_vowel_chars='ะ')
elif re.search(f'แ[{C}]', syllable_string):
    process_cluster(syllable, init_vowel_char='แ')

elif re.search(f'เ[{C}]([{C}]|)ี([{T}]|)ยะ', syllable_string):
    process_cluster(syllable, init_vowel_char='เ', vert_vowel_char='ี', fin_vowel_chars='ยะ')
elif re.search(f'เ[{C}]([{C}]|)ื([{T}]|)อะ', syllable_string):
    process_cluster(syllable, init_vowel_char='เ', vert_vowel_char='ื', fin_vowel_chars='อะ')
elif re.search(f'เ[{C}]([{C}]|)([{T}]|)อะ', syllable_string):
    process_cluster(syllable, init_vowel_char='เ', fin_vowel_chars='อะ')
elif re.search(f'เ[{C}]([{C}]|)([{T}]|)าะ', syllable_string):
    process_cluster(syllable, init_vowel_char='เ', fin_vowel_chars='าะ')
elif re.search(f'เ[{C}]([{C}]|)([{T}]|)ะ', syllable_string):
    process_cluster(syllable, init_vowel_char='เ', fin_vowel_chars='ะ')
elif re.search(f'เ[{C}]([{C}]|)ี([{T}]|)ย([^์]|)', syllable_string):
    process_cluster(syllable, init_vowel_char='เ', vert_vowel_char='ี', fin_vowel_chars='ย')
elif re.search(f'เ[{C}]([{C}]|)ื([{T}]|)อ([^์]|)', syllable_string):
    process_cluster(syllable, init_vowel_char='เ', vert_vowel_char='ื', fin_vowel_chars='อ')
elif re.search(f'เ[{C}]([{C}]|)([{T}]|)อ([^์]|)', syllable_string):
    process_cluster(syllable, init_vowel_char='เ', fin_vowel_chars='อ')
elif re.search(f'เ[{C}]([{C}]|)([{T}]|)า', syllable_string):
    process_cluster(syllable, init_vowel_char='เ', fin_vowel_chars='า')
elif re.search(f'เ[{C}]([{C}]|)ิ([{T}]|)[{C}]', syllable_string):
    process_cluster(syllable, init_vowel_char='เ', vert_vowel_char='ิ')
elif re.search(f'เ[{C}]', syllable_string):
    process_cluster(syllable, init_vowel_char='เ')
elif re.search(f'[{C}]([{T}]|)า', syllable_string):
    process_cluster(syllable, fin_vowel_chars='า')
    process_cluster_one_final(syllable, 'า')
elif re.search(f'[{C}]ิ', syllable_string):
    process_cluster(syllable, vert_vowel_char='ิ')
elif re.search(f'[{C}]ี', syllable_string):
    process_cluster(syllable, vert_vowel_char='ี')

elif re.search(f'[{C}]([{C}]|)ื([{T}]|)อ', syllable_string):
    process_cluster(syllable, vert_vowel_char='ื', fin_vowel_chars='อ')
elif re.search(f'[{C}]ื([{T}]|)[{C}]', syllable_string):
    process_cluster(syllable, vert_vowel_char='ื')

elif re.search(f'โ[{C}]([{C}]|)([{T}]|)ะ', syllable_string):
    process_cluster(syllable, init_vowel_char='โ', fin_vowel_chars='ะ')
elif re.search(f'โ[{C}]', syllable_string):
    process_cluster(syllable, init_vowel_char='โ')

elif re.search(f'ไ[{C}]ย([^์]|)', syllable_string):
    process_cluster(syllable, init_vowel_char='ไ', fin_vowel_chars='ย')
elif re.search(f'ไ[{C}]', syllable_string):
    process_cluster(syllable, init_vowel_char='ไ')
elif re.search(f'ใ[{C}]', syllable_string):
    process_cluster(syllable, init_vowel_char='ใ')

elif re.search(f'[{C}]ั([{T}]|)วะ', syllable_string):
    process_cluster(syllable, vert_vowel_char='ั', fin_vowel_chars='วะ')
elif re.search(f'[{C}]ั([{T}]|)ว', syllable_string):
    process_cluster(syllable, vert_vowel_char='ั', fin_vowel_chars='ว')
elif re.search(f'[{C}]ั([{T}]|)[{C}]', syllable_string):
    process_cluster(syllable, vert_vowel_char='ั')
    process_cluster_one_final(syllable, 'ั')
elif re.search(f'[{C}]([{T}]|)ะ', syllable_string):
    process_cluster(syllable, fin_vowel_chars='ะ')
    process_cluster_one_final(syllable, 'ะ')

elif re.search(f'[{C}]็อ[{C}]', syllable_string):
    process_cluster(syllable, vert_vowel_char='็', fin_vowel_chars='อ', has_tone=False)
elif re.search(f'[{C}]([{T}]|)อ', syllable_string):
    process_cluster(syllable, fin_vowel_chars='อ')

elif re.search(f'[{C}]([{T}]|)ว[{C}]', syllable_string):
    process_cluster(syllable, fin_vowel_chars='ว')
    process_cluster_one_final(syllable, 'ว')

elif re.search(f'[{C}][{C}]', syllable_string):
    print('implied oh')

process_roles(syllable)

for thchar in syllable.thchars:
    print(thchar.cluster)