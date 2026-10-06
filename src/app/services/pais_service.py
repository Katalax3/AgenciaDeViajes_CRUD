from typing import List, Optional
from psycopg import Cursor, Connection
from app.services.base_service import BaseService, with_db 
from app.dal import BaseDAL
from app.models.Pais import Pais


class PaisService(BaseService):
    def __init__(self) -> None:
        self.dal = BaseDAL(table_name="pais", model_class=Pais)

    @with_db
    def listar(self, limit: int = 100, offset: int = 0, *, cur: Cursor, conn: Connection) -> List[Pais]:
        return self.dal.get_all(cur, limit=limit, offset=offset)

    @with_db
    def buscar_por_id(self, idpais: int, *, cur: Cursor, conn: Connection) -> Optional[Pais]:
        return self.dal.get_by_id(cur, id_value=idpais, id_column="idpais")

    @with_db
    def crear(self, idpais: str, nombre: str, *, cur: Cursor, conn: Connection) -> Pais | None:
        nombre = (nombre or "").strip()
        if not nombre:
            conn.rollback()
            raise ValueError("El nombre del país no puede estar vacío.")
        if len(nombre) > 100:
            conn.rollback()
            raise ValueError("El nombre es demasiado largo.")
        
        row = self.dal.create(cur, data={"idpais": idpais, "nombre": nombre})
        if not row:
            conn.rollback()
            raise ValueError("No se pudo crear el pais")
        conn.commit()
        return row

    @with_db
    def actualizar(self, idpais: int, nombre: str, *, cur: Cursor, conn: Connection) -> Pais:
        nombre = (nombre or "").strip()
        if not nombre:
            conn.rollback()
            raise ValueError("El nombre del país no puede estar vacío.")
        row = self.dal.update(cur, id_value=idpais, data={"nombre": nombre}, id_column="idpais")
        if row is None:
            conn.rollback()
            raise ValueError(f"No existe el país con id {idpais}.")
        conn.commit()
        return row

    @with_db
    def eliminar(self, idpais: int, *, cur: Cursor, conn: Connection) -> None:
        row = self.dal.delete(cur, id_value=idpais, id_column="idpais")
        if not row:
            conn.rollback()
            raise ValueError(f"No se pudo eliminar el país con id {idpais}.")
        conn.commit()