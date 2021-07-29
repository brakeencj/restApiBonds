============
restApiBonds
============

==================================================
Construyendo APIs con **Django Rest Framework**
==================================================

Challenge
=============
Puede ejecutarse el proyecto en modo desarrollo en la máquina, recomendándose la instalación en un virtualenv.
Para ello::

    # Clonar proyecto
    git clone https://github.com/brakeencj/restApiBonds.git
    # Acceder al directorio del challenge
    cd restApi
    # Instalar dependencias
    pip install -r requirements.txt
    # Crear y rellenar base de datos
    python manage.py migrate --no-input
    # Inicializar el proyecto en modo desarrollo escuchando en puerto 8000
    python manage.py runserver 8000

Tras la instalación y configuración el proyecto pasará a estar disponible en
`localhost en el puerto 8000 <http://localhost:8000/>`_.

Documentación
=============
La documentación se puede consultar en la siguiente liga:
`localhost:8000/redoc <http://localhost:8000/redoc>`_.

Además se pueden hacer pruebas de las consultan en la siguiente liga: 
`localhost:8000/swagger <http://localhost:8000/swagger>`_.

Para autentificarse ir a la siguiente liga de administración: 
`localhost:8000/admin <http://localhost:8000/admin>`_.


Copyright
=========

Brakeen 2021.
