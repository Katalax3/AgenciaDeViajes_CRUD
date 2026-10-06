from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QAction
from src.app.ui import Ui_MenuOpciones
from .Paises_ui_controller import VentanaPais
from app.services.pais_service import PaisService
from app.dal import BaseDAL

class MenuOpciones(QMainWindow):
    def __init__(self, rol: str):
        super().__init__()
        self.ui = Ui_MenuOpciones()
        self.ui.setupUi(self)
        self.service = PaisService()
        self.rol = rol
        self.ui.menuBarMO.triggered.connect(self.SeleccionarVentanaTabla)

    def SeleccionarVentanaTabla(self, action):
        text = action.text()
        if text == 'Paises':
            self.siguiente_ventana = VentanaPais(self.service)
            self.siguiente_ventana.show()
