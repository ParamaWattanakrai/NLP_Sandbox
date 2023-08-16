from pythainlp.tokenize import Tokenizer

PATH_TO_CUSTOM_DICTIONARY = './custom_dictionary.txtt'

# write a file
# with open(PATH_TO_CUSTOM_DICTIONARY, 'w', encoding='utf-8') as f:
#     f.write('อะเฟเซีย\nAphasia\nผิด\nปกติ')

text = "อะเฟเซีย (Aphasia) เป็นอาการผิดปกติของการพูด"

# initate an object from file with `attacut` as tokenizer
_tokenizer = Tokenizer(custom_dict=PATH_TO_CUSTOM_DICTIONARY, \
    engine='newmm')

print(_tokenizer.word_tokenize('กรณี'))
# output:
# ['อะเฟเซีย', ' ', '(', 'Aphasia', ')', ' ', 'เป็น', 'อาการ', 'ผิด',
#   'ปกติ', 'ของ', 'การ', 'พูด']