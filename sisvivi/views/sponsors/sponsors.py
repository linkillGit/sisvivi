import reflex as rx
import sisvivi.styles.styles as style
from sisvivi.components.link_sponsor import link_sponsor as sponsor

def sponsors() -> rx.Component:
  return rx.hstack(
    sponsor("ubv_logo.png","http://www.ubv.edu.ve/","UBV"),
    sponsor("orinoquia_logo.jpg","https://orinoquia.com.ve/","Orinoquia"),
    justify="center",
    margin_top=style.Spacer.EXTRABIG.value,
  )