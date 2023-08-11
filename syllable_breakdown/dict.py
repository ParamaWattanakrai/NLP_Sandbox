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

    'ia_forms': ['เียะ'],
    'iaia_forms': ['เีย'],
    'uea_forms': ['ือะ'],
    'ueauea_forms': ['เือ'],
    'ua_forms': ['ัวะ'],
    'uaua_forms': ['ว','ัว'], # ะ ว

    'ay_forms': ['ไ','ใ','ไย'],
    'ayay': ['าย'],
    'oy': ['็ฮย'],
    'oyoy': ['อย'],
    'oeyoey': ['เย'],
    'ohyohy': ['โย'],
    'uy': ['ุย'],
    'ueayueay': ['เือย'],
    'uay': ['วย'],
    'uayuay': ['วาย'],

    'aw': ['เา'],
    'awaw': ['าว'],
    'aew': ['แ็ว'],
    'aewaew': ['แว'],
    'eoweow': ['เอว'],
    'ew': ['เ็ว'],
    'ewew': ['เว'],
    'iw': ['ิว'],
    'iawiaw': ['เียว'],

    'am': ['ำ'], #amam
    'rue': ['ฤ'],

    'vowel_forms': {
        '-ะ': ['ั', 'รร', 'ะ'],
        '-า': ['า'],
        'แ-ะ': ['แ็','แะ'],
        'แ-': ['แ'],
        'เ-าะ': ['็อ','เาะ'],
        '-อ': ['อ'],
        'เ-ะ': ['เ็','เะ'],
        'เ-': ['เ'],
        'เ-อะ': ['เอะ'], # เ-ิ
        'เ-อ': ['เิ','เอ'],
        'โ-ะ': ['โะ'],
        'โ-': ['โ'],
        '-ิ': ['ิ'],
        '-ี': ['ี'],
        '-ึ': ['ึ'],
        '-ื': ['ิ','ิอ'],
        '-ุ': ['ุ'],
        '-ู': ['ู'],

        'เ-ียะ': ['เียะ'],
        'เ-ีย': ['เีย'],
        'เ-ือะ': ['ือะ'],
        'เ-ือ': ['เือ'],
        '-ัวะ': ['ัวะ'],
        '-ัว': ['ว','ัว'], # ะ ว

        'ไ-': ['ไ','ใ','ไย'],
        '-าย': ['าย'],
        '-็อย': ['็ฮย'],
        '-อย': ['อย'],
        'เ-ย': ['เย'],
        'โ-ย': ['โย'],
        '-ุย': ['ุย'],
        'เ-ือย': ['เือย'],
        '-วย': ['วย'],
        '-วาย': ['วาย'],

        'เ-า': ['เา'],
        '-าว': ['าว'],
        'แ-็ว': ['แ็ว'],
        'แ-ว': ['แว'],
        'เ-อว': ['เอว'],
        'เ-็ว': ['เ็ว'],
        'เ-ว': ['เว'],
        '-ิว': ['ิว'],
        'เ-ียว': ['เียว'],

        '-ำ': ['ำ'], #amam
        '-ฤ': ['ฤ'],
    },

    'short_vowel_forms': []
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

A_FORMS = th_chars['a_forms']
AA_FORMS = th_chars['aa_forms']
AE_FORMS = th_chars['ae_forms']
AEAE_FORMS = th_chars['aeae_forms']
O_FORMS = th_chars['o_forms']
OO_FORMS = th_chars['oo_forms']
E_FORMS = th_chars['e_forms']
EE_FORMS = th_chars['ee_forms']
OE_FORMS = th_chars['oe_forms']
OEOE_FORMS = th_chars['oeoe_forms']
OH_FORMS = th_chars['oh_forms']
OHOH_FORMS = th_chars['ohoh_forms']
I_FORMS = th_chars['i_forms']
II_FORMS = th_chars['ii_forms']
UE_FORMS = th_chars['ue_forms']
UEUE_FORMS = th_chars['ueue_forms']
U_FORMS = th_chars['u_forms']
UU_FORMS = th_chars['uu_forms']

IA_FORMS = th_chars['ia_forms']
IAIA_FORMS = th_chars['iaia_forms']
UEA_FORMS = th_chars['uea_forms']
UEAUEA_FORMS = th_chars['ueauea_forms']
UA_FORMS = th_chars['ua_forms']
UAUA_FORMS = th_chars['uaua_forms']

AY_FORMS = th_chars['ay_forms']
AYAY_FORMS = th_chars['ayay']
OY_FORMS = th_chars['oy']
OYOY_FORMS = th_chars['oyoy']
OEYOEY_FORMS = th_chars['oeyoey']
OHYOHY_FORMS = th_chars['ohyohy']
UY_FORMS = th_chars['uy']
UEAYUEAY_FORMS = th_chars['ueayueay']
UAY_FORMS = th_chars['uay']
UAYUAY_FORMS = th_chars['uayuay']

AW_FORMS = th_chars['aw']
AWAW_FORMS = th_chars['awaw']
AEW_FORMS = th_chars['aew']
AEWAEW_FORMS = th_chars['aewaew']
EOWEOW_FORMS = th_chars['eoweow']
EW_FORMS = th_chars['ew']
EWEW_FORMS = th_chars['ewew']
IW_FORMS = th_chars['iw']
IAWIAW_FORMS = th_chars['iawiaw']

AM_FORMS = th_chars['am']
RUE_FORMS = th_chars['rue']

VOWEL_FORMS = th_chars['vowel_forms']