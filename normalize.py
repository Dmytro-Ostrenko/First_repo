import re

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}
 
for c, t in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = t
    TRANS[ord(c.upper())] = t.upper()   
    


def normalize(name):
    # Прибираємо зайві символи
    translate_name = re.sub(r'\W', '_', name.translate(TRANS))
    # Замінюємо підкреслення '.' перед розширеннями, аби все читалось
    translate_name = re.sub(r'_([a-zA-Z0-9]+)$', r'.\1', translate_name)
    return translate_name  

    

