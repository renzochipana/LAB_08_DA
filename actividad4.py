import reflex as rx
import httpx
async def obtener_datos_api():
 async with httpx.AsyncClient() as cliente:
 respuesta = await cliente.get("https://jsonplaceholder.typicode.com/posts")
 respuesta.raise_for_status()
 return respuesta.json()
class EstadoDatosAPI(rx.State):
 def __init__(self):
 super().__init__()
 self.datos = []
 async def cargar_datos(self):
 self.datos = await obtener_datos_api()
def mostrar_datos_api():
 return rx.fragment(
 rx.button("Cargar Datos", on_click=EstadoDatosAPI.cargar_datos),
 rx.ul([rx.li(dato["title"]) for dato in EstadoDatosAPI.datos]),
 )
@rx.page("/api", title="Consumo de API")
def pagina_api():
 return mostrar_datos_api()
