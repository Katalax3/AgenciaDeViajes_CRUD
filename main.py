import sys
from PySide6.QtWidgets import QApplication
from src.app.controllers import VentanaLogin
from database.connection import close_pool

def main():
    app = QApplication(sys.argv)

    Ventana_Login = VentanaLogin()
    Ventana_Login.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    try:
        main()
    except:
        close_pool()