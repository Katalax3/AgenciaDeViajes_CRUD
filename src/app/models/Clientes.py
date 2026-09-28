from dataclasses import dataclass
from PySide6.QtWidgets import QMessageBox

@dataclass
class Clientes:
    id: int
    nombre: str
    paterno: str
    materno: str
    telefono: str
    email: str
    contrasena: str

    def __post_init__(self):
        if not len(self.contrasena) >= 8:
            QMessageBox.critical(None, "Mensage de error", "Error: Ingrese una contraseña mayor a 8 caracteres")