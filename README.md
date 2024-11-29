# repa2024
Plataforma de gestión para los recursos del Instituto Audiovisuales de Misiones

La plataforma está basada en la implementación de un API service basado en FastAPI, el cual consume los datos de una base de datos relacional Postgress.

El backend inmplementa la gestión de parmisos de usuario mediante JWT, en un módulo incicial de CRUD de usuarios.

## Instalación de la plataforma

Es necesario contar con Docker ya instalado y funcionando correctamente.

Para instalar el entorno de desarrollo se debe ejecutar, dentro del direcotrio **repa2024** es siguiente comando:

`$> docker compose up`

Ésto iniciará los contenedores de Docker con la aplicación Backend en FastAPI, el motor de base de datos Postgress y la aplicación de frontend en REACT.

## Estructura de la aplicación:

La API de Backend mantiene la sigueinte estructura de directorios:

```
my_app/
├── main.py
├── auth/
│   ├── auth.py
│   ├── permissions.py
├── db/
│   ├── database.py
├── models/
│   ├── user_model.py
├── schemas/
│   ├── user_schema.py
├── routes/
│   ├── user_routes.py
└── requirements.txt
```

- En el directorio **db** se encuentra el archivo de configuración de conexión a la base de datos, y es utulizado por los distintos módulos que necesitan conectarse a los datos.
- El directorio **auth** contiene las funcionalidades que permiten la gestión de Tockens y la gestión de las Listas de Control de Acceso (ACL) de los usuarios
- En el directorio **models** se encuentra definido los modelos de datos para cada uno de los objetos. Como *usuarios*, *personas*, *empresas*, etc.
- En el directorio **schemas** se encuentra definido las **clases** que define la estructura de datos para cada uno de los objetos, y cómo se interactúa con ellos en cada caso.
- En el directorio **routes** se encuentra la lógica del sistema. Se declaran las rutas para la ejecucón de las funcionalidades del sistema, y la lógica de funcionamiento. Implementa también las ACL de acceso a cada una de las rutas, de acuerdo a la lógica de negocio definida.

Mediante ésta estructúra, es posible extender el funcionamiento de la API, incorporando en cada caso los distintos elementos para un "modulo" o función.

Para incorporar el "modulo" de empresa, se debe crear un *modelo* de datos, que será creado e incertado en la base de datos. Un *schema* que define las clases para el objeto de datos que se va a manipular (una empresa, un curso, etc.) y finalmente *rutes* donde se define la lógica de negocio y restricciones propias del módulo a implementar.
