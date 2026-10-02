from PySide6.QtWidgets import QMainWindow
from src.app.ui import Ui_MenuOpciones

class MenuOpciones(QMainWindow):
    def __init__(self, rol: str):
        super().__init__()
        self.ui = Ui_MenuOpciones()
        self.ui.setupUi(self)
        
        self.rol = rol