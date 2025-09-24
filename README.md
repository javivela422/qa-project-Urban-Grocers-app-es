## 🧪 README — `create_kit_name_kit_test`

Este módulo contiene pruebas automatizadas para validar el comportamiento de la función `create_kit` en relación con el parámetro `name_kit`.

### 📋 Descripción

Las pruebas están diseñadas para verificar que el parámetro `name_kit`:

- Se reciba correctamente al momento de crear un kit.
- Maneje adecuadamente valores como listas vacías (`[]`), listas con datos válidos y entradas inválidas.
- Genere respuestas esperadas del sistema (por ejemplo, códigos de estado HTTP, mensajes de error o confirmación).

### 📦 Requisitos

Antes de ejecutar las pruebas, asegúrate de tener instalados los siguientes paquetes:

```bash
pip install pytest requests
```

### 🚀 Ejecución de pruebas

Puedes ejecutar las pruebas de dos formas:

- **Desde la terminal**:

  ```bash
  pytest
  ```

- **Desde PyCharm**:
  - Usa la consola integrada.
  - O haz clic derecho sobre el archivo `create_kit_name_kit_test.py` y selecciona **"Run"**.

### ✅ Casos cubiertos

Las pruebas incluyen:

- `test_create_kit_with_empty_name_kit`: Verifica que el sistema acepte una lista vacía sin errores.
- `test_create_kit_with_valid_name_kit`: Comprueba que se cree el kit correctamente con datos válidos.
- `test_create_kit_with_invalid_name_kit`: Asegura que se rechacen entradas mal formateadas o no permitidas.

```

### 🛡️ Buenas prácticas

- Usa fixtures para preparar datos reutilizables.
- Mantén los nombres de las pruebas descriptivos.
- Documenta los casos límite y errores esperados.

---