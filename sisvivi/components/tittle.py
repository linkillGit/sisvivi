import reflex as rx
import sisvivi.styles.styles as style

def tcatalogo(text: str) -> rx.Component:
  return rx.heading(
    text,
    size = "9",
    style=style.tittle_style,
  )