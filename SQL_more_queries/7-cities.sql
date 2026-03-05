-- 7-cities
-- Creates a cities table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities (
	id int NOT NULL AUTO_INCREMENT,
	state_id int NOT NULL,
	name varchar(256) NOT NULL,
	PRIMARY KEY (id),
	UNIQUE KEY id (id),
	FOREIGN KEY (state_id) REFERENCES states(id)
);
