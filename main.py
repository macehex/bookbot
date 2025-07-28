import sys
from stats import get_num_words
from stats import get_books_text, get_char_occurances, sort_char_dict


def print_report_of(book_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")

    num_words = get_num_words(get_books_text(book_path))
    string = f"Found {num_words} total words"
    print(string)
    print("--------- Character Count -------")
    get_report_char_count(book_path)


def get_report_char_count(book_path):
    dict = {}
    dict = get_char_occurances(get_books_text(book_path))
    dict_list = []
    dict_list = sort_char_dict(dict)
    for dictionary in dict_list:
        if dictionary["char"].isalpha():
            print(f"{dictionary['char']}: {dictionary['num']}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.orig_argv[2]
        print_report_of(book_path)


main()
