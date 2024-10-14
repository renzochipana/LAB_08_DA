import reflex as rx
# Definir el estado local
class EstadoContador(rx.State):
 conteo: int = 0 # Estado inicializado en 0
 # Función para incrementar el conteo
 def incrementar(self):
 self.conteo += 1
 # Función para disminuir el conteo
 def disminuir(self):
 self.conteo -= 1
# Componente Contador
def contador():
 return rx.fragment(
 rx.hstack(
 rx.button("Incrementar", on_click=EstadoContador.incrementar),
 rx.text(EstadoContador.conteo),
 rx.button("Disminuir", on_click=EstadoContador.disminuir),
 )
 )
