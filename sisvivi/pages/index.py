##############################
####### IMPORTACIONES ########
##############################

#---> Libreria principal
import reflex as rx

#---> Configuraciones del reflex
from rxconfig import config

#---> Componentes
from sisvivi.components.navbar import navbar
from sisvivi.components.saludo import saludo
from sisvivi.components.footer import footer

#---> Vistas
from sisvivi.views.catalogo.catalogo import catalogo
from sisvivi.views.sponsors.sponsors import sponsors

#---> Estilos
import sisvivi.styles.styles as style

#---> Utilidades
import sisvivi.utils as utils

#---> Rutas
from sisvivi.routes import Route

#---> Estados
from sisvivi.api.api import get_repo_updated_at

##############################
######### BACKEND ############
##############################

class IndexState(rx.State):
  
  github_ultima_conexion: str = "Fecha github por actualizar"
  
  async def github_consulta(self) -> str:
    self.github_ultima_conexion = await get_repo_updated_at("linkillGit","sisvivi")

##############################
########### PÁGINA ###########
##############################

#--->Pagina del menú
@rx.page(
  route=Route.INDEX.value,
  title=utils.menu_title,
  description=utils.menu_description,
  image=utils.preview,
  on_load=IndexState.github_consulta,
)
def index() -> rx.Component:
  return rx.box(
    utils.lang(),
    navbar(),
    saludo(github_act=IndexState.github_ultima_conexion),
    catalogo(),
    sponsors(),
    footer(),
    background_color=style.Color.fondo_dia.value
  )