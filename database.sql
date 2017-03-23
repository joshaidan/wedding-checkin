
CREATE TABLE checkins (
    id int,
    date text,
    firstname text,
    lastname text
);

CREATE TABLE people (
    id int,
    firstname text,
    lastname text,
    uuid text,
    table_id int
);

CREATE TABLE tables (
    id int,
    name text,
    number int
)

INSERT INTO people (id, firstname, lastname, uuid) VALUES (1, 'Brian', 'Jones', '0011');