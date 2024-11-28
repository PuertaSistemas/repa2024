# repa2024
Plataforma de gestión para los recursos del Instituto Audiovisuales de Misiones

La plataforma está basada en la implementación de un API service basado en FastAPI, el cual consume los datos de una base de datos relacional Postgress.

El backend inmplementa la gestión de parmisos de usuario mediante JWT, en un módulo incicial de CRUD de usuarios.

## Instalación de la plataforma

Para instalar el entorno de desarrollo se debe ejecutar:

'''
$> docker compose up
'''

Ésto iniciará los contenedores de Docker con la aplicación Backend en FastAPI, el motor de base de datos Postgress y la aplicación de frontend en REACT.

Estructura de la aplicación:

'''
my_app/
├── main.py
├── db/
│   ├── database.py
├── models/
│   ├── user_model.py
├── schemas/
│   ├── user_schema.py
├── routes/
│   ├── user_routes.py
└── requirements.txt
'''
