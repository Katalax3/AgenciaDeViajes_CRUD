import sys
from PySide6.QtWidgets import QDialog, QMessageBox
from src.app.ui import Ui_Login
from src.app.controllers import VentanaCliente, VentanaEmpleado
from src.app.dal.auth_dal import autenticar_usuario

class VentanaLogin(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Login()
        self.ui.setupUi(self)

        self.ui.BCliente.setCheckable(True)
        self.ui.BEmpleado.setCheckable(True)
        self.ui.buttonGroup.setExclusive(True)
        self.ui.BCliente.setChecked(True)

        
        self.ui.Ingresar.clicked.connect(self.procesar_login)

    def obtener_rol(self) -> str:
            if self.ui.BCliente.isChecked():
                 return "clientes"
            return "empleados"

    def siguiente_ventana(self, rol: str, usuario: dict):
        if rol == "clientes":
              self.ventana_principal = VentanaCliente(datos_usuario=usuario)
        else:
             self.ventana_principal = VentanaEmpleado(datos_usuario=usuario)

        self.ventana_principal.show()

        self.close()
                        
    def procesar_login(self):
     identificador = self.ui.EUsuarioCorreo.text().strip()
     contrasena = self.ui.EContrasena.text().strip()
     rol = self.obtener_rol()

     if not identificador or not contrasena:
          QMessageBox.warning(self, "Campos Vacios", "Por favor ingrese su usuario/correo y contraseña")
          return

     usuario = autenticar_usuario(identificador, rol, contrasena)

     if usuario:
          self.siguiente_ventana(rol, usuario)
     else:
          QMessageBox.critical(self, "Mensaje de error", "Credenciales incorrectas o el usuario no existe")