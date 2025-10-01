import cx_Oracle
from db_config import DB_CONFIG

def get_connection():
    try:
        conn = cx_Oracle.connect(
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            dsn=DB_CONFIG["dsn"],
            encoding=DB_CONFIG["encoding"]

        )
        print("Conexion exitosa")
        return conn
    except cx_Oracle.Error as e:
        print("Error al conectar:",e)
        return NONE


