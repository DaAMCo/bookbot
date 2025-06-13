# main.py
from stats import number_of_characters
def get_book_text(book_path):
    with open(book_path) as book_file:
        return book_file.read()
def main():
    book_path = 'books/frankenstein.txt'
    book_text = get_book_text(book_path)
    number_of_character = number_of_characters(book_text)
    print(number_of_character)
main()
