text = "An apple a day keeps the doctor away"

def words(t):
    words_number = 0
    stripped = text.split()
    for i in stripped:
        words_number += 1
    return words_number

def sort_words_by_length(text):
    # split makes the list, sorted ogarnia resztę
    words = text.split()
    return sorted(words, key=len, reverse=True)


def sort_words_by_alphabet(text):
    # split makes the list, sorted ogarnia resztę
    words = text.split()
    return sorted(words)

