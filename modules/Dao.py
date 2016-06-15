import sqlite3



class Dao():

    def __init__(self):
        self.conn=sqlite3.connect("exp.sqlite3")
        self.cur=self.conn.cursor()

    def insertSmemory(self, t):
        self.cur.execute("insert or replace into smemory (item,ref,strong,parent) values (?,?,?,?) ",
        t)
        self.commit()
    def commit(self):
        self.conn.commit()
    def selectSmemory(self):
        self.cur.execute("select * from smemory")
        return self.cur.fetchall()
    def resetDb(self):
        self.cur.executescript('''
        drop table if exists smemory;
        drop table if exists lmemory;
        drop table if exists context;

        CREATE TABLE smemory (
            id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            item    TEXT ,
            ref     Text unique,
            strong  Text,
            parent  Text
        );
        CREATE TABLE lmemory (
            id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            type    TEXT,
            item    TEXT
        );
        CREATE TABLE context (
            id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            item    TEXT UNIQUE
        );
        ''')
