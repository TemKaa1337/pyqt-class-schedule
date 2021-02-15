from .db import Database


class DatabaseSchema:
    table_names = [
        'default_schedule',
        'current_schedule',
        'class_translations'
    ]
    schema = [
        '''
            CREATE TABLE default_schedule (
                id integer PRIMARY KEY AUTOINCREMENT ,
                monday text,
                tuesday text,
                wednesday text,
                thursday text,
                friday text,
                saturday text,
                sunday text
            );
        ''',
        '''
            CREATE TABLE current_schedule (
                id integer PRIMARY KEY AUTOINCREMENT ,
                date text type UNIQUE,
                monday text,
                tuesday text,
                wednesday text,
                thursday text,
                friday text,
                saturday text,
                sunday text
            );
        ''',
        '''
            CREATE TABLE class_translations (
                id integer PRIMARY KEY AUTOINCREMENT ,
                name text NOT NULL,
                translation text NOT NULL
            );
        '''
    ]

    def __init__(self):
        self.db = Database()

    def down(self):
        for table_query in self.table_names:
            self.db.cursor.execute('DROP TABLE IF EXISTS ' + table_query + ';')
            self.db.connection.commit()

    def up(self):
        for table_query in self.schema:
            self.db.cursor.execute(table_query)
            self.db.connection.commit()

    def refresh(self):
        self.down()
        self.up()

