"""Capa de servicio de la tabla `pais`.

Aquí viven las REGLAS DE NEGOCIO (validaciones, no repetir ID, no borrar un
país con ciudades...). No usa nada de PySide6: si algo está mal lanza un
`PaisError` y el controller decide cómo mostrarlo.

Flujo:  Ventana (controller)  ->  Pais_service  ->  Pais_dal  ->  BD
"""
import re

from src.app.dal import Pais_dal as dal

# ---------- constantes ----------
# solo letras, acentos y espacios
PATRON_NOMBRE = r"[A-Za-zÁÉÍÓÚÜáéíóúüÑñ ]+"
ID_MAX = 999999999      # NUMERIC(9)
NOMBRE_MAX = 30


class PaisError(Exception):
    """Error de validación / regla de negocio.

    Lleva un `titulo` y un `mensaje` listos para ponerlos en un QMessageBox.
    """

    def __init__(self, titulo: str, mensaje: str):
        super().__init__(mensaje)
        self.titulo = titulo
        self.mensaje = mensaje


# ---------- validaciones ----------
def validar_id(id_pais) -> int:
    """Regresa el ID como int, o lanza PaisError si no es válido."""
    try:
        id_int = int(str(id_pais).strip())
    except ValueError:
        raise PaisError("ID inválido", "El ID debe ser un número entero")
    if not 1 <= id_int <= ID_MAX:
        raise PaisError("ID inválido", f"El ID debe estar entre 1 y {ID_MAX}")
    return id_int


def validar_nombre(nombre: str) -> str:
    """Regresa el nombre limpio, o lanza PaisError si no es válido."""
    nombre = (nombre or "").strip()
    if not nombre:
        raise PaisError("Campo vacío", "El nombre no puede estar vacío")
    if len(nombre) > NOMBRE_MAX:
        raise PaisError(
            "Nombre inválido", f"El nombre puede tener máximo {NOMBRE_MAX} caracteres"
        )
    if not re.fullmatch(PATRON_NOMBRE, nombre):
        raise PaisError("Nombre inválido", "El nombre solo puede tener letras")
    return nombre


# ---------- consultas ----------
def listar() -> list[dict]:
    """Todos los países ordenados por ID."""
    return dal.listar_paises()


def buscar(id_pais) -> dict | None:
    """Busca un país. Regresa None si no existe (no lanza error)."""
    return dal.obtener_pais(validar_id(id_pais))


def obtener(id_pais) -> dict:
    """Como `buscar`, pero lanza PaisError si el país no existe."""
    id_int = validar_id(id_pais)
    pais = dal.obtener_pais(id_int)
    if pais is None:
        raise PaisError("No existe", f"No hay ningún país con el ID {id_int}")
    return pais


# ---------- operaciones ----------
def crear(id_pais, nombre) -> None:
    """INSERT: valida los datos y que el ID no esté repetido."""
    if not str(id_pais).strip() or not (nombre or "").strip():
        raise PaisError("Campos vacíos", "Llena el ID y el nombre del país")

    id_int = validar_id(id_pais)
    nombre = validar_nombre(nombre)

    if dal.obtener_pais(id_int):
        raise PaisError(
            "Ya existe",
            f"Ya existe un país con el ID {id_int}. "
            "Usa el botón Modificar si quieres cambiarlo.",
        )
    dal.insertar_pais(id_int, nombre)


def modificar(id_pais, nombre) -> None:
    """UPDATE: valida el nombre y que el país exista."""
    pais = obtener(id_pais)             # lanza PaisError si no existe
    nombre = validar_nombre(nombre)
    dal.actualizar_pais(pais["idpais"], nombre)


def validar_eliminacion(id_pais) -> dict:
    """Revisa que el país exista y NO tenga ciudades.

    Regresa el país (para mostrar su nombre en la confirmación).
    """
    pais = obtener(id_pais)
    ciudades = dal.contar_ciudades(pais["idpais"])
    if ciudades > 0:
        raise PaisError(
            "No se puede eliminar",
            f"{pais['nombre']} tiene {ciudades} ciudad(es) registrada(s). "
            "Primero elimina sus ciudades.",
        )
    return pais


def eliminar(id_pais) -> None:
    """DELETE: vuelve a validar por seguridad y elimina."""
    pais = validar_eliminacion(id_pais)
    dal.eliminar_pais(pais["idpais"])
