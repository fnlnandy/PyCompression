import text_analyzis
from binary_container import binary_container

# Constante de séparation, utilisée pour délimité l'en-tête
# et pour indiquer un changement de mode dans l'encodage.
SEPARATOR = 0

def write_encoding_table_header(source_encoding_table: dict[str, int], dest: binary_container) -> binary_container:
    '''
        Fonction qui ajoute la table d'encodage au début
        d'un conteneur binaire.
    '''
    for key in source_encoding_table.keys():
        # ord() retourne la valeur unicode d'un str.
        ascii_code = ord(key[0])
        dest.push_back_8_bits(ascii_code)
    
    # Si jamais il y a moins de 15 caractères, ce terminateur dira au
    # decomprésseur que c'est la fin de la table.
    if len(source_encoding_table.keys()) < 15:
        dest.push_back_8_bits(SEPARATOR)
    
    return dest


def compress_file_content(decoded_text: str) -> binary_container:
    '''
        Fonction qui compresse du texte en données binaires.
    '''
    encoding_table = text_analyzis.get_encoding_table(decoded_text)
    compressed_content = binary_container()
    is_specially_encoded_mode = False

    # Voici l'en-tête du fichier, celle que le décompresseur va
    # utiliser comme réference pour connaître l'index des caractères
    # les plus utilisés.
    compressed_content = write_encoding_table_header(encoding_table, compressed_content)

    for char in decoded_text:
        if char in encoding_table.keys():
            # Les caractères précedents auraient pu être des
            # caractères ASCII normaux. Cependant, le décompresseur
            # doit avoir un moyen pour connaître quand changer de
            # 'mode'; et ce moyen sera la lecture du séparateur 0b00000000.
            if not is_specially_encoded_mode:
                compressed_content.push_back_8_bits(SEPARATOR)
                is_specially_encoded_mode = True
            
            compressed_content.push_back_4_bits(encoding_table[char])
        else:
            # Les caractères précedents auraient pu être des
            # caractès encodés spécialement. Comme en haut, on
            # utilise un séparateur pour dire au décompresseur
            # de changer de 'mode'.
            if is_specially_encoded_mode:
                compressed_content.push_back_8_bits(SEPARATOR)
                is_specially_encoded_mode = False
            
            ascii_code = ord(char)
            compressed_content.push_back_8_bits(ascii_code)
    
    return compressed_content
                