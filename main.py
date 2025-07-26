from stats import get_num_words
from stats import get_books_text, get_char_occurances


def main():
    # call get_books_text() to parse text
    num_words = get_num_words(get_books_text("books/frankenstein.txt"))
    string = f"{num_words} words found in the document"
    print(string)
    print(get_char_occurances(get_books_text("books/frankenstein.txt")))


main()
