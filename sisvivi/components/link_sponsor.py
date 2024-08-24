import reflex as rx
import sisvivi.styles.styles as style

def link_sponsor(img: str, url: str, text: str) -> rx.Component:
  return rx.link(
    rx.vstack(
      rx.image(
        height=style.Spacer.EXTRABIG.value,
        width="auto",
        src=img,
      ),
      rx.text(text,color="black",justify="center",),
      align="center",
    ),
    href=url,
    is_external=True,
  )