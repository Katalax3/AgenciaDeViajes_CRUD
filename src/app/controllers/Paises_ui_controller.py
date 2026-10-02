from PySide6.QtWidgets import QWidget
from src.app.ui import Ui_VentanaPaises

class VentanaPais(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_VentanaPaises()
        self.ui.setupUi(self)