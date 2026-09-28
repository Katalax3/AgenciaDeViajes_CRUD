import sys
from PySide6.QtWidgets import QApplication
from src.app.controllers import VentanaLogin

if __name__ == "__main__":
    app = QApplication(sys.argv)

    Ventana_Login = VentanaLogin()
    Ventana_Login.show()

    sys.exit(app.exec())