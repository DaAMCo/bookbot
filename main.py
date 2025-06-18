import sys
# main.py
from stats import *
def get_book_text(book_path):
    with open(book_path) as book_file:
        return book_file.read()
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    book_text = get_book_text(book_path)
    number_of_character = number_of_characters(book_text)
    total_characters = word_count(book_text)
    character_orderer = order_dict(number_of_character)
    # Llama a las funciones de stats.py para obtener el conteo de caracteres
    print(
        f"============ BOOKBOT ============\n"
        f"Analyzing book found at {book_path}\n"
        f"----------- Word Count ----------\n"
        f"Found {total_characters} total words\n"
        f"---------- Character Count -------")
    for character in character_orderer:
        for key, value in character.items():
            print(f"{key}: {value}")
    print('============= END ===============')
main()
