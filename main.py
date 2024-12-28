def main():
    file_path = "books/frankenstein.txt"

    file_content = get_file_text(file_path)

    print(file_content)
    print(get_word_count(file_content))
    print(get_char_count(file_content))
    print(print_report(file_path, get_word_count(file_content), get_char_count(file_content)))

def get_file_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
    return file_content

def get_word_count(text):
    words = text.split()
    count = len(words)
    return count

def get_char_count(text):
    char_dict = {}
    text_lowered = text.lower()
    for char in text_lowered:
        if (char in char_dict) == True:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def print_report(file_path, words_count, dict):
    print(f"--- Begin report of {file_path} ---")
    print(f"{words_count} words found in the document")
    print()
    dict_keys = dict.keys()
    list_of_dicts = []
    # iterate dict_keys, check if alpha and add key+value to a new list of dicts
    for key in dict_keys:
        if key.isalpha():
            list_of_dicts.append({"alpha": key, "num": dict[key]})
    
    list_of_dicts.sort(reverse=True, key=sort_on)

    for dict in list_of_dicts:
        print(f"The '{dict["alpha"]}' character was found {dict["num"]} times")
    
    print("--- End report ---")

main()