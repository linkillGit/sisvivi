import reflex as rx

#---> Común

def lang() -> rx.Component:
  return rx.script("document.documentElement.lang='es'")

preview = "/enconstruccion.jpeg"

#---> Index
index_title = "SISVIVI | Sistema de Visión Vehicular Inteligente"
index_description = "Proyecto Universitario de Automatización de Sistema de Visión Vehicular Inteligente"

#---> Menú
menu_title = "SISVIVI | Menú"
menu_description = "Catalogo de funciones"

#---> Pag en construcción
construction_title = "SISVIVI | En costrucción"
construction_description = "Esta página es de pruebas o está en construcción"


route="/"