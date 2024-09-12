#--> Version de Python en la que va a correr el contenedor
FROM python:3.11

#--> Direcctorio de trabajo
WORKDIR /app
COPY . .

#--> Actualiza el gestor de paquetes
RUN pip install --upgrade pip
#--> Instala los requerimientos en el contenedor
RUN pip install --no-cache-dir -r requirements.txt

#--> Iniciar app en producción
CMD reflex run --env prod --backend-only