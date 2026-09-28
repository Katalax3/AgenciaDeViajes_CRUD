from PySide6.QtWidgets import QMainWindow
from src.app.ui import Ui_PCliente

class VentanaCliente(QMainWindow):
    def __init__(self, datos_usuario: dict):
        super().__init__()
        self.ui = Ui_PCliente()
        self.ui.setupUi(self)
        
        self.usuario = datos_usuario