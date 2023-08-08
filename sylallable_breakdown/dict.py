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

th_all = {
    'consonant_classes': {
        'low_classes': {
            'low_paireds': {'ค','ฅ','ฆ','ช','ซ','ฌ','ฑ','ฒ','ท','ธ','พ','ฟ','ภ','ฮ'},
            'low_unpaireds': {'ง','ญ','ณ','น','ม','ย','ร','ฤ','ล','ฦ','ว','ฬ'}
            },
        'mid_classes': {'ก','จ','ฎ','ฏ','ด','ต','บ','ป','อ'},
        'high_classes': {'ข','ฃ','ฉ','ฐ','ถ','ผ','ฝ','ศ','ษ','ส','ห'},
    },
    'leading_consonants': {'ห','อ'}
}

class ThaiCharDict:
    def __init__(self, consonants, vowels, tone_marks,
                low_consonants, unpaired_low_consonants, paired_low_consonants, high_consonants, mid_consonants,
                leading_consonants,
                leading_consonants, following_consonants):
        self.low_consonants = low_consonants
        self.unpaired_low_consonants = unpaired_low_consonants
        self.paired_low_consonants = paired_low_consonants
        self.high_consonants = high_consonants
        self.mid_consonants = mid_consonants

        self.leading_consonants = leading_consonants