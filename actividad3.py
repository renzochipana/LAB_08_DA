import reflex as rx
class EstadoFormulario(rx.State):
 def __init__(self):
 super().__init__()
 self.nombre = ""
 self.email = ""
 self.mensaje = ""
 def enviar_formulario(self):
 if "@" not in self.email or "." not in self.email:
 rx.notify("Error: Dirección de correo electrónico no válida")
 else:
 rx.notify("Formulario enviado correctamente")
def formulario_contacto():
 return rx.fragment(
 rx.heading("Formulario de Contacto"),
 rx.form(
 rx.input(
 placeholder="Nombre",
 on_change=lambda valor: setattr(EstadoFormulario, "nombre", valor)
 ),
 rx.input(
 placeholder="Correo electrónico",
 on_change=lambda valor: setattr(EstadoFormulario, "email", valor)
 ),
 rx.textarea(
 placeholder="Mensaje",
 on_change=lambda valor: setattr(EstadoFormulario, "mensaje", valor)
 ),
 rx.button("Enviar", on_click=EstadoFormulario.enviar_formulario),
 ),
 )
@rx.page("/contacto", title="Contacto")
def pagina_contacto():
 return formulario_contacto()