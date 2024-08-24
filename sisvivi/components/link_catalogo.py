import reflex as rx
import sisvivi.styles.styles as style

def link_catalogo(ttittle: str, tbody: str, pag: str) -> rx.Component:
  return rx.link(
    rx.button(
      rx.hstack(
        rx.icon(
          tag="arrow_right",
          width=style.Spacer.BIG.value,
          height=style.Spacer.BIG.value,
          margin=style.Spacer.MEDIUM.value,
          ),
        rx.vstack(
          rx.text(
            ttittle,  
            style=style.button_tittle_style,
          ),
          rx.text(
            tbody,
            style=style.button_body_style,
            text_align="start",
          ),
          spacing=style.Spacer.SMALL.value,
          margin="0",
        ),
        align="center",
      ),
    ),
    href=pag,
    is_external=True,
    width="100%"
  )