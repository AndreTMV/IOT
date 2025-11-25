# 📡 IoT Sensors API & Dashboard

Bienvenido al proyecto **IoT Sensors**. Esta aplicación es una plataforma completa para la gestión y visualización de lecturas de sensores IoT, construida con **Django** y **Django Rest Framework**.

## 🚀 Características Principales

*   **Gestión de Sensores**: Registra y administra sensores de diferentes tipos (Ultrasonico, Temperatura, Fotoresistor).
*   **Registro de Lecturas**: Almacena lecturas de sensores con alta precisión y marcas de tiempo.
*   **API RESTful**: Endpoints robustos para interactuar con sensores y lecturas, documentados con Swagger/OpenAPI.
*   **Dashboard Interactivo**: Visualiza métricas clave, promedios de las últimas 24 horas y tendencias de los últimos 7 días.

## 🛠️ Tecnologías Utilizadas

*   **Backend**: Python, Django 5.2.8
*   **API**: Django Rest Framework, drf-yasg (Swagger)
*   **Base de Datos**: PostgreSQL (configurado mediante `psycopg2`)
*   **Utilidades**: `django-cors-headers`, `whitenoise`

## ⚙️ Instalación y Configuración

Sigue estos pasos para levantar el proyecto en tu entorno local:

1.  **Clonar el repositorio**
    ```bash
    git clone <url-del-repositorio>
    cd arqui
    ```

2.  **Crear y activar un entorno virtual**
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3.  **Instalar dependencias**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configurar la Base de Datos**
    Asegúrate de tener una base de datos PostgreSQL disponible y configura las credenciales en `arqui/settings.py` o mediante variables de entorno si es necesario.

5.  **Aplicar migraciones**
    ```bash
    python manage.py migrate
    ```

6.  **Crear un superusuario (Opcional)**
    ```bash
    python manage.py createsuperuser
    ```

7.  **Ejecutar el servidor de desarrollo**
    ```bash
    python manage.py runserver
    ```

## 📖 Uso de la API

Una vez que el servidor esté corriendo, puedes acceder a la documentación interactiva de la API en:

*   **Swagger UI**: `http://localhost:8000/docs/`

### Endpoints Principales

*   `GET /api/v1/sensor/`: Listar todos los sensores.
*   `POST /api/v1/sensor/`: Crear un nuevo sensor.
*   `GET /api/v1/lectura/`: Listar todas las lecturas.
*   `POST /api/v1/lectura/`: Registrar una nueva lectura.
*   `GET /api/v1/sensor_readings/?sensor=<id>`: Obtener lecturas específicas de un sensor.

## 📊 Dashboard

Accede al panel de visualización de datos en:

*   `http://localhost:8000/dashboard/sensores/`

Aquí podrás ver:
*   Resumen total de sensores y lecturas.
*   Estadísticas de las últimas 24 horas por sensor.
*   Gráficos de evolución de promedios en los últimos 7 días.

---
Desarrollado para la materia de Arquitectura de Computadoras.
