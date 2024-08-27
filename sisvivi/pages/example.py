##############################
####### IMPORTACIONES ########
##############################

#--->Libreria principal
import reflex as rx

#--->Configuraciones del reflex
from rxconfig import config

#--->Componentes
from sisvivi.components.navbar import navbar
from sisvivi.components.footer import footer

#--->Estilos
import sisvivi.styles.styles as style

#---> Utilidades
import sisvivi.utils as utils

##############################
########### PÁGINA ###########
##############################

@rx.page(route="/uno",title="Uno")
def uno() -> rx.Component:
  return rx.box(
    utils.lang(),
    navbar(),
    rx.text(
      "Este es el espacio Nº1",
      text_aling="center"
    ),
    footer()
  )

#--->Pag temporal
@rx.page(route="/dos",title="Dos")
def dos() -> rx.Component:
  return rx.box(
    utils.lang(),
    navbar(),
    rx.text(
      "Este es el espacio Nº2",
      text_aling="center"
    ),
    footer()
  )

#--->Pag temporal
@rx.page(route="/tres",title="Tres")
def tres() -> rx.Component:
  return rx.box(
    utils.lang(),
    navbar(),
    rx.text(
      "Este es el espacio Nº3",
      text_aling="center"
    ),
    footer()
  )

#--->Pag temporal
@rx.page(route="/cuatro",title="Cuatro")
def cuatro() -> rx.Component:
  return rx.box(
    utils.lang(),
    navbar(),
    rx.text(
      "Este es el espacio Nº4",
      text_aling="center"
    ),
    footer()
  )