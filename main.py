from binary_container import binary_container
from encrypt import parse_file_content, transition_encryption
from compress import compress_file_content
from decompress import decompress_binary_data_into_text
from sys import argv

def try_decompressing_a_file() -> None:
    '''
        Fonction qui décompresse un fichier compressé et encodé.
    '''
    file_path_to_decompress = input("Entrez le nom du fichier à décompresser: ")
    compressed_file_content = binary_container()
    
    success_in_reading = compressed_file_content.read_from_file(file_path_to_decompress)

    if not success_in_reading:
        print(f"Il y a eu une erreur durant la lécture du fichier '{file_path_to_decompress}'.")
        return
    
    decompressed_text = decompress_binary_data_into_text(compressed_file_content)
    decompressed_text = transition_encryption(decompressed_text)
    destination_file = input("Entrez le fichier de destination: ")

    try:
        with open(destination_file, 'w', encoding='utf-8') as file:
            file.write(decompressed_text)
    except:
        print(f"Il y a eu une erreur durant l'écriture du fichier '{destination_file}'.")
        return
    
    print(f"'{file_path_to_decompress}' a été décompressé vers '{destination_file}'.")


def try_compressing_a_file() -> None:
    '''
        Fonction qui compresse un fichier texte normal.
    '''
    file_path_to_compress = input("Entrez le nom du fichier à compresser: ")
    decompressed_file_content = parse_file_content(file_path_to_compress)

    if len(file_path_to_compress) == 0:
        print(f"Il y a eu une erreur durant la lécture du fichier '{file_path_to_compress}'.")
        return

    decompressed_file_content = transition_encryption(decompressed_file_content)
    compressedContent = compress_file_content(decompressed_file_content)
    destination_file = input("Entrez le fichier de destination: ")
    success_in_writing = compressedContent.write_into_file(destination_file)

    if not success_in_writing:
        print(f"Il y a eu une erreur dans l'écriture du fichier '{destination_file}'.")
        return
    
    print(f"'{file_path_to_compress}' a été compressé vers '{destination_file}'.")

if __name__ == "__main__":
    if len(argv) == 1 or (('-c' in argv) and ('-d' in argv)) or (('-c' not in argv) and ('-d' not in argv)):
        print("Usage: [main.py] [-c (Compress)]|[-d (Decompress)]")
        exit(0)

    if '-c' in argv:
        try_compressing_a_file()
    else:
        try_decompressing_a_file()
