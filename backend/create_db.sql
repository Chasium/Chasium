CREATE USER IF NOT EXISTS chasium IDENTIFIED BY '123456';
DROP DATABASE IF EXISTS chasium;
CREATE DATABASE IF NOT EXISTS chasium;
GRANT ALL ON chasium.* TO 'chasium'@'%' IDENTIFIED BY '123456';