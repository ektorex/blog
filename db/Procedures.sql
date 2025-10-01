CREATE OR REPLACE PROCEDURE crear_usuario(
    p_name   IN VARCHAR2,
    p_email  IN VARCHAR2
) IS
BEGIN
    INSERT INTO users (name, email)
    VALUES (p_name, p_email);
END;
/

CREATE OR REPLACE PROCEDURE crear_articulo(
    p_user_id IN NUMBER,
    p_title   IN VARCHAR2,
    p_text    IN CLOB
) IS
BEGIN
    INSERT INTO articles (user_id, title, text)
    VALUES (p_user_id, p_title, p_text);
END;
/


CREATE OR REPLACE PROCEDURE crear_comentario(
    p_article_id IN NUMBER,
    p_user_id    IN NUMBER,
    p_name       IN VARCHAR2,
    p_url        IN VARCHAR2
) IS
BEGIN
    INSERT INTO comments (article_id, user_id, name, url)
    VALUES (p_article_id, p_user_id, p_name, p_url);
END;
/


CREATE OR REPLACE PROCEDURE asignar_tag_articulo(
    p_article_id IN NUMBER,
    p_tag_id     IN NUMBER
) IS
BEGIN
    INSERT INTO article_tags (article_id, tag_id)
    VALUES (p_article_id, p_tag_id);
END;
/


CREATE OR REPLACE PROCEDURE asignar_categoria_articulo(
    p_article_id   IN NUMBER,
    p_category_id  IN NUMBER
) IS
BEGIN
    INSERT INTO article_categories (article_id, category_id)
    VALUES (p_article_id, p_category_id);
END;
/


CREATE OR REPLACE FUNCTION listar_articulos_usuario(
    p_user_id IN NUMBER
) RETURN SYS_REFCURSOR IS
    v_cursor SYS_REFCURSOR;
BEGIN
    OPEN v_cursor FOR
        SELECT article_id, title, pub_date, text
        FROM articles
        WHERE user_id = p_user_id
        ORDER BY pub_date DESC;
    RETURN v_cursor;
END;
/


CREATE OR REPLACE FUNCTION listar_comentarios_articulo(
    p_article_id IN NUMBER
) RETURN SYS_REFCURSOR IS
    v_cursor SYS_REFCURSOR;
BEGIN
    OPEN v_cursor FOR
        SELECT comment_id, name, url, fecha_comentario
        FROM comments
        WHERE article_id = p_article_id
        ORDER BY fecha_comentario DESC;
    RETURN v_cursor;
END;
/

select * from articles


