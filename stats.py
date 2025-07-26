def get_books_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def get_num_words(text):
    words = text.split()
    return len(words)


def get_char_occurances(text):
    # converting all characters to lower case
    text = text.lower()
    char_count = {}
    for char in text:
        # checking if a character is an existing key
        #     yes -> count++
        #     no -> add a new key to dictionary, count = 1
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
