from contextlib import contextmanager
from psycopg_pool import ConnectionPool
from config import settings

try:
    db_pool = ConnectionPool(
        min_size=1,
        max_size=10,
        kwargs={
            **settings.DB_CONFIG
        }
    )
except Exception as e:
    print(f"Error al conectar con la base de datos: {e}")
    db_pool = None

@contextmanager
def get_db_connection():
    if db_pool is None:
        raise Exception("El pool de conexiones no está inicializado.")
    
    conn = db_pool.getconn()
    try:
        yield conn
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        db_pool.putconn(conn)

def close_pool():
    global db_pool
    if db_pool is not None and not db_pool.closed:
        db_pool.close()
        print("Pool de conexiones cerrado de manera segura.")