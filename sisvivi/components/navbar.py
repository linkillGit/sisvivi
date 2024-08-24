import reflex as rx

import sisvivi.styles.styles as style

def navbar() -> rx.Component:
  return rx.desktop_only(
    rx.hstack(
      rx.hstack(
        
        rx.heading("SISVIVI"),
      ),
      rx.hstack(
        rx.switch(default_checked=True,color_scheme="ruby",
        variant="soft"),
        spacing="2",
      ),
      justify="between",
      align_items="center",
      width="100%",
    ),
    position="sticky",
    width="100%",
    top="0",
    #bg="lightgray", #8e0242
    background_color="#8e0242",
    
    padding_x=style.Spacer.DEFAULT.value,
    padding_y=style.Spacer.SMALL.value,
    z_index="999",
  )

