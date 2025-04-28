CLIMBOT en Discord: https://discord.com/oauth2/authorize?client_id=1358881010351083682

INICIAR BOT (Seguir las instrucción detalladas en "IMPORTANTE" antes de iniciar por primera vez)

1) Activar entorno virtual:

.\venv\Scripts\Activate

2) Ejecutar el bot

python bot.py

TESTING (Seguir las instrucción detalladas en "IMPORTANTE" antes de iniciar por primera vez)

1) Activar entorno virtual:

.\venv\Scripts\Activate

2) Ejecutar tests

pytest -p no:warnings -v --asyncio-mode=auto

IMPORTANTE: A continuación, las instrucciones para creación de entorno, instalación de dependencias, variables de entorno (.env) y variables de entorno para testing (.env.test). Todos estos archivos se encuentran dentro de .gitignore por lo que NO se encuentran disponibles en el repositorio de GitHub, esto por 2 motivos, peso de los archivos y sensibilidad de los datos (tokens). Para obtener el contenido del archivo .env y .env.test solicitar al Scrum Master del proyecto d.ibanez03@ufromail.cl

CREACIÓN DE ENTORNO E INSTALACIÓN DE DEPENDENCIAS

1) Crear entorno virtual python:

python -m venv venv

2) Activar entorno virtual:

.\venv\Scripts\Activate

3) Instalar dependencias:

pip install -r requirements.txt

4) Descargar modelo de SpaCy

python -m spacy download es_core_news_sm

CREACIÓN ARCHIVO .env

1) En la raíz de nuestro proyecto creamos el archivo .env

2) Completamos el contenido del archivo con los tokens brindados por el Scrum Master del proyecto (d.ibanez03@ufromail.cl)

CREACIÓN ARCHIVO .env.test

1) En la raíz de nuestro proyecto creamos el archivo .env.test

2) Completamos el contenido del archivo con los tokens brindados por el Scrum Master del proyecto (d.ibanez03@ufromail.cl)
