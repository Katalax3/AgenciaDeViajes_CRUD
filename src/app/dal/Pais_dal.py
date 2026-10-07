from psycopg.rows import dict_row
from database.connection import get_db_connection

#todos los paises ordenados po ID
def listar_paises():
    with get_db_connection() as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute("SELECT idpais, nombre FROM pais ORDER BY idpais")
            return cur.fetchall()

#revisa si un ID ya existe
def obtener_pais(id_pais):
    with get_db_connection() as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            cur.execute(
                "SELECT idpais, nombre FROM pais WHERE idpais = %s", (id_pais,)
            )
            return cur.fetchone()

#No dejar borrar un país que ya tiene ciudades
def contar_ciudades(id_pais):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM ciudad WHERE idpais = %s", (id_pais,))
            return cur.fetchone()[0] #type: ignore

#insert
def insertar_pais(id_pais, nombre):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO pais (idpais, nombre) VALUES (%s, %s)",
                (id_pais, nombre),
            )

#update
def actualizar_pais(id_pais, nombre):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE pais SET nombre = %s WHERE idpais = %s", (nombre, id_pais)
            )

#delete
def eliminar_pais(id_pais):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM pais WHERE idpais = %s", (id_pais,))