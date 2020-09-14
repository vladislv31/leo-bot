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

    def check_user(self, chat_id):
        users = self.query('SELECT * FROM users WHERE chat_id = %s', (chat_id,))
        if len(users) < 1:
            return False

        return True

    def get_user_id(self, chat_id):
        user = self.query('SELECT id FROM users WHERE chat_id = %s', (str(chat_id),))[0]
        return user['id']

    def new_user(self, chat_id, username):
        if not self.check_user(chat_id):
            self.query('INSERT INTO users(chat_id, username) VALUES(%s, %s)', (chat_id, username))

    def check_pin(self, pin):
        configs = self.query('SELECT * FROM configs WHERE pin = %s', (int(pin),))
        if len(configs) < 1:
            return False
        return True

    def check_config(self, config_id):
        configs = self.query('select * from configs where not exists(select * from used_configs where used_configs.config_id = configs.id) and id = %s', (config_id,))
        if len(configs) < 1:
            return False

        return True

    def get_config(self, config_id):
        config = self.query('select * from configs where not exists(select * from used_configs where used_configs.config_id = configs.id) and id = %s', (config_id,))
        if len(config) < 1:
            return False
        return config[0]
        


    def new_config(self, title, descr, pin):
        if not self.check_pin(pin):
            self.query('INSERT INTO configs(title, descr, pin) VALUES(%s, %s, %s)', (title, descr, int(pin)))
            return True
        return 'PIN-код уже занят'

    def get_free_configs(self):
        configs = self.query('select * from configs where not exists(select * from used_configs where used_configs.config_id = configs.id)')
        return configs

    def connect_config(self, user_id, config_id):
        self.query('INSERT INTO used_configs(user_id, config_id) VALUES(%s, %s)', (user_id, config_id))

    def __del__(self):
        self.close()
