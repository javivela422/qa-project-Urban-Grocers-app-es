headers = {
    "Content-Type": "application/json"
}

user_body = {
    "firstName": "Andrea",
    "phone": "+11234567890",
    "address": "123 Elm Street, Hilltop"
}

kit_body = {
    "name": "Mi conjunto"
}
# Variable para la prueba de un carácter
one_letter = "a"

# Variable para la prueba de caracteres especiales
special_characters = "%$&@"

# Variable para la prueba de espacios
space_in_name = "A Aaa"

# Variable para la prueba de números
numbers = "123456789"

# Variables para las pruebas de longitud
empty_name = ""  # 0 caracteres
max_length_name = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"  # 511 caracteres

over_max_length_name = max_length_name + "D"  # 512 caracteres

#El parámetro no se pasa en la solicitud
without_parameter = {}

# Se ha pasado un tipo de parámetro diferente (número)
different_parameter = 123
