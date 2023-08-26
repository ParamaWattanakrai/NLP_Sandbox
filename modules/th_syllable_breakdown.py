import re

from th_utils_regex import *

print(000,T)

pattern = f'เ[{C}]([{C}]|)ี([{T}]|)ยะ'

text = "เกลี้ยะ"

if re.search(f'[{C}]ึ', text):
    print(text)
if re.search(f'[{C}]ุ', text):
    print(text)
if re.search(f'[{C}]ู', text):
    print(text)
if re.search(f'[{C}]รร', text):
    print(text)
if re.search(f'[{C}]([{T}]|)ำ', text):
    print(text)
if re.search(f'[{C}]ฤ', text):
    print(text)

if re.search(f'แ[{C}]([{C}]|)็([{T}]|)[{C}]', text):
    print(text)
if re.search(f'แ[{C}]([{C}]|)([{T}]|)ะ', text):
    print(text)
if re.search(f'แ[{C}]', text):
    print(text)

if re.search(f'เ[{C}]([{C}]|)ี([{T}]|)ยะ', text):
    print(text)
if re.search(f'เ[{C}]([{C}]|)ี([{T}]|)ยะ', text):
    print(text)
if re.search(f'เ[{C}]([{C}]|)ื([{T}]|)อะ', text):
    print(text)
if re.search(f'เ[{C}]([{C}]|)([{T}]|)อะ', text):
    print(text)
if re.search(f'เ[{C}]([{C}]|)([{T}]|)าะ', text):
    print(text)
if re.search(f'เ[{C}]([{C}]|)([{T}]|)ะ', text):
    print(text)
if re.search(f'เ[{C}]([{C}]|)ื([{T}]|)อ', text):
    print(text)
if re.search(f'เ[{C}]([{C}]|)([{T}]|)อ', text):
    print(text)
if re.search(f'เ[{C}]([{C}]|)ิ([{T}]|)[{C}]', text):
    print(text)
if re.search(f'เ[{C}]', text):
    print(text)
if re.search(f'[{C}]([{T}]|)า', text):
    print(text)
if re.search(f'[{C}]ิ', text):
    print(text)
if re.search(f'[{C}]ี', text):
    print(text)

if re.search(f'[{C}]([{C}]|)ื([{T}]|)อ', text):
    print(text)
if re.search(f'[{C}]ื([{T}]|)[{C}]', text):
    print(text)

if re.search(f'โ[{C}]([{C}]|)([{T}]|)ะ', text):
    print(text)
if re.search(f'โ[{C}]', text):
    print(text)

if re.search(f'ไ[{C}]ย', text):
    print(text)
if re.search(f'ไ[{C}]', text):
    print(text)
if re.search(f'ใ[{C}]', text):
    print(text)

if re.search(f'[{C}]ั([{T}]|)วะ', text):
    print(text)
if re.search(f'[{C}]ั([{T}]|)ว', text):
    print(text)
if re.search(f'[{C}]ั([{T}]|)[{C}]', text):
    print(text)
if re.search(f'[{C}]([{T}]|)ะ', text):
    print(text)

if re.search(f'[{C}]็อ[{C}]', text):
    print(text)
if re.search(f'[{C}]([{T}]|)อ', text):
    print(text)

if re.search(f'[{C}]([{T}]|)ว[{C}]', text):
    print(text)

if re.search(f'[{C}][{C}]', text):
    print(text)

    