# FAST-API-LIBROS

## Inicializar el proyecto:
1. Clona el repositorio en un directorio local.
2. Crear el entorno virtual con el comando `python -m venv .venv`.
3. Activar el entorno virtual:
     - powershell: `.venv\Scripts\Activate.ps1`.
     - bash: `.venv\Scripts\Activate`
4. Instalar librerias con: `pip install -r requirements.txt`
5. Ejecuta el proyecto desde el directorio raiz con: `uvicorn main:app --reload`
6. Cada vez que se instale una dependencia hay que actualizar el fichero de requisitos con el comando `pip freeze > requirements.txt`.

## Flujo de seguridad: 
- Aplicación FastAPI securizada utilizando OAuth2 y JWT.
- Si accedo con un usuario activo puedo acceder a la rutas securizadas.
- Para todas las peticiones CRUD de los libros no hay que estar autenticado ya que no están securizadas.

## Probar con Swagger:
- Botón de autorización: se abre un formulario de autorización para escribir username y password.
- Hay que acceder con un usuario que exista en la base de datos (alvaro).
- La API verifica el username y password, y devuelve un "token".
- Con las credenciales: user: `alvaro` pw: `secret` devolvera la autenticación.
- Habiendo recibo el token ya se puede acceder a las rutas securizadas: `/users/me` - `/users/me/items/` y obtiene la información del usuario.
- Si se cierra la sesión y se intenta acceder a rutas securizadas se recibe: "Not authenticated".

## Documentación:
Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
Redocly: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Colección de Postman:
[Fast-Api-Libros.postman_collection.json](docs/Fast-Api-Libros.postman_collection.json)
