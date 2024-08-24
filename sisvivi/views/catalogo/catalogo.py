import reflex as rx

from sisvivi.components.link_catalogo import link_catalogo
from sisvivi.components.tittle import tcatalogo
import sisvivi.styles.styles as style

def catalogo() -> rx.Component:
  return rx.container(
    rx.hstack(
      rx.vstack(
        tcatalogo("Funciones"),
        rx.image(src="img_catalogo.jpeg",opacity="0.8"),
        width="58%",
        align= "center",
      ),
      rx.vstack(
        link_catalogo("Opción 1","Esta es la primera función","/uno"),
        link_catalogo("Opción 2","Esta es la segunda función","/dos"),
        link_catalogo("Opción 3","Esta es la tercera función","/tres"),
        link_catalogo("Opción 4","Esta es la cuarta función","/cuatro"),
        link_catalogo("Opción 1","Esta es la primera función","/uno"),
        link_catalogo("Opción 2","Esta es la segunda función","/dos"),
        link_catalogo("Opción 3","Esta es la tercera función","/tres"),
        link_catalogo("Opción 4","Esta es la cuarta función","/cuatro"),
        width="40%",
        padding_top=style.Spacer.BIG.value,
      ),
      #spacing="2",
      wrap="wrap",
      justify = "center",
      width="100%",
    ),
    padding_x=style.Spacer.DEFAULT.value,
    margin_y=style.Spacer.BIG.value,
    width="100%",
  )


