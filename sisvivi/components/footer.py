import reflex as rx
import datetime
import sisvivi.styles.styles as style

def footer_item(text: str) -> rx.Component:
  return rx.text(text, size="3")


def footer_items_1() -> rx.Component:
  return rx.flex(
    rx.heading(
      "ORINOQUIA", size="4", weight="bold", as_="h3"
    ),
    footer_item("Klaus"),
    footer_item("Pedro"),
    spacing="4",
    text_align=["center", "center", "start"],
    flex_direction="column",
  )

def footer_items_2() -> rx.Component:
  return rx.flex(
    rx.heading(
      "INSTRUCTORES", size="4", weight="bold", as_="h3"
    ),
    footer_item("Javier Torrealva"),
    footer_item("María Veloz"),
    spacing="4",
    text_align=["center", "center", "start"],
    flex_direction="column",
  )

def footer_items_3() -> rx.Component:
  return rx.flex(
    rx.heading(
      "DESARROLLADORES", size="4", weight="bold", as_="h3"
    ),
    footer_item("Mairet Villalva"),
    footer_item("Eliezer Gómez"),
    footer_item("Leonel Román"),
    spacing="4",
    text_align=["center", "center", "start"],
    flex_direction="column",
  )


def footer() -> rx.Component:
  return rx.el.footer(
    rx.vstack(
      rx.flex(
        footer_items_1(),
        footer_items_2(),
        footer_items_3(),
        justify="between",
        spacing="4",
        flex_direction=["column", "column", "row"],
        width="100%",
      ),
      rx.divider(),
      rx.flex(
        rx.hstack(
          rx.avatar(
            fallback="SV",
            radius="none",
            color_scheme="crimson",
            variant="solid",
            ),
          
          rx.text(
            f"SISVIVI 2023-{datetime.date.today().year} Proyecto Universitario de Informática",
            size="3",
            white_space="nowrap",
            weight="medium",
          ),
          spacing="2",
          align="center",
          justify_content=[
            "center",
            "center",
            "start",
          ],
          width="100%",
        ),
        
        spacing="4",
        flex_direction=["column", "column", "row"],
        width="100%",
      ),
      spacing="5",
      width="100%",
    ),
    width="100%",
    padding="1em",
    margin_top="4em",
    border_top="solid 2px",
    color=style.Color.contraste_dia.value,
    background_color="lightgray",
  )
