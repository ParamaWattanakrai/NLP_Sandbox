import re

from th_utils_classes import *
from th_utils_regex import *

pattern = f'เ[{C}]([{C}]|)ี([{T}]|)ยะ'

syllable = ThaiSyllable("มึน")
syllable_string = syllable.syllable_string
print(syllable_string)

if re.search(f'[{C}]ึ', syllable_string):
    syllable.vowel_default = '-ึ'
    for thchar in syllable.getChar:
        thchar.selfRole('initial_consonant')
        
    print(syllable.vowel_default)
elif re.search(f'[{C}]ุ', syllable_string):
    print(syllable_string)
elif re.search(f'[{C}]ู', syllable_string):
    print(syllable_string)
elif re.search(f'[{C}]รร', syllable_string):
    print(syllable_string)
elif re.search(f'[{C}]([{T}]|)ำ', syllable_string):
    print(syllable_string)
elif re.search(f'[{C}]ฤ', syllable_string):
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
    print(syllable_string)
elif re.search(f'[{C}]ิ', syllable_string):
    print(syllable_string)
elif re.search(f'[{C}]ี', syllable_string):
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
    print(syllable_string)
elif re.search(f'[{C}]([{T}]|)ะ', syllable_string):
    print(syllable_string)

elif re.search(f'[{C}]็อ[{C}]', syllable_string):
    print(syllable_string)
elif re.search(f'[{C}]([{T}]|)อ', syllable_string):
    print(syllable_string)

elif re.search(f'[{C}]([{T}]|)ว[{C}]', syllable_string):
    print(syllable_string)

elif re.search(f'[{C}][{C}]', syllable_string):
    print(syllable_string)

    