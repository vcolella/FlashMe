CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username TEXT NOT NULL,
    hash TEXT NOT NULL
);

-- CREATE TABLE sqlite_sequence(name, seq);

CREATE UNIQUE INDEX username ON users (username);

CREATE TABLE sets (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    tags TEXT,
    total_cards INTEGER NOT NULL,
    FOREIGN KEY (username_id) REFERENCES users(id)
);

CREATE TABLE cards (
    card_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username_id INTEGER NOT NULL,
    set_id INTEGER NOT NULL,
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    creation_date TEXT NOT NULL,
    FOREIGN KEY (set_id) REFERENCES sets(id)
    FOREIGN KEY (username_id) REFERENCES users(id)
);
