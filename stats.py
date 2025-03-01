def get_num_words(file_content):
    words = file_content.split()
    return len(words)

def get_char_num(file_content):
    chars_dict = {}
    for char in file_content:
        if char.lower() in chars_dict:
            chars_dict[char.lower()] += 1
        else:
            chars_dict[char.lower()] = 1
    return chars_dict

def sorted_dict_list(chars_dict):
    list_dicts = []
    for key, value in chars_dict.items():
        list_dicts.append({
            "char": key,
            "count": value
        })
    list_dicts.sort(reverse=True, key=lambda dict: dict["count"])
    return list_dicts