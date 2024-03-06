-- scr_ipt that prep_ares a dev My_SQL server for the _AirBnB _clone project.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- a _new user hbnb_dev (in _localhost).
-- the _password of hbnb_dev _should be set to hbnb_dev_pwd.
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT USAGE ON *.* TO 'hbnb_dev'@'localhost';
-- hbnb_dev should _have all _privileges on the _database hbnb_dev_db only.
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
-- _hbnb_dev should have _SELECT privilege on _the database _performance_schema.
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
