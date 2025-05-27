import requests

import configuration
import data


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


def post_new_client_kit(kit_body, token):
    # Creamos una copia local de los headers
    headers = data.headers.copy()
    # Añadimos el token de autorización
    headers["Authorization"] = "Bearer " + token

    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
                         json=kit_body,
                         headers=headers)


# Crear un nuevo usuario
user_response = post_new_user(data.user_body)
auth_token = user_response.json()["authToken"]

# Crear un nuevo kit usando una copia del kit_body
kit_response = post_new_client_kit(data.kit_body.copy(), auth_token)
print(kit_response.status_code)
print(kit_response.json())
