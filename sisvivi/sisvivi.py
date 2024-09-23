##############################
####### IMPORTACIONES ########
##############################

#---> Libreria principal
import reflex as rx

#---> Configuraciones del reflex
from rxconfig import config

#---> Estilos
import sisvivi.styles.styles as style

#---> Estados
from sisvivi.api.api import get_repo_updated_at

##############################
######### PÁGINAS ############
##############################

from sisvivi.pages.index import index
from sisvivi.pages.example import uno, dos, tres, cuatro

##############################
######## APLICACION ##########
##############################

app = rx.App(
  style=style.BASE_STYLE,
  stylesheets=[
    "https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300..700&display=swap",
  ],
)

##############################
######### API_RUTAS ##########
##############################

app.api.add_api_route("/repos/{owner}/{repo}/updated_at",get_repo_updated_at)