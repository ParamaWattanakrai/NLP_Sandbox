def check_ambiguous_initial(vowel, first_char, second_char):
    ambiguous_table = {
        ('แ','ก','ร'): True,
        ('แ','ก','ล'): True,
        ('แ','ก','ว'): False,
        ('แ','ข','ร'): True,
        ('แ','ข','ล'): False,
        ('แ','ข','ว'): True,
        ('แ','ค','ร'): True,
        ('แ','ค','ล'): False,
        ('แ','ค','ว'): True,
        ('แ','ป','ร'): True,
        ('แ','ป','ล'): True,
        ('แ','พ','ร'): True,
        ('แ','พ','ล'): True,
        ('แ','ต','ร'): True,
        ('แ','ผ','ล'): True,
        
        ('เ','ก','ร'): True,
        ('เ','ก','ล'): False,
        ('เ','ก','ว'): False, #Blank
        ('เ','ข','ร'): False, #Blank
        ('เ','ข','ล'): False,
        ('เ','ข','ว'): True,
        ('เ','ค','ร'): True,
        ('เ','ค','ล'): False,
        ('เ','ค','ว'): True,
        ('เ','ป','ร'): True,
        ('เ','ป','ล'): True,
        ('เ','พ','ร'): True,
        ('เ','พ','ล'): False,
        ('เ','ต','ร'): True,
        ('เ','ผ','ล'): True,

        ('โ','ก','ร'): True,
        ('โ','ก','ล'): True,
        ('โ','ก','ว'): False,
        ('โ','ข','ร'): True,
        ('โ','ข','ล'): False,
        ('โ','ข','ว'): True, #Blank
        ('โ','ค','ร'): True,
        ('โ','ค','ล'): True,
        ('โ','ค','ว'): True,
        ('โ','ป','ร'): True,
        ('โ','ป','ล'): False,
        ('โ','พ','ร'): True,
        ('โ','พ','ล'): False,
        ('โ','ต','ร'): True,
        ('โ','ผ','ล'): True,
    }
    return ambiguous_table[(vowel, first_char, second_char)]

def get_tone(initial_class, live_dead, tone_mark):
    tone_table = {

    }
    return tone_table[(initial_class, live_dead, tone_mark)]