# Books API - Proyecto Django con MongoDB

## Descripción

Este proyecto implementa una API REST para gestionar información de libros utilizando **MongoDB** como base de datos y **Django** con **Django REST Framework (DRF)** para la exposición de la API. La API permite realizar operaciones CRUD sobre los libros y utilizar un pipeline de agregación en MongoDB para obtener el precio promedio de los libros publicados en un año específico.

El proyecto también incluye autenticación mediante **JWT** y documentación de la API utilizando **Swagger**.

---

## Requisitos

- **Python 3.8+**
- **MongoDB**
- **Poetry** (para la gestión de dependencias)
- **Django** y **Django REST Framework**
- **Pymongo** (para la integración con MongoDB)

---

## Pasos para la Instalación

### 1. Clonar el Repositorio

Primero, clona el repositorio del proyecto en tu máquina local:

```bash
git clone https://github.com/tu_usuario/books-api.git
cd books-api
```

### 2. Instalar Poetry
Si no tienes Poetry instalado, puedes hacerlo de la siguiente forma:

En macOS/Linux:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

En Windows:

Sigue las instrucciones oficiales en Poetry Docs.


### 3. Crear y Activar un Entorno Virtual con Poetry

Dentro del directorio de tu proyecto, ejecuta:

```bash
poetry install
poetry shell
```

### 4. Ejecutar el Servidor
Para iniciar el servidor de desarrollo de Django, ejecuta:

```bash
python manage.py runserver
```

El servidor estará disponible en http://localhost:8000/.

## Uso de la API
### Documentación de la API (Swagger)
Accede a la documentación interactiva de la API usando Swagger en:

```bash
http://localhost:8000/swagger/
```

## Autenticación JWT
Para autenticarte en la API, utiliza el endpoint de autenticación JWT:

POST /api/token/: Obtén un token de autenticación.

Envía las credenciales del usuario de la siguiente manera:

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

Esto devolverá un access token y un refresh token. Usa el token de acceso en las siguientes peticiones de la API como:

```bash
Authorization: Bearer <access_token>
```

## Endpoints

- **POST /api/token/**: Obtiene un token de autenticación JWT.
- **GET /api/books/:** Obtiene la lista de libros con paginación.
- **POST /api/books/:** Crea un nuevo libro.
- **GET /api/books/{id}/:** Obtiene los detalles de un libro específico.
- **PUT /api/books/{id}/:** Actualiza un libro existente.
- **DELETE /api/books/{id}/:** Elimina un libro.
- **GET /api/books/avg-price/{year}/:** Obtiene el precio promedio de los libros publicados en un año usando un pipeline de agregación de MongoDB.


## Pruebas
Las pruebas están definidas en books/tests.py. Puedes ejecutar las pruebas unitarias utilizando el siguiente comando:

```bash
pytest
```