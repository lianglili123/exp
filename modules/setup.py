import sqlite3

conn=sqlite3.connect("exp.sqlite3")
cur=conn.cursor()

cur.executescript('''
drop table if exists smemory;
drop table if exists lmemory;
drop table if exists context;

CREATE TABLE smemory (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    item    TEXT UNIQUE,
    ref     Text
);
CREATE TABLE lmemory (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    item    TEXT UNIQUE
);
CREATE TABLE context (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    item    TEXT UNIQUE
);
''')
