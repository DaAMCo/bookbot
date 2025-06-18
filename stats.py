# stats.py
def word_count(text):
    # Lee el contenido del archivo 
    words = text.split() # Devuelve una lista de las palabras del string
    # El método split() divide el texto en palabras usando espacios como delimitadores
    # y devuelve una lista de palabras.
    # Contamos el número de palabras en la lista
    return len(words) # Devuelve el número de palabras en la lista
def number_of_characters(text):
    #valid_letters = set('abcdefghijklmnopqrstuvwxyzæâêëô') # Definimos las letras válidas
    # Cuenta el número de caracteres en el texto
    lowercase_text = text.lower()# Convierte el texto a minúsculas
    # El método lower() convierte todas las letras del texto a minúsculas
    # y devuelve una nueva cadena de texto.
    # contar el numero de caracteres por letra
    characters = {} # Creamos un diccionario para almacenar el conteo de caracteres
    for char in lowercase_text:
        if char.isalpha(): #verifico si es una letra
        #if char in valid_letters:
            if not char in characters:
                characters[char] = 1
            else:
                characters[char] += 1
    return characters # Devuelve el diccionario con el conteo de caracteres
    # Recorremos el texto y contamos las letras
def order_dict(characters):
    dicc_ordered = dict(sorted(characters.items(), key=lambda item: item[1], reverse=True))
    list_dict = []  # Creamos una lista para almacenar los diccionarios
    for key, value in dicc_ordered.items():
        list_dict.append({key:value})
    #for i in list_dict:
     #   for key, value in i.items():
      #      print(f'{key}: {value}')
    return list_dict
    # Ordena el diccionario por el valor de los caracteres
    