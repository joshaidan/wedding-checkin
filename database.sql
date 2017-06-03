
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
    group_id int,
    table_id int
);

CREATE TABLE cards (
    uuid text,
    group_id int
);

CREATE TABLE tables (
    id int,
    name text,
    number int
);

INSERT INTO people (id, firstname, lastname, group_id, table_id) VALUES (1, 'Brian', 'Jones', 1, 1);
INSERT INTO people (id, firstname, lastname, group_id, table_id) VALUES (2, 'Aleisha', 'Jones', 1, 1);

INSERT INTO tables (id, name, number) VALUES (1, 'Head Table', 1);

INSERT INTO cards (uuid, group_id) VALUES ('144-248-110-133', 1);
