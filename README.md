# FAST-API-LIBROS

## Flujo de seguridad: 
- Si accedo con un usuario activo(alvaro) puedo acceder a la rutas securizadas
- Para todas las peticiones CRUD de los libros no hay que estar logueado.

## Probar con Swagger:
- Primero hay que loguearse (para loguearse solo hay que ejecutar la peticion POST /token introduciendo un username y passw que exista en la bbdd de users ) para obtener el token y teniendo el token ya puedes acceder a traves del boton Authorize de Swagger
- Poner usuario y contraseña y ya puedes accder a las rutas securizadas.
- user: alvaro pw: secret

## Documentación:
Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
Redocly: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Colección de Postman:
[Fast-Api-Libros.postman_collection.json](docs/Fast-Api-Libros.postman_collection.json)
