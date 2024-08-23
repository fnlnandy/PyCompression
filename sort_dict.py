def __sort_dict_core_lists_internal__(keys_list: list[str], values_list: list[int]) -> list[list[str], list[int]]:
    '''
        Fonction qui trie deux listes, qui correspondent
        respectivement aux clés et aux valeurs d'un dictionnaire.
        Le tri se fait par triage en bulle, et elle retourne
        les deux listes triées.
    '''
    for i in range(len(values_list) - 1, 0, -1):
        for j in range(0, i):
            current_value = values_list[j]
            next_value = values_list[j + 1]

            if current_value < next_value:
                temp_key = keys_list[j]
                
                values_list[j] = next_value
                values_list[j + 1] = current_value
                keys_list[j] = keys_list[j + 1]
                keys_list[j + 1] = temp_key
    
    return [keys_list, values_list]

def __create_dict_core_lists_internal__(source_dict: dict[str, int]) -> list[list[str], list[int]]:
    '''
        Fonction qui sépare en deux listes les clés
        et les valeurs d'un dictionnaire, et retourne
        ces listes.
    '''
    keys = list[str](source_dict.keys())
    values = list[int](source_dict.values())

    return [keys, values]

def sort_dict_in_reverse(dict_to_sort: dict[str, int]) -> dict[str, int]:
    '''
        Fonction qui trie un dictionnaire par ordre
        décroissant, et retourne le nouveau dictionnaire
        trié.
    '''
    dict_keys, dict_values = __create_dict_core_lists_internal__(dict_to_sort)
    dict_keys, dict_values = __sort_dict_core_lists_internal__(dict_keys, dict_values)

    # zip() va associer chaque valeur de dictKeys et dictValues
    # par rapport à leurs index.
    sorted_dict = dict(zip(dict_keys, dict_values))

    return sorted_dict
