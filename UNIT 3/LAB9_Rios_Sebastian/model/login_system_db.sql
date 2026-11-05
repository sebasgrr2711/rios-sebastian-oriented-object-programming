CREATE DATABASE IF NOT EXISTS login_system_db;
USE login_system_db;

CREATE TABLE IF NOT EXISTS users (
    id_user INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(256) NOT NULL,
    nombre VARCHAR(50) NOT NULL
);

 CREATE TABLE IF NOT EXISTS products(
    id_product INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR (100) NOT NULL,
    precio DECIMAL (10,2) NOT NULL,
    stock INT NOT NULL
 );

INSERT INTO users (username, password, nombre) VALUES ('admin', 'admin123', 'Superadmin');

ON DUPLICATE KEY UPDATE nombre='Super admin';

INSERT INTO products (nombre, precio, stock) VALUES 
('Laptop HP', 12500.50, 10),
('Mouse Inalámbrico', 350.00, 25),
('Teclado Mecánico', 850.00, 15),
('Monitor HP', 4000.00, 10),
('Teclado', 200.00, 10);