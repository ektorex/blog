from db_connection import get_connection
import cx_Oracle

# Procedimientos (INSERT, UPDATE)
def crear_usuario(nombre, email):
    conn = get_connection()
    if not conn: return
    try:
        cursor = conn.cursor()
        cursor.callproc("crear_usuario", [nombre, email])
        conn.commit()
        print(f"✅ Usuario {nombre} creado")
    except Exception as e:
        print("❌ Error crear_usuario:", e)
    finally:
        cursor.close()
        conn.close()


def crear_articulo(user_id, titulo, texto):
    conn = get_connection()
    if not conn: return
    try:
        cursor = conn.cursor()
        cursor.callproc("crear_articulo", [user_id, titulo, texto])
        conn.commit()
        print(f"✅ Artículo '{titulo}' creado")
    except Exception as e:
        print("❌ Error crear_articulo:", e)
    finally:
        cursor.close()
        conn.close()


def crear_comentario(article_id, user_id, nombre, url):
    conn = get_connection()
    if not conn: return
    try:
        cursor = conn.cursor()
        cursor.callproc("crear_comentario", [article_id, user_id, nombre, url])
        conn.commit()
        print("✅ Comentario creado")
    except Exception as e:
        print("❌ Error crear_comentario:", e)
    finally:
        cursor.close()
        conn.close()

# Funciones (Consultas)

def listar_articulos_usuario(user_id):
    conn = get_connection()
    if not conn: return []
    try:
        cursor = conn.cursor()
        out_cursor = cursor.var(cx_Oracle.CURSOR)
        cursor.callfunc("listar_articulos_usuario", out_cursor, [user_id])
        rows = out_cursor.getvalue().fetchall()

        # Convertir LOB a str aquí
        clean_rows = []
        for row in rows:
            article_id, title, pub_date, text = row
            text = str(text.read()) if hasattr(text, "read") else str(text)
            clean_rows.append((article_id, title, pub_date, text))

        return clean_rows
    except Exception as e:
        print("❌ Error listar_articulos_usuario:", e)
        return []
    finally:
        cursor.close()
        conn.close()



def listar_comentarios_articulo(article_id):
    conn = get_connection()
    if not conn: return []
    try:
        cursor = conn.cursor()
        out_cursor = cursor.var(cx_Oracle.CURSOR)
        cursor.callfunc("listar_comentarios_articulo", out_cursor, [article_id])
        return out_cursor.getvalue().fetchall()
    except Exception as e:
        print("❌ Error listar_comentarios_articulo:", e)
        return []
    finally:
        cursor.close()
        conn.close()

