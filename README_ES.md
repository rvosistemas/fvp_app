# FVP_APP

Este es un proyecto de plataforma financiera que utiliza un backend con FastAPI y un frontend con Angular. Este README te guiará para configurar el entorno de desarrollo, ejecutar las pruebas, y montar el proyecto en producción usando Docker.

## Requisitos previos

- Docker y Docker Compose
- Node.js y npm (para desarrollo de Angular fuera de Docker)
- Python 3.9+ y pip (para desarrollo de FastAPI fuera de Docker)

## Estructura del Proyecto

- `backend/`: Contiene el código y configuración de FastAPI.
- `frontend/`: Contiene el código de Angular.
- `docker-compose.yml`: Configuración de Docker Compose para desarrollo.
- `docker-compose.prod.yml`: Configuración de Docker Compose para producción.

## Configuración del Entorno de Desarrollo

1. Clona el repositorio:

    ```bash
    git clone https://github.com/tu_usuario/fvp_app.git
    cd fvp_app
    ```

2. Crea un archivo `.env` en la carpeta `backend` basado en el archivo `.env.example`, configurando las variables necesarias para conectarse a la base de datos local.

### 1. Levantar el Entorno en Desarrollo con Docker

Para ejecutar el proyecto en Docker en modo de desarrollo:

```bash
docker-compose up --build
Este comando levantará los contenedores para nginx, fastapi-backend, y angular-frontend.

2. Levantar el Entorno de Desarrollo Localmente (Sin Docker)
Backend - FastAPI
Navega a la carpeta backend y crea un entorno virtual:

bash
cd backend
python3 -m venv env
source env/bin/activate
Instala las dependencias:

bash
pip install -r requirements.txt
Configura la base de datos y realiza las migraciones con Alembic:

bash
alembic upgrade head
Ejecuta el servidor de desarrollo:

bash
uvicorn app.main:app --reload
El backend estará disponible en http://localhost:8000.

Frontend - Angular
Navega a la carpeta frontend e instala las dependencias:

bash
cd frontend
npm install
Ejecuta el servidor de desarrollo:

bash
ng serve
El frontend estará disponible en http://localhost:4200.

Ejecutar Pruebas
Pruebas en el Backend (FastAPI)
Navega a la carpeta backend.

Asegúrate de estar en el entorno virtual (si estás ejecutando localmente).

Ejecuta las pruebas con pytest:

bash
pytest
Para generar un reporte de cobertura:

bash
pytest --cov=app
Pruebas en el Frontend (Angular)
Navega a la carpeta frontend.

Ejecuta las pruebas unitarias con Karma:

bash
ng test
Para generar un reporte de cobertura:

bash
ng test --code-coverage
Los reportes de cobertura se encontrarán en la carpeta coverage dentro del proyecto frontend.

Configuración del Entorno de Producción
Para ejecutar el proyecto en modo de producción usando Docker:

Asegúrate de tener configurado el archivo .env.production en la carpeta backend.

Ejecuta el siguiente comando para levantar el proyecto en producción:

bash
docker-compose -f docker-compose.prod.yml up --build -d
Este comando levantará los contenedores en modo "detached" (-d) para ejecutarse en segundo plano.

Notas Importantes
Nginx: Nginx actúa como proxy inverso para dirigir el tráfico hacia el frontend y el backend. La configuración está en nginx.conf.
Base de Datos en Producción: En el archivo .env.production, configura POSTGRES_DATABASE_URL con la URL de la base de datos RDS de AWS o el servicio de base de datos que estás usando en producción.
Permisos de CORS: En el archivo main.py del backend, hemos permitido CORS para que el frontend pueda comunicarse con el backend.
Estructura del Proyecto
bash

.
├── backend
│   ├── alembic             # Manejador de migraciones
│   ├── app                 # Código de la aplicación FastAPI
│   ├── Dockerfile          # Dockerfile para FastAPI
│   └── requirements.txt    # Dependencias de FastAPI
├── frontend
│   ├── src                 # Código de la aplicación Angular
│   ├── Dockerfile          # Dockerfile para Angular
│   └── angular.json        # Configuración del proyecto Angular
├── docker-compose.yml      # Configuración para el entorno de desarrollo
└── docker-compose.prod.yml # Configuración para el entorno de producción
Troubleshooting
Error de conexión entre Frontend y Backend: Asegúrate de que CORS esté configurado correctamente y que las URLs estén configuradas correctamente en ApiService en el frontend.
Problemas con las migraciones de Alembic: Revisa el archivo alembic.ini y asegúrate de que la cadena de conexión de la base de datos sea correcta.
Errores de permiso en Docker: Asegúrate de que los contenedores tengan permisos adecuados para acceder a los volúmenes o archivos necesarios.
¡Listo! Ahora tienes una guía completa para ejecutar y probar tu proyecto en desarrollo y producción.


Este README proporciona una guía completa sobre cómo configurar el entorno de desarrollo,