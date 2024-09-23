import reflex as rx
import sisvivi.styles.styles as style

def saludo(github_act: str) -> rx.Component:
  return rx.hstack(
    rx.avatar(
      fallback="SV",
      radius="none",
      color_scheme="crimson",
      variant="soft",
      size="7",
      ),
    rx.vstack(
      rx.text(
        rx.text.span(
          "Hola",
          weight="bold",
          size="8",
        ),
        " soy ",
        rx.text.span(
          "SISVIVI",
          color=style.Color.contraste_dia.value,
        ),
        ", tu ",
        rx.text.span(
          "Sis",
          color=style.Color.contraste_dia.value,
        ),
        "tema de ",
        rx.text.span(
          "Vi",
          color=style.Color.contraste_dia.value,
        ),
        "sión ",
        rx.text.span(
          "V",
          color=style.Color.contraste_dia.value,
        ),
        "ehicular ",
        rx.text.span(
          "I",
          color=style.Color.contraste_dia.value,
        ),
        "nteligente, aquí podrás ir probando las distintas funciones que voy a implementar a medida que se vayan desarrollando.",
#        color="grey",
        size="7",
        font_family="Space Grotesk",
      ),
      rx.text(
        github_act,
      ),
      color="grey",
    ),
    padding_x=style.Spacer.DEFAULT.value,
    padding_y=style.Spacer.BIG.value,
    align="center",
  )