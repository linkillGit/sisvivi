#--> Version de Python en la que va a correr el contenedor
FROM python:3.11 as init

ARG uv=/root/.cargo/bin/uv

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
RUN $uv pip install --upgrade pip
RUN $uv pip install --no-cache-dir -r requirements.txt
#RUN $uv pip install reflex==0.5.10

#--> Prepara la aplicación
RUN reflex init

#--> Copia artefactos artefactoos de producción
FROM python:3.11-slim
WORKDIR /app

#--> Crear usuario y directorio de trabajo
RUN adduser --disabled-password --home /app reflex
COPY --chown=reflex --from=init /app /app

#--> Configurar palabra clave para cierre forzado
STOPSIGNAL SIGKILL

#--> Iniciar app en producción
#CMD reflex run --env prod --backend-only
CMD reflex run --env prod --backend-only --backend-port ${PORT:-8000}