# stats.py
def word_count(text):
    # Lee el contenido del archivo 
    words = text.split() # Devuelve una lista de las palabras del string
    # El método split() divide el texto en palabras usando espacios como delimitadores
    # y devuelve una lista de palabras.
    # Contamos el número de palabras en la lista
    return len(words) # Devuelve el número de palabras en la lista
def number_of_characters(text):
    # Cuenta el número de caracteres en el texto
    lowercase_text = text.lower()# Convierte el texto a minúsculas
    # El método lower() convierte todas las letras del texto a minúsculas
    # y devuelve una nueva cadena de texto.
    # contar el numero de caracteres por letra
    characters = {} # Creamos un diccionario para almacenar el conteo de caracteres
    for char in lowercase_text:
        if not char in characters:
            characters[char] = 1
        else:
            characters[char] += 1
    return print (characters) # Devuelve el diccionario con el conteo de caracteres
    # Recorremos el texto y contamos las letras