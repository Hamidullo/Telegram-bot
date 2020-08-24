import sqlite3

class DBHelper1:

    def __init__(self, dbname="brigadiri.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def dele(self, chat_id):
        delete = f"DELETE FROM brigadiri where chat_id = ?"
        self.conn.execute(delete, (chat_id,))
        self.conn.commit()

    def setup(self):
        tblstmt = "CREATE TABLE IF NOT EXISTS brigadiri (user_id text, chat_id text,obyom text)"
        user_ididx = "CREATE INDEX IF NOT EXISTS user_idIndex ON brigadiri (user_id ASC)"
        chat_ididx = "CREATE INDEX IF NOT EXISTS chat_idIndex ON brigadiri (chat_id ASC)"
        obyomidx = "CREATE INDEX IF NOT EXISTS obyomIndex ON brigadiri (obyom ASC)"

        self.conn.execute(tblstmt)
        self.conn.execute(user_ididx)
        self.conn.execute(chat_ididx)
        self.conn.execute(obyomidx)


        self.conn.commit()

    def add_otchyot(self, user_id,chat_id, obyom):
        stmt = "INSERT INTO brigadiri (user_id, chat_id, obyom) VALUES (?, ?, ?)"
        args = (user_id, chat_id, obyom)
        self.conn.execute(stmt, args)
        self.conn.commit()

    def update_Obyom(self, obyom, chat_id, user_id):
        stmt = "UPDATE brigadiri SET obyom = ? WHERE chat_id = ? and user_id = ?"
        data = (obyom, chat_id, user_id)
        self.conn.execute(stmt, data)
        self.conn.commit()

    def get_Obyom(self, chat_id,text):
        stmt = "SELECT obyom FROM brigadiri WHERE chat_id = (?) and obyom = (?)"
        args = (chat_id,text)
        return [x[0] for x in self.conn.execute(stmt, args)]

    def get_id(self):
        stmt = "SELECT user_id FROM brigadiri"
        return [x[0] for x in self.conn.execute(stmt, )]

    def delete_item(self, chat_id):
        stmt = "DELETE FROM brigadiri WHERE chat_id = (?)"
        args = (chat_id,)
        self.conn.execute(stmt, args)
        self.conn.commit()

    def get_item(self, obyom):
        stmt = "SELECT chat_id FROM brigadiri WHERE obyom = (?)"
        args = (obyom,)
        return [x[0] for x in self.conn.execute(stmt, args)]

    def get_data(self):
        stmt = "SELECT * FROM brigadiri"
        return [x[0] for x in self.conn.execute(stmt, )]

