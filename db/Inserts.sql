INSERT INTO users (name, email)
VALUES ('Alice', 'alice@example.com');

INSERT INTO users (name, email)
VALUES ('Bob', 'bob@example.com');

INSERT INTO users (name, email)
VALUES ('Carlos', 'carlos@example.com');


INSERT INTO articles (user_id, title, text)
VALUES (1, 'Primer Post', 'Este es el contenido del primer artículo del blog.');

INSERT INTO articles (user_id, title, text)
VALUES (2, 'Receta de cocina', 'Hoy compartiré una receta muy fácil y deliciosa.');

INSERT INTO articles (user_id, title, text)
VALUES (1, 'Tips de programación', 'Buenas prácticas para escribir código limpio.');

INSERT INTO tags (name, url)
VALUES ('Python', 'http://tags.com/python');

INSERT INTO tags (name, url)
VALUES ('Cocina', 'http://tags.com/cocina');

INSERT INTO tags (name, url)
VALUES ('Tips', 'http://tags.com/tips');


INSERT INTO categories (name, url)
VALUES ('Tecnología', 'http://cat.com/tecnologia');

INSERT INTO categories (name, url)
VALUES ('Gastronomía', 'http://cat.com/gastronomia');

INSERT INTO categories (name, url)
VALUES ('Educación', 'http://cat.com/educacion');


-- El primer post tiene los tags Python y Tips
INSERT INTO article_tags (article_id, tag_id) VALUES (1, 1);
INSERT INTO article_tags (article_id, tag_id) VALUES (1, 3);

-- La receta de cocina tiene el tag Cocina
INSERT INTO article_tags (article_id, tag_id) VALUES (2, 2);


-- El primer post en Tecnología
INSERT INTO article_categories (article_id, category_id) VALUES (1, 1);

-- La receta de cocina en Gastronomía
INSERT INTO article_categories (article_id, category_id) VALUES (2, 2);

-- Tips de programación en Tecnología y Educación
INSERT INTO article_categories (article_id, category_id) VALUES (3, 1);
INSERT INTO article_categories (article_id, category_id) VALUES (3, 3);


select *FROM articles
