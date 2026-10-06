from contextlib import contextmanager
from functools import wraps
from psycopg.rows import dict_row
from database.connection import get_db_connection


@contextmanager
def default_db_cursor():
    with get_db_connection() as conn:
        with conn.cursor(row_factory=dict_row) as cur:
            yield conn, cur

def with_db(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        with self.db_cursor() as (conn, cur):
            return func(self, *args, cur=cur, conn=conn, **kwargs)
    return wrapper

class BaseService:
    @contextmanager
    def db_cursor(self):
        with default_db_cursor() as (conn, cur):
            yield conn, cur