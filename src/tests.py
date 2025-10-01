# src/test_blog_db.py
from blog_db import crear_usuario, crear_articulo, crear_comentario
from blog_db import listar_articulos_usuario, listar_comentarios_articulo

if __name__ == "__main__":
    # Crear usuario
    crear_usuario("Karen", "karen@example.com")

#     Crear artículo de usuario 1
    crear_articulo(1, "Nuevo artículo", "Contenido de prueba en Oracle")

    # Crear comentario
    crear_comentario(1, 2, "Comentario de Bob en artículo 1", "http://bob.com")

    # Listar artículos de usuario 1
    print("📌 Artículos de usuario 1:")
    for row in listar_articulos_usuario(1):
        print(row)

    # Listar comentarios de artículo 1
    print("\n📌 Comentarios del artículo 1:")
    for row in listar_comentarios_articulo(1):
        print(row)

