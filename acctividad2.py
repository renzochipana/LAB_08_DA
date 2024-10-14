import reflex as rx
class EstadoTareas(rx.State):
 tareas: list = ["Tarea 1", "Tarea 2"]
 def agregar_tarea(self, nueva_tarea: str):
 if nueva_tarea:
 self.tareas.append(nueva_tarea)
def lista_tareas():
 return rx.fragment(
 rx.heading("Lista de Tareas"),
 rx.ul([rx.li(tarea) for tarea in EstadoTareas.tareas]),
 )
def agregar_tarea():
 nueva_tarea = rx.var("")
 return rx.fragment(
 rx.input(placeholder="Agregar tarea...", value=nueva_tarea, on_change=lambda e: nueva_tarea.set(e.target.value)),
 rx.button("Agregar", on_click=lambda: EstadoTareas.agregar_tarea(nueva_tarea.get()))
 )
def app():
 return rx.fragment(
 agregar_tarea(),
 lista_tareas()
 )