from dataclasses import dataclass

@dataclass
class Clientes:
    idclientes: int
    nombre: str
    paterno: str
    materno: str
    telefono: str
    email: str
    contrasena: str

    def __post_init__(self):
        if not len(self.contrasena) >= 8:
            raise ValueError("Error: Ingrese una contraseña mayor a 8 caracteres")