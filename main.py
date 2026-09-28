import sys
from PySide6.QtWidgets import QApplication, QDialog

from src.app.ui.PopGuardado_ui import Ui_Dialog

class Login(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Login()
    ventana.show()

    sys.exit(app.exec())