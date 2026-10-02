class AuthDAL:
    def __init__(self, cursor):
        self.cur = cursor
    def obtener_usuario_por_identificador(self, identificador: str, rol: str) -> dict | None:
        tabla = "clientes" if rol == "clientes" else "empleados"

        query = f"SELECT * FROM {tabla} WHERE (nombre = %(id)s OR correo = %(id)s)"

        self.cur.execute(query, {"id": identificador})
        return self.cur.fetchone()