import psycopg2 as ps
from psycopg2.extras import DictCursor, RealDictCursor
import config


class Db:
    def __init__(self):
        self.connection = ps.connect(**config.database)
        self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)

    def query(self, query, params=[]):
        self.cursor.execute(query, params)
        self.connection.commit()
        return self.cursor.fetchall() if self.cursor.description else None

    def close(self):
        self.cursor.close()
        self.connection.close()

    def new_user(self, chat_id, username):
        users = self.query('SELECT * FROM users WHERE chat_id = %s', (chat_id,))
        if len(users) < 1:
            self.query('INSERT INTO users(chat_id, username) VALUES(%s, %s)', (chat_id, username))

    def __del__(self):
        self.close()
