def get_book_text(book_path):
    with open(book_path) as book_file:
        return book_file.read()
def main():
    book_path = 'books/frankenstein.txt'
    book_text = get_book_text(book_path)
    number_of_words = word_count(book_text)
    print(f'{number_of_words} words found in the document')
def word_count(text):
     # Lee el contenido del archivo 
    words = text.split() # Devuelve una lista de las palabras del string
    # El método split() divide el texto en palabras usando espacios como delimitadores
    # y devuelve una lista de palabras.
    # Contamos el número de palabras en la lista
    return len(words) # Devuelve el número de palabras en la lista
main()
