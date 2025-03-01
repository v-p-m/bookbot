import sys
from stats import get_num_words, get_char_num, sorted_dict_list
from reports import print_full_report

def main():
    #file_path = "books/frankenstein.txt"
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    file_content = get_book_text(file_path)
    total_words = get_num_words(file_content)
    chars_dict = get_char_num(file_content)
    sorted_list = sorted_dict_list(chars_dict)
    print_full_report(file_path, total_words, sorted_list)

def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()

    return file_content

main()