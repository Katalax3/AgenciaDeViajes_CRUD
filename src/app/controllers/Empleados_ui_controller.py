from PySide6.QtWidgets import QMainWindow
from src.app.ui import Ui_PEmpleado

class VentanaEmpleado(QMainWindow):
    def __init__(self, datos_usuario: dict):
        super().__init__()
        self.ui = Ui_PEmpleado()
        self.ui.setupUi(self)
        
        self.usuario = datos_usuario