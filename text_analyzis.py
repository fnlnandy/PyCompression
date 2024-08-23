import sort_dict

def get_character_use_stats(to_analyze: str, max_iterations: int = 0) -> dict[str, int]:
    '''
        Fonction qui retourne les statistiques d'utilisation de chaque
        caractère dans un texte.
    '''
    use_stats_dict = {}
    counter = 0

    for character in to_analyze:
        if max_iterations > 0 and counter >= max_iterations: break

        if character in use_stats_dict.keys():
            use_stats_dict[character] += 1
        else:
            use_stats_dict[character] = 1
            counter += 1

    return use_stats_dict

def get_most_used_characters(to_analyze: str, max_iterations: int = 0) -> dict[str, int]:
    '''
        Fonction qui retourne les 15 caractères les plus
        utilisés dans un texte.
    '''
    use_stats_dict = get_character_use_stats(to_analyze)
    most_used_dict = {}
    counter = 0

    if len(use_stats_dict) == 0: return most_used_dict
    
    use_stats_dict = sort_dict.sort_dict_in_reverse(use_stats_dict)

    for key, value in use_stats_dict.items():
        if counter >= max_iterations: break

        most_used_dict[key] = value
        counter += 1

    return most_used_dict

def get_encoding_table(to_analyze: str) -> dict[str, int]:
    '''
        Fonction qui retourne la table d'encodage pour
        les 15 caractères.
    '''
    most_used_dict = get_most_used_characters(to_analyze, 15)
    encoding_table = most_used_dict.copy()
    counter = 0b0001

    for key in encoding_table.keys():
        encoding_table[key] = counter
        counter += 1

    return encoding_table