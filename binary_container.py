class binary_container:
    '''
        Classe qui agit comme conteneur d'une
        liste d'int intéprétés comme bytes.
    '''
    def __init__(self, to_copy: list[int] = []) -> None:
        '''
            Constructeur de la classe.
        '''
        self.raw_data = to_copy.copy()
        self.last_elem = -1
        self.is_half_push_state = False
        self.is_half_pop_state = False
        self.is_half_peek_state = False
    
    def push_back_4_bits(self, to_push: int) -> None:
        '''
            Fonction qui ajoute 4 bits au conteneur.
        '''
        clean = to_push & 0b1111
        to_write = 0

        # On push la première moitié d'un byte, i.e.
        # 4 bits.
        if not self.is_half_push_state:
            to_write = (clean << 4)
            self.raw_data += [to_write]
            self.last_elem = len(self.raw_data) - 1
        # On a push la moitié d'un bytes, i.e. 4 bits,
        # et maintenant on doit push l'autre moitié.
        else:
            to_write = self.raw_data[self.last_elem] | clean
            self.raw_data[self.last_elem] = to_write

        self.is_half_push_state = not self.is_half_push_state

    def push_back_8_bits(self, to_push: int) -> None:
        '''
            Fonction qui ajoute 8 bits au conteneur.
        '''
        clean = to_push & 0xFF

        self.push_back_4_bits(clean >> 0x4)
        self.push_back_4_bits(clean & 0xF)
    
    def pop_back_4_bits(self) -> int:
        '''
            Fonction qui retourne et supprime 4 bits du conteneur.
        '''
        read_4_bits = 0

        # Dans certains cas spéciaux, il n'y a plus assez de bits.
        if len(self.raw_data) == 0: return 0
        if not self.is_half_pop_state:
            read_4_bits = self.raw_data[0] >> 0x4
        else:
            first_item_backup = self.raw_data.pop(0)

            read_4_bits = first_item_backup & 0xF

        self.is_half_pop_state = not self.is_half_pop_state
        return read_4_bits
    
    def peek_4_bits(self) -> int:
        '''
            Fonction qui retourne, sans supprimer, les
            4 bits suivants.
        '''
        copy = binary_container(self.raw_data)

        return copy.pop_back_4_bits()

    def pop_back_8_bits(self) -> int:
        '''
            Fonction qui retourne et supprime 8 bits du conteneur.
        '''
        read_8_bits = (self.pop_back_4_bits() << 0x4) | (self.pop_back_4_bits())

        return read_8_bits

    def write_into_file(self, file_path: str) -> bool:
        '''
            Fonction qui écrit le contenu de ce conteneur dans
            un fichier.
        '''
        
        try:
            with open(file_path, 'wb') as file:
                file.write(bytes(self.raw_data))
        # Le fichier n'existe pas, ou il y a eu un problème de permissions, etc...
        except:
            return False
        return True
    
    def read_from_file(self, file_path: str) -> bool:
        '''
            Fonction qui lit un fichier pour initialiser
            les données de ce conteneur.
        '''

        # Le fichier n'existe pas, ou il y a eu un problème de permissions, etc...
        try:
            with open(file_path, 'rb') as file:
                raw = file.read()
                self.raw_data = list(raw)
        except:
            return False
        return True
    
    def is_empty(self) -> bool:
        '''
            Fonction qui retourne si la liste que
            cette classe contient est vide.
        '''
        return len(self.raw_data) == 0