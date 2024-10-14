import reflex as rx
def contar_tareas_por_estado(tareas):
 # Esta función recibe una lista de tareas y cuenta cuántas hay por estado
 contadores = {} # Diccionario para almacenar el conteo de tareas por estado
 for tarea in tareas:
 estado = tarea["estado"] # Obtiene el estado de la tarea actual
 if estado in contadores:
 # Si el estado ya está en el diccionario, incrementa el contador
 contadores[estado] += 1
 else:
 # Si el estado no está en el diccionario, lo agrega con un contador inicial de 1
 contadores[estado] = 1
 return contadores # Devuelve el diccionario con los contadores
def index():
 # Función principal que renderiza el contenido del tablero Kanban
 contadores = contar_tareas_por_estado(todas_las_tareas) # Llama a la función para contar tareas por estado

 return rx.div(
 # Aquí se agregarían las columnas del tablero Kanban

 # Muestra la cantidad de tareas en cada estado en elementos separados
 rx.div(f"Pendientes: {contadores.get('Pendiente', 0)}"), # Muestra el contador de tareas pendientes
 rx.div(f"En Progreso: {contadores.get('En Progreso', 0)}"), # Muestra el contador de tareas en progreso
 rx.div(f"Completadas: {contadores.get('Completada', 0)}") # Muestra el contador de tareas completadas
 )