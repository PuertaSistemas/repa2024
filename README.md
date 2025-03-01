# repa2024
Plataforma de gestión para los recursos del Instituto Audiovisuales de Misiones

La plataforma está basada en la implementación de un API service basado en FastAPI, el cual consume los datos de una base de datos relacional PostgreSQL.

El backend implementa la gestión de permisos de usuario mediante JWT, en un módulo inicial de CRUD de usuarios.

## Instalación de la plataforma

Es necesario contar con docker ya instalado y funcionando correctamente.

Para instalar el entorno de desarrollo se debe ejecutar dentro del direcotrio **repa2024** es siguiente comando:

`$> docker compose up`

Esto iniciará los contenedores de docker con la aplicación backend en FastAPI, el motor de base de datos PostgreSQL y la aplicación de frontend en REACT.

Es importante configurar las variables de entorno en el archivo *.env*
El archivo .env está alojado en el PATH "./backend/src/.env" y por motivos de  compatibilidad se sugiere crear un enlace dinámico del archivo desde la raíz del proyecto con " $> ln -s ./backend/src/.env .env"

| Variable                    | Valor                                          |
|-----------------------------|------------------------------------------------|
| POSTGRES_USER               | 'postgres'                                     |
| POSTGRES_PASSWORD           | 'example'                                      |
| POSTGRES_PORT               | 5432                                           |
| POSTGRES_DB                 | 'iaavim'                                       |
| POSTGRES_DBHOST             | repa2024-db-1                                  |
| DATABASE_URL                | 'postgresql://postgres:example@db:5432/iaavim' |
| SECRET_KEY                  | '09d25e094faa6cad3e7'                          |
| ALGORITHM                   | 'HS256'                                        |
| ACCESS_TOKEN_EXPIRE_MINUTES | 30                                             |
| NODE_ENV                    | 'develop'                                      |
| PORT                        | '3000'                                         |

## Lógica de la aplicación:

La aplicación recopila información principalmente de dos tipos de entidades:
**Personas** y **Empresas**

### Relación de las entidades

```
my_app/
│
├── usuarios/
│   ├── persona*
│   ├── presentacion_personal
│   ├── obra_audiovisual
│   ├── capacitacion
│   ├── formacion*
│   ├── participacion_IAAVIM
│   ├── empresa*
│         ├── obra_audiovisual
│         ├── participacion_foros

```

La información es cargada en la plataforma a partir de un usuario.

El usuario será responsable de la información proporcionada: deberá registrar su información personal, las obras audiovisuales, capacitaciones, formación y su participación en IAAVIM.

De la misma manera, un usuario podrá registrar todas las empresas que haya creado y la información asociada a cada empresa, como las obras producidas, participaciones, etc.


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

- En el directorio **db** se encuentra el archivo de configuración de conexión a la base de datos, y es utilizado por los distintos módulos que necesitan conectarse a los datos.
- El directorio **auth** contiene las funcionalidades que permiten la gestión de tokens y la gestión de las Listas de Control de Acceso (ACL) de los usuarios.
- En el directorio **models** se encuentran definido los modelos de datos para cada uno de los objetos, como *usuarios*, *personas*, *empresas*, etc.
- En el directorio **schemas** se encuentran definidas las **clases** que define la estructura de datos para cada uno de los objetos, y cómo se interactúa con ellos en cada caso.
- En el directorio **routes** se encuentra la lógica del sistema: se declaran las rutas para la ejecución de las funcionalidades del sistema, y la lógica de funcionamiento. Implementa también las ACL a cada una de las rutas, de acuerdo a la lógica de negocio definida.

Mediante esta estructura, es posible extender el funcionamiento de la API, incorporando en cada caso los distintos elementos para un "módulo" o función.

Para incorporar el "modulo" de empresa, se debe crear un *modelo* de datos, que será creado e insertado en la base de datos. Un *schema* que define las clases para el objeto de datos que se va a manipular (una empresa, un curso, etc.) y finalmente *routes* donde se define la lógica de negocio y restricciones propias del módulo a implementar.
