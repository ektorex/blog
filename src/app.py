# src/app.py
from flask import Flask, render_template, request, redirect, url_for
from blog_db import crear_usuario, crear_articulo, crear_comentario
from blog_db import listar_articulos_usuario, listar_comentarios_articulo
from db_connection import get_connection
import random

app = Flask(__name__)

@app.route("/")
def landing():
    
    conn = get_connection()
    articles = []
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT article_id,title,name,text from articles a join users u on a.user_id = u.user_id ")
        articles = cursor.fetchall()


        clean_rows = []
        for row in articles:
            article_id, title, name, text = row
            text = str(text.read()) if hasattr(text, "read") else str(text)
            clean_rows.append((article_id, title, name, text))


        cursor.close()
        conn.close()
        selected = random.sample(clean_rows, 1)
    return render_template("landing.html", articles = selected)





# -------------------------------
# Home con usuarios
# -------------------------------
@app.route("/users", methods=["GET"])
def home():
    conn = get_connection()
    usuarios = []
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT user_id, name, email FROM users")
        usuarios = cursor.fetchall()
        cursor.close()
        conn.close()
    return render_template("index.html", usuarios=usuarios)
@app.route("/usuarios/nuevo", methods=["POST"])
def crear_usuario_form():
    nombre = request.form["name"]
    email = request.form["email"]
    crear_usuario(nombre, email)
    return redirect(url_for("home"))

# -------------------------------
# Usuarios
# -------------------------------
# -------------------------------
# Artículos
# -------------------------------
@app.route("/usuarios/<int:user_id>", methods=["GET"])
def ver_articulos_usuario(user_id):
    articulos = listar_articulos_usuario(user_id)
    conn = get_connection()
    usuario = "Usuario"
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM users WHERE user_id=:id", id=user_id)
        row = cursor.fetchone()
        if row:
            usuario = row[0]
        cursor.close()
        conn.close()
    return render_template("user_articles.html", articulos=articulos, usuario=usuario, user_id=user_id)

@app.route("/usuarios/<int:user_id>/articulos/nuevo", methods=["POST"])
def crear_articulo_form(user_id):
    titulo = request.form["title"]
    texto = request.form["text"]
    crear_articulo(user_id, titulo, texto)
    return redirect(url_for("ver_articulos_usuario", user_id=user_id))

# -------------------------------
# Comentarios
# -------------------------------
@app.route("/articulos/<int:article_id>", methods=["GET"])
def ver_comentarios_articulo(article_id):
    comentarios = listar_comentarios_articulo(article_id)
    return render_template("article_comments.html", comentarios=comentarios, article_id=article_id)

@app.route("/articulos/<int:article_id>/comentarios/nuevo", methods=["POST"])
def crear_comentario_form(article_id):
    user_id = request.form["user_id"]
    nombre = request.form["name"]
    url = request.form["url"]
    crear_comentario(article_id, user_id, nombre, url)
    return redirect(url_for("ver_comentarios_articulo", article_id=article_id))

# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)

