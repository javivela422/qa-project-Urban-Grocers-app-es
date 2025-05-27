import data
import sender_stand_request

def get_kit_body(name_kit):
    current_body = data.kit_body.copy()
    current_body['name'] = name_kit
    return current_body

def get_new_user_token():
    resp_user = sender_stand_request.post_new_user(data.user_body)
    value_token = resp_user.json()["authToken"]
    return value_token

def positive_assert(name_kit):
    kit_body = get_kit_body(name_kit)
    positive_kit_response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert positive_kit_response.status_code == 201
    assert positive_kit_response.json()['name'] == name_kit

def negative_assert(name_kit):
    if isinstance(name_kit, dict):
        kit_body = name_kit
    else:
        kit_body = get_kit_body(name_kit)
    negative_kit_response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert negative_kit_response.status_code == 400

     # Prueba 1 El número permitido de caracteres (1): kit_body = { "name": "a"}
def test_create_user_1_letter_in_name_kit_get_success_response():
    positive_assert("a")

    # Prueba 2 	El número permitido de caracteres (511)
def test_create_user_511_letter_in_first_name_kit_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

    # Prueba 3 	El número de caracteres es menor que la cantidad permitida (0)
def test_create_user_0_letter_in_name_kit_get_success_response():
    negative_assert("")

    # Prueba 4 El número de caracteres es mayor que la cantidad permitida (512)
def test_create_user_512_leter_in_name_kit_get_success_response():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

    # Prueba 5 	Se permiten caracteres especiales
def test_create_user_special_letter_in_name_kit_get_success_response():
    positive_assert("%$&@")

    # Prueba 6 	Se permiten espacios
def test_create_user_space_in_name_kit_get_success_response():
    positive_assert("A Aaa")

    # Prueba 7 	Se permiten números
def test_create_user_number_in_name_kit_get_success_response():
    positive_assert("123456789")

    # Prueba 8 	El parámetro no se pasa en la solicitud
def test_create_user_no_name_kit_get_success_response():
    negative_assert({})

    # Prueba 9 Se ha pasado un tipo de parámetro diferente (numero)
def test_create_user_name_kit_get_success_response():
    negative_assert(123)
