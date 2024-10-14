import reflex as rx
class State(rx.State):
 def __init__(self):
 super().__init__() # Inicializa la clase base
 self.mostrar_solo_pendientes = False # Variable para controlar la visualización de tareas pendientes
 def mostrar_pendientes(self):
 # Método para cambiar el estado a mostrar solo las tareas pendientes
 self.mostrar_solo_pendientes = True
def tarjeta_tarea(tarea):
 # Función para renderizar una tarjeta de tarea
 return rx.div(
 tarea["titulo"], # Muestra el título de la tarea
 # ... puedes agregar otros detalles de la tarea aquí
 )
def columna_kanban(nombre, tareas, state):
 # Función para renderizar una columna en el tablero Kanban
 if state.mostrar_solo_pendientes:
 # Si se solicita mostrar solo las tareas pendientes, filtra la lista de tareas
 tareas = [t for t in tareas if t["estado"] == "Pendiente"]
 return rx.div(
 rx.heading(nombre), # Muestra el nombre de la columna como un encabezado
 rx.div(
 [tarjeta_tarea(tarea) for tarea in tareas] # Renderiza las tarjetas de tarea
 )
 )
def index(state):
 # Función principal para renderizar el contenido del tablero Kanban
 return rx.div(
 rx.button("Mostrar Pendientes", on_click=state.mostrar_pendientes), # Botón para mostrar solo las tareas pendientes
 columna_kanban("En Progreso", tareas_en_progreso, state), # Renderiza la columna de tareas en progreso
 columna_kanban("Completadas", tareas_completadas, state) # Renderiza la columna de tareas completadas
 )
# Crea una instancia del estado
state = State()