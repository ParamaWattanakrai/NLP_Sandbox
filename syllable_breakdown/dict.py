th_chars = {
    'consonants': {
        'low_classes': {
            'low_paireds': {'ค','ฅ','ฆ','ช','ซ','ฌ','ฑ','ฒ','ท','ธ','พ','ฟ','ภ','ฮ'},
            'low_unpaireds': {'ง','ญ','ณ','น','ม','ย','ร','ฤ','ล','ฦ','ว','ฬ'}
            },
        'mid_classes': {'ก','จ','ฎ','ฏ','ด','ต','บ','ป','อ'},
        'high_classes': {'ข','ฃ','ฉ','ฐ','ถ','ผ','ฝ','ศ','ษ','ส','ห'},
        'blends': {'ร','ล','ว'}
    },
    'vowels': {'ะ','ั','า','ำ','ิ','ี','ึ','ื','ุ','ู','เ','แ','โ','ใ','ไ','็','ๅ'},
    'diacritics': {
        'tones': {'่','้','๊','๋'},
        'others': {'์'},
    },
    'symbols': {
        'modifies': {'ๆ','ฺ'},
        'numbers': {'๐','๑','๒','๓','๔','๕','๖','๗','๘','๙'},
        'others': {'ฯ','฿'}
    }
}

th_utils = {
    'poly_initials': {'แ','เ','โ','ั'},
    'poly_follows': {
      'แ': {'ะ','็'},
      'เ': {'ะ','า','ี','ื','็'},
      'โ': {'ะ'},
      'ั': {'ะ'}
    },
    'blend_initials': {
        'ร': {'ก','ข','ค','ต','ป','พ'},
        'ล': {'ก','ข','ค','ผ','ป','พ'},
        'ว': {'ก','ข','ค'}
    }
}

consonants = ['ก', 'ข', 'ฃ', 'ค', 'ฅ', 'ฆ', 'ง', 'จ', 'ฉ', 'ช',
    'ซ', 'ฌ', 'ญ', 'ฎ', 'ฏ', 'ฐ', 'ฑ', 'ฒ', 'ณ', 'ด',
    'ต', 'ถ', 'ท', 'ธ', 'น', 'บ', 'ป', 'ผ', 'ฝ', 'พ',
    'ฟ', 'ภ', 'ม', 'ย', 'ร', 'ฤ', 'ล', 'ฦ', 'ว', 'ศ',
    'ษ', 'ส', 'ห', 'ฬ', 'อ', 'ฮ']
vowels = ['ิ', 'ี', 'ึ', 'ื', 'ๅ', 'ุ', 'ู', 'เ', 'โ', 'แ',
    'ะ', 'ั', 'า', 'ำ', 'ใ', 'ไ', '็']
tone_marks = ['่','้','๊','๋']


low_consonants = ['ง','ญ','ณ','น','ม','ย','ร','ฤ','ล','ฦ','ว','ฬ']
unpaired_low_consonants = ['ง','ญ','ณ','น','ม','ย','ร','ล','ว','ฬ']
paired_low_consonants = ['ค','ฅ','ฆ','ช','ซ','ฌ','ฑ','ฒ','ท','ธ','พ','ฟ','ภ','ฮ']
high_consonants = ['ข','ฃ','ฉ','ฐ','ถ','ผ','ฝ','ศ','ษ','ส','ห']
mid_consonants = ['ก','จ','ฎ','ฏ','ด','ต','บ','ป','อ']

leading_consonants = ['ห','อ']

blending_consonants = ['ย','ร','ล','ว']
blend_initials = []

initial_vowels = ['แ', 'เ', 'โ', 'ไ', 'ใ']

k_final_sound = ['ก','ข','ฃ','ค','ฅ','ฆ']
p_final_sound = ['บ','ป','ผ','ฝ','พ','ฟ','ภ'] #ฝ
t_final_sound = ['จ','ฉ','ช','ฌ','ฎ','ฏ','ฐ','ฑ','ฒ','ด','ต','ถ','ท','ธ','ศ','ษ','ส']
n_final_sound = ['ญ','ณ','น','ร','ล','ฬ']
m_final_sound = ['ม']
y_final_sound = ['ย']
w_final_sound = ['ว']
ng_final_sound = ['ง']

a_forms = ['ั', 'รร', 'ะ']
aa_forms = ['า']
ae_forms = ['แ็','แะ']
aeae_forms = ['แ']
o_forms = ['็อ','เาะ']
oo_forms = ['อ']
e_forms = ['เ็','เะ']
ee_forms = ['เ']
oe_forms = ['เอะ'] # เ-ิ
oeoe_forms = ['เิ','เอ']
oh_forms = ['โะ']
ohoh_forms = ['โ']
i_forms = ['ิ']
ii_forms = ['ี']
ue_forms = ['ึ']
ueue_forms = ['ิ','ิอ']
u_forms = ['ุ']
uu_forms = ['ู']

ia_forms = ['','','','','','','']
iaia_forms = ['','','','','','','']
uea_forms = ['','','','','','','']
ueauea_forms = ['','','','','','','']
ua_forms = ['','','','','','','']
uaua_forms = ['','','','','','','']

ai_forms = ['','','','','','','']
aiai = ['','','','','','','']

class ThaiCharDict:
    def __init__(self, consonants, vowels, tone_marks,
            low_consonants, unpaired_low_consonants, paired_low_consonants, high_consonants, mid_consonants,
            leading_consonants,
            blending_consonants, blend_initials,
            initial_vowels,
            k_final_sound, p_final_sound, t_final_sound, n_final_sound, m_final_sound, y_final_sound, w_final_sound, ng_final_sound):

        self.consonants = consonants
        self.vowels = vowels
        self.tone_marks = tone_marks

        self.low_consonants = low_consonants
        self.unpaired_low_consonants = unpaired_low_consonants
        self.paired_low_consonants = paired_low_consonants
        self.high_consonants = high_consonants
        self.mid_consonants = mid_consonants

        self.leading_consonants = leading_consonants

        self.blending_consonants = blending_consonants
        self.blend_initials = blend_initials

        self.initial_vowels = initial_vowels

        self.k_final_sound = k_final_sound
        self.p_final_sound = p_final_sound
        self.t_final_sound = t_final_sound
        self.n_final_sound = n_final_sound
        self.m_final_sound = m_final_sound
        self.y_final_sound = y_final_sound
        self.w_final_sound = w_final_sound
        self.ng_final_sound = ng_final_sound

th_all = ThaiCharDict(consonants, vowels, tone_marks,
            low_consonants, unpaired_low_consonants, paired_low_consonants, high_consonants, mid_consonants,
            leading_consonants,
            blending_consonants, blend_initials,
            initial_vowels,
            k_final_sound, p_final_sound, t_final_sound, n_final_sound, m_final_sound, y_final_sound, w_final_sound, ng_final_sound)