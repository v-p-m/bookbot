def print_full_report(file_path, num_words, sorted_char_counts):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_count in sorted_char_counts:
        char = char_count["char"]
        if char.isalpha():
            print(f"{char_count["char"]}: {char_count["count"]}")
    print("============= END ===============")
