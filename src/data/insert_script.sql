use bd_py_mysql;

-- crear la tabla de usuarios id,username,name,password
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);


-- insertar un usuario
INSERT INTO users (id, username, name, password) VALUES (1, 'usuario_prueba@gmail.com', 'Usuario Prueba', 'test_123');