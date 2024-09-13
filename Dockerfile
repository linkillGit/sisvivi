#--> Version de Python en la que va a correr el contenedor
FROM python:3.11 as init

#--> Instalar `uv` para compilar ams rapidamente el arranque
ADD --chmod=755 https://astral.sh/uv/install.sh /install.sh
RUN /install.sh && rm /install.sh

#--> Crear direcctorio de trabajo
WORKDIR /app
COPY . .
RUN mkdir -p /app/data /app/uploaded_files

#--> Crea el entorno virtual
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN $uv venv

#--> Instalar requerimientos
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

#--> Prepara la aplicación
RUN reflex init

#--> Configurar palabra clave para cierre forzado
STOPSIGNAL SIGKILL

#--> Iniciar app en producción
CMD reflex run --env prod --backend-only