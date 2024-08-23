CRYPTING_DICT = {
    'a': 'z',
    'b': 'y',
    'c': 'x',
    'd': 'w',
    'e': 'v',
    'f': 'u',
    'g': 't',
    'h': 's',
    'i': 'r',
    'j': 'q',
    'k': 'p',
    'l': 'o',
    'm': 'n'
}

def transition_encryption(wrong_state_text: str) -> str:
    '''
        Fonction qui permet de 'transitionner'
        l'encodage d'un string, i.e.:
        Encodé -> Décodé & Décodé -> Encodé
        et retourne le string encodé/décodé.
    '''
    right_state_text = ""

    for char in wrong_state_text:
        encrypted = False
        low = char.islower()
        to_find = char.lower()
        
        for (key, value) in CRYPTING_DICT.items():
            if to_find == key:
                right_state_text += value if low else value.upper()
                encrypted = True
                break
            elif to_find == value:
                right_state_text += key if low else key.upper()
                encrypted = True
                break
        
        if not encrypted:
            right_state_text += char
    
    return right_state_text

def parse_file_content(file_path: str) -> str:
    '''
        Fonction qui lit tout le contenu
        d'un fichier et retourne ce contenu.
    '''
    parsed_file_content = ""

    try:
        with open(file_path, "r") as file:
            parsed_file_content = file.read()
        
        return parsed_file_content
    
    except:
        return ""
