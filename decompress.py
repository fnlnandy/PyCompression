from binary_container import binary_container
from compress import SEPARATOR

def deduce_encoding_table_from_content(encoded_data: binary_container) -> list[dict[str, int], binary_container]:
    '''
        Fonction qui déduit la table d'encodage de caractères
        en lisant l'en-tête des données binaires, et retourne
        la table encodée ansi que le conteneur binaire
        modifié.
    '''
    encoding_table = {}

    for i in range(1, 16):
        buffer = encoded_data.pop_back_8_bits()

        # Séparateur
        if buffer == SEPARATOR:
            break

        key_from_ascii = chr(buffer)
        encoding_table[key_from_ascii] = i

    return [encoding_table, encoded_data]

def decompress_binary_data_into_text(encoded_data: binary_container) -> str:
    '''
        Fonction qui décompresse des données binaires vers
        du texte lisible, et retourne ce texte.
    '''
    decoded_text = ""
    encoding_table = {}
    is_specially_encoded_mode = False

    encoding_table, encoded_data = deduce_encoding_table_from_content(encoded_data)

    # Dû au fait qu'on va lire 4bits mais qu'on doit vérifier si le séparateur
    # 0 (8 bits) n'a pas été rencontré, il va falloir verifier la valeur précédente,
    # actuelle et suivante en même temps.
    previous_char = -1

    while not encoded_data.is_empty():
        if not is_specially_encoded_mode:
            buff = encoded_data.pop_back_8_bits()

            # On a un séparateur.
            if buff == SEPARATOR:
                is_specially_encoded_mode = True
                continue
            
            decoded_text += chr(buff)
        else:
            current_char = encoded_data.pop_back_4_bits()
            next_char = encoded_data.peek_4_bits()

            # On a un séparateur.
            if current_char == SEPARATOR and previous_char == SEPARATOR:
                is_specially_encoded_mode = False
                previous_char = -1
                continue
            elif current_char == SEPARATOR and next_char == SEPARATOR:
                # peek4bits() ne supprime pas la valeur de
                # la liste, mais maintenant qu'on sait ce que
                # cette valeur représente, on peut s'en
                # débarasser.
                next_char = encoded_data.pop_back_4_bits()
                is_specially_encoded_mode = False
                previous_char = -1
                continue

            for key, value in encoding_table.items():
                if value != current_char:
                    continue
                
                decoded_text += key

            previous_char = current_char

    return decoded_text
            