##########################
########LIBRERIAS#########
##########################

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
    
##########################
########PAGINAS###########
##########################

#--->Pagina del menú
@rx.page(route="/",title="SISVIVI | Sistema de Visión Vehicular Inteligente",description="Catalogo de funciones")
def index() -> rx.Component:
  return rx.box(
    navbar(),
    saludo(),
    #contador(),
    catalogo(),
    sponsors(),
    footer(),
    background_color=style.Color.fondo_dia.value
  )

#--->Pag temporal
@rx.page(route="/uno",title="Uno")
def index() -> rx.Component:
  return rx.box(
    navbar(),
    rx.text(
      "Este es el espacio Nº1",
      text_aling="center"
    ),
    footer()
  )

#--->Pag temporal
@rx.page(route="/dos",title="Dos")
def index() -> rx.Component:
  return rx.box(
    navbar(),
    rx.text(
      "Este es el espacio Nº2",
      text_aling="center"
    ),
    footer()
  )

#--->Pag temporal
@rx.page(route="/tres",title="Tres")
def index() -> rx.Component:
  return rx.box(
    navbar(),
    rx.text(
      "Este es el espacio Nº3",
      text_aling="center"
    ),
    footer()
  )

#--->Pag temporal
@rx.page(route="/cuatro",title="Cuatro")
def index() -> rx.Component:
  return rx.box(
    navbar(),
    rx.text(
      "Este es el espacio Nº4",
      text_aling="center"
    ),
    footer()
  )
  
##########################
#######APLICACION#########
##########################

app = rx.App(
  style=style.BASE_STYLE,
  stylesheets=[
    "https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300..700&display=swap",
  ],
)
#Tutorial
#5:32:00