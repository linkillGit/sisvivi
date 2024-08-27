##############################
####### IMPORTACIONES ########
##############################

#--->Libreria principal
import reflex as rx

#--->Configuraciones del reflex
from rxconfig import config

#--->Componentes
from sisvivi.components.navbar import navbar
from sisvivi.components.saludo import saludo
from sisvivi.components.footer import footer

#--->Vistas
from sisvivi.views.catalogo.catalogo import catalogo
from sisvivi.views.sponsors.sponsors import sponsors

#--->Estilos
import sisvivi.styles.styles as style

#---> Utilidades
import sisvivi.utils as utils

#---> Rutas
from sisvivi.routes import Route
    
##############################
########### PÁGINA ###########
##############################

#--->Pagina del menú
@rx.page(
  route=Route.INDEX.value,
  title=utils.menu_title,
  description=utils.menu_description,
  image=utils.preview,
)
def index() -> rx.Component:
  return rx.box(
    utils.lang(),
    navbar(),
    saludo(),
    #contador(),
    catalogo(),
    sponsors(),
    footer(),
    background_color=style.Color.fondo_dia.value
  )