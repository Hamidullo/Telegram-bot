import sqlite3


class DBHelper:

    def __init__(self, dbname="zayavka.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def dele(self, chat_id):
        delete = f"DELETE FROM users where chat_id = ?"
        self.conn.execute(delete,(chat_id,))
        self.conn.commit()

    def setup(self):
        tblstmt = "CREATE TABLE IF NOT EXISTS users (user_id text, posit text, user_name text, chat_id text,login text, parol text, numb text, lang text, status text, unposit text)"
        user_ididx = "CREATE INDEX IF NOT EXISTS user_idIndex ON users (user_id ASC)"
        positidx = "CREATE INDEX IF NOT EXISTS positIndex ON users (posit ASC)"
        user_nameidx = "CREATE INDEX IF NOT EXISTS user_nameIndex ON users (user_name ASC)"
        chat_ididx = "CREATE INDEX IF NOT EXISTS chat_idIndex ON users (chat_id ASC)"
        loginidx = "CREATE INDEX IF NOT EXISTS loginIndex ON users (login ASC)"
        parolidx = "CREATE INDEX IF NOT EXISTS parolIndex ON users (parol ASC)"
        numberidx = "CREATE INDEX IF NOT EXISTS numbIndex ON users (numb ASC)"
        langidx = "CREATE INDEX IF NOT EXISTS langIndex ON users (lang ASC)"
        statusidx = "CREATE INDEX IF NOT EXISTS statusIndex ON users (status ASC)"
        unpositidx = "CREATE INDEX IF NOT EXISTS unpositIndex ON users (status ASC)"
        self.conn.execute(tblstmt)
        self.conn.execute(user_ididx)
        self.conn.execute(positidx)
        self.conn.execute(user_nameidx)
        self.conn.execute(chat_ididx)
        self.conn.execute(loginidx)
        self.conn.execute(parolidx)
        self.conn.execute(numberidx)
        self.conn.execute(langidx)
        self.conn.execute(statusidx)
        self.conn.execute(unpositidx)
        self.conn.commit()

    def add_user(self, user_id, posit, user_name, chat_id, login, parol, numb, lang, status,unposit):
        stmt = "INSERT INTO users (user_id, posit, user_name, chat_id, login, parol, numb, lang, status, unposit) VALUES (?, ?, ? , ?, ?, ?, ?, ?, ?, ?)"
        args = (user_id, posit, user_name, chat_id, login, parol, numb, lang, status,unposit)
        self.conn.execute(stmt, args)
        self.conn.commit()

    def update_lang(self, lang, chat_id):
        stmt = "UPDATE users SET lang = ? WHERE chat_id = ?"
        data = (lang,chat_id)
        self.conn.execute(stmt,data)
        self.conn.commit()

    def update_unposit(self, unposit, chat_id):
        stmt = "UPDATE users SET unposit = ? WHERE chat_id = ?"
        data = (unposit,chat_id)
        self.conn.execute(stmt,data)
        self.conn.commit()

    def update_id(self, id, chat_id):
        stmt = "UPDATE users SET user_id = ? WHERE chat_id = ?"
        data = (id,chat_id)
        self.conn.execute(stmt,data)
        self.conn.commit()

    def update_numb(self, numb, chat_id):
        stmt = "UPDATE users SET numb = ? WHERE chat_id = ?"
        data = (numb,chat_id)
        self.conn.execute(stmt,data)
        self.conn.commit()

    def update_name(self, name, chat_id):
        stmt = "UPDATE users SET user_name = ? WHERE chat_id = ?"
        data = (name,chat_id)
        self.conn.execute(stmt,data)
        self.conn.commit()

    def update_login(self, login, chat_id):
        stmt = "UPDATE users SET login = ? WHERE chat_id = ?"
        data = (login,chat_id)
        self.conn.execute(stmt,data)
        self.conn.commit()

    def update_parol(self, paol, chat_id):
        stmt = "UPDATE users SET parol = ? WHERE chat_id = ?"
        data = (paol,chat_id)
        self.conn.execute(stmt,data)
        self.conn.commit()

    def update_position(self, position, chat_id):
        stmt = "UPDATE users SET posit = ? WHERE chat_id = ?"
        data = (position,chat_id)
        self.conn.execute(stmt,data)
        self.conn.commit()

    def set_status(self, status, chat_id):
        stmt = "UPDATE users SET status = ? WHERE chat_id = ?"
        data = (status,chat_id)
        self.conn.execute(stmt,data)
        self.conn.commit()

    def get_userID(self, chat):
        stmt = "SELECT user_id FROM users WHERE chat_id = (?)"
        args = (chat, )
        return [x[0] for x in self.conn.execute(stmt, args)]

    def get_unposit(self, chat):
        stmt = "SELECT unposit FROM users WHERE chat_id = (?)"
        args = (chat, )
        return [x[0] for x in self.conn.execute(stmt, args)]

    def has_user(self, chat):
        stmt = "SELECT chat_id FROM users WHERE chat_id = (?)"
        args = (chat, )
        return [x[0] for x in self.conn.execute(stmt, args)]

    def has_name(self, name):
        stmt = "SELECT user_name FROM users WHERE user_name = (?)"
        args = (name, )
        return [x[0] for x in self.conn.execute(stmt, args)]

    def get_name(self, chat_id):
        stmt = "SELECT user_name FROM users WHERE chat_id = (?)"
        args = (chat_id, )
        return [x[0] for x in self.conn.execute(stmt, args)]

    def has_login(self, login):
        stmt = "SELECT login FROM users WHERE login = (?)"
        args = (login, )
        return [x[0] for x in self.conn.execute(stmt, args)]

    def get_login(self, chat_id):
        stmt = "SELECT login FROM users WHERE chat_id = (?)"
        args = (chat_id, )
        return [x[0] for x in self.conn.execute(stmt, args)]

    def has_parol(self, parol):
        stmt = "SELECT parol FROM users WHERE parol = (?)"
        args = (parol, )
        return [x[0] for x in self.conn.execute(stmt, args)]

    def get_parol(self, chat_id):
        stmt = "SELECT parol FROM users WHERE chat_id = (?)"
        args = (chat_id, )
        return [x[0] for x in self.conn.execute(stmt, args)]

    def is_lang(self, lang):
        stmt = "SELECT lang FROM users WHERE lang = (?)"
        args = (lang, )
        return [x[0] for x in self.conn.execute(stmt, args)]

    def get_lang(self, chat_id):
        stmt = "SELECT lang FROM users WHERE chat_id = (?)"
        args = (chat_id, )
        return [x[0] for x in self.conn.execute(stmt, args)]

    def is_position(self, position):
        stmt = "SELECT posit FROM users WHERE posit = (?)"
        args = (position, )
        return [x[0] for x in self.conn.execute(stmt, args)]

    def is_number(self, number):
        stmt = "SELECT numb FROM users WHERE numb = (?)"
        args = (number, )
        return [x[0] for x in self.conn.execute(stmt, args)]

    def get_number(self, chat_id):
        stmt = "SELECT numb FROM users WHERE chat_id = (?)"
        args = (chat_id, )
        return [x[0] for x in self.conn.execute(stmt, args)]

    def get_status(self, chat_id):
        stmt = "SELECT status FROM users WHERE chat_id = (?)"
        args = (chat_id, )
        return [x[0] for x in self.conn.execute(stmt, args)]

    def get_dispetcher(self, text,status):
        stmt = "SELECT chat_id FROM users WHERE posit = (?) and status = (?)"
        args = (text,status )
        return [x[0] for x in self.conn.execute(stmt, args)]

    def get_disp(self, text,status):
        stmt = "SELECT chat_id FROM users WHERE posit = (?) and status = (?)"
        args = (text,status )
        return [x[0] for x in self.conn.execute(stmt, args)]

    def get_position(self, chat_id):
        stmt = "SELECT posit FROM users WHERE chat_id = (?)"
        args = (chat_id, )
        return [x[0] for x in self.conn.execute(stmt, args)]

    def delete_item(self, user_name, chat_id):
        stmt = "DELETE FROM users WHERE user_name = (?) AND chat_id = (?)"
        args = (user_name, chat_id)
        self.conn.execute(stmt, args)
        self.conn.commit()

    def get_item(self, chat_id):
        stmt = "SELECT * FROM users WHERE chat_id = (?)"
        args = (chat_id, )
        return [x[0] for x in self.conn.execute(stmt, args)]

    def get_count(self):
        stmt = "SELECT * FROM users"

        return [x for x in self.conn.execute(stmt, )]

    
            




