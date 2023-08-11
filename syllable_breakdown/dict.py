th_archive = {
    'symbols': {
        'modifies': {'ๆ','ฺ'},
        'numbers': {'๐','๑','๒','๓','๔','๕','๖','๗','๘','๙'},
        'others': {'ฯ','฿'}
    }
}

th_chars = {
    'consonants': [
        'ก', 'ข', 'ฃ', 'ค', 'ฅ', 'ฆ', 'ง', 'จ', 'ฉ', 'ช',
        'ซ', 'ฌ', 'ญ', 'ฎ', 'ฏ', 'ฐ', 'ฑ', 'ฒ', 'ณ', 'ด',
        'ต', 'ถ', 'ท', 'ธ', 'น', 'บ', 'ป', 'ผ', 'ฝ', 'พ',
        'ฟ', 'ภ', 'ม', 'ย', 'ร', 'ฤ', 'ล', 'ฦ', 'ว', 'ศ',
        'ษ', 'ส', 'ห', 'ฬ', 'อ', 'ฮ'
        ],
    'vowels': [
        'ิ', 'ี', 'ึ', 'ื', 'ๅ', 'ุ', 'ู', 'เ', 'โ', 'แ',
        'ะ', 'ั', 'า', 'ำ', 'ใ', 'ไ', '็'
        ],
    'tone_marks': ['่','้','๊','๋'],


    'low_consonants': ['ง','ญ','ณ','น','ม','ย','ร','ฤ','ล','ฦ','ว','ฬ'],
    'unpaired_low_consonants': ['ง','ญ','ณ','น','ม','ย','ร','ล','ว','ฬ'],
    'paired_low_consonants': ['ค','ฅ','ฆ','ช','ซ','ฌ','ฑ','ฒ','ท','ธ','พ','ฟ','ภ','ฮ'],
    'high_consonants': ['ข','ฃ','ฉ','ฐ','ถ','ผ','ฝ','ศ','ษ','ส','ห'],
    'mid_consonants': ['ก','จ','ฎ','ฏ','ด','ต','บ','ป','อ'],

    'leading_consonants': ['ห','อ'],

    'blending_consonants': ['ย','ร','ล','ว'],
    'r_l_blending_initials': ['ก','ข','ค','ต','ป','พ'],
    'w_blending_initials': ['ก','ข','ค'],

    'initial_vowels': ['แ', 'เ', 'โ', 'ไ', 'ใ'],

    'k_final_sound': ['ก','ข','ฃ','ค','ฅ','ฆ'],
    'p_final_sound': ['บ','ป','ผ','ฝ','พ','ฟ','ภ'], #ฝ
    't_final_sound': ['จ','ฉ','ช','ฌ','ฎ','ฏ','ฐ','ฑ','ฒ','ด','ต','ถ','ท','ธ','ศ','ษ','ส'],
    'n_final_sound': ['ญ','ณ','น','ร','ล','ฬ'],
    'm_final_sound': ['ม'],
    'y_final_sound': ['ย'],
    'w_final_sound': ['ว'],
    'ng_final_sound': ['ง'],

    'a_forms': ['ั', 'รร', 'ะ'],
    'aa_forms': ['า'],
    'ae_forms': ['แ็','แะ'],
    'aeae_forms': ['แ'],
    'o_forms': ['็อ','เาะ'],
    'oo_forms': ['อ'],
    'e_forms': ['เ็','เะ'],
    'ee_forms': ['เ'],
    'oe_forms': ['เอะ'], # เ-ิ
    'oeoe_forms': ['เิ','เอ'],
    'oh_forms': ['โะ'],
    'ohoh_forms': ['โ'],
    'i_forms': ['ิ'],
    'ii_forms': ['ี'],
    'ue_forms': ['ึ'],
    'ueue_forms': ['ิ','ิอ'],
    'u_forms': ['ุ'],
    'uu_forms': ['ู'],

    'ia_forms': ['เียะ','เีย','','','','',''],
    'iaia_forms': ['','','','','','',''],
    'uea_forms': ['','','','','','',''],
    'ueauea_forms': ['','','','','','',''],
    'ua_forms': ['','','','','','',''],
    'uaua_forms': ['','','','','','',''],

    'ai_forms': ['','','','','','',''],
    'aiai': ['','','','','','',''],
}

CONSONANTS = th_chars['consonants']
VOWELS = th_chars['vowels']
TONE_MARKS = th_chars['tone_marks']

LOW_CONSONANTS = th_chars['low_consonants']
UNPAIRED_LOW_CONSONANTS = th_chars['unpaired_low_consonants']
PAIRED_LOW_CONSONANTS = th_chars['paired_low_consonants']
HIGH_CONSONANTS = th_chars['high_consonants']
MID_CONSONANTS = th_chars['mid_consonants']

LEADING_CONSONANTS = th_chars['leading_consonants']

BLENDING_CONSONANTS = th_chars['blending_consonants']
R_L_BLENDING_INITIALS = th_chars['r_l_blending_initials']
W_BLENDING_INITIALS = th_chars['w_blending_initials']

INITIAL_VOWELS = th_chars['initial_vowels']

K_FINAL_SOUND = th_chars['k_final_sound']
P_FINAL_SOUND = th_chars['p_final_sound']
T_FINAL_SOUND = th_chars['t_final_sound']
N_FINAL_SOUND = th_chars['n_final_sound']
M_FINAL_SOUND = th_chars['m_final_sound']
Y_FINAL_SOUND = th_chars['y_final_sound']
W_FINAL_SOUND = th_chars['w_final_sound']
NG_FINAL_SOUND = th_chars['ng_final_sound']