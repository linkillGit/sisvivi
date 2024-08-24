import reflex as rx
from enum import Enum

# Constantes


# Medidas

class Spacer(Enum):
  SMALL="0.5em"
  MEDIUM="0.8em"
  DEFAULT="1EM"
  BIG="2em"
  EXTRABIG="8EM"

# Colores

class Color(Enum):
  contraste_dia="#8e0242",
  contraste_noche="#ff0477",
  #fondo_dia="lightgray",
  fondo_dia="white",
  fondo_noche="#"

# Estilos Base

BASE_STYLE = {
  rx.button: {
    "width": "100%",
    "height": "100%",
    "border_radius": "0",
    "padding": Spacer.SMALL.value,
    "display": "block",
    "background_color": Color.contraste_dia.value,
    "_hover": {
      "opacity": "0.7",
      "text_decoration": "none",
    },
  },
}

tittle_style = dict(
  #width = "100%",
  #size = "lg",
  color=Color.contraste_dia
)

button_tittle_style = dict(
  font_size = Spacer.DEFAULT.value,
  font_weight = "bold",
)

button_body_style = dict(
  font_size = Spacer.MEDIUM.value
)

#margin-block-start: 1em;