DROP TABLE IF EXISTS locations;
CREATE TABLE locations (
   id TEXT PRIMARY KEY UNIQUE,
   name TEXT,
   lat NUMBER,
   lon NUMBER,
   country TEXT
);

CREATE TABLE users (
   username TEXT PRIMARY KEY,
   password TEXT
);

INSERT INTO users(username, password)
VALUES('ad', 'min');

