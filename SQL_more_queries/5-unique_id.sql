-- creates the table 'unique_id'
CREATE TABLE IF NOT EXISTS unique_id
(
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);