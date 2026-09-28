from database.connection import get_db_connection
from psycopg.rows import dict_row
from PySide6.QtWidgets import QMessageBox

def autenticar_usuario(identificador: str, rol: str, contrasena: str) -> dict | None:
    tabla = "clientes" if rol == "clientes" else "empleados"

    query = f"SELECT * FROM {tabla} WHERE (nombre = %(id)s OR correo = %(id)s)"

    try:
        with get_db_connection() as conn:
            with conn.cursor(row_factory=dict_row) as cur:
                cur.execute(query, {"id": identificador})
                usuario = cur.fetchone()

            if usuario:
                if usuario["contrasena"] == contrasena:
                    return usuario

    except Exception as e:
        QMessageBox.critical(None, "Mensaje de error", f"Error al conectar o consultar la BD: {e}")