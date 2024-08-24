import reflex as rx

class State(rx.State):
  contar: int = 0

  def sumar(self):
    self.contar += 1

  def restar(self):
    self.contar -= 1

def contador() -> rx.Component:
  return rx.hstack(
    rx.button(
      "Restar",
      color_scheme="red",
      border_radius="1em",
      on_click=State.restar
    ),
    rx.heading(
      State.contar, 
      font_size="2em"
    ),
    rx.button(
      "Sumar",
      color_scheme="green",
      on_click=State.sumar
    ),
  )