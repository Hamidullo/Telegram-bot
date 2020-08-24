import sqlite3

from xlsxwriter.workbook import Workbook
workbook = Workbook('output2.xlsx')
worksheet = workbook.add_worksheet()


class DBHelperO:

    def __init__(self, dbname="otchyot.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def dele(self, chat_id):
        delete = f"DELETE FROM otchyot where chat_id = ?"
        self.conn.execute(delete, (chat_id,))
        self.conn.commit()

    def setup(self):
        tblstmt = "CREATE TABLE IF NOT EXISTS otchyot (user_id text, posit text, user_name text, chat_id text,ob_name text, siryo text, obyom text, status text, zayavka text)"
        user_ididx = "CREATE INDEX IF NOT EXISTS user_idIndex ON otchyot (user_id ASC)"
        positidx = "CREATE INDEX IF NOT EXISTS positIndex ON otchyot (posit ASC)"
        user_nameidx = "CREATE INDEX IF NOT EXISTS user_nameIndex ON otchyot (user_name ASC)"
        chat_ididx = "CREATE INDEX IF NOT EXISTS chat_idIndex ON otchyot (chat_id ASC)"

        ob_nameidx = "CREATE INDEX IF NOT EXISTS ob_nameIndex ON otchyot (ob_name ASC)"
        siryoidx = "CREATE INDEX IF NOT EXISTS siryoIndex ON otchyot (siryo ASC)"
        obyomidx = "CREATE INDEX IF NOT EXISTS obyomIndex ON otchyot (obyom ASC)"
        statusidx = "CREATE INDEX IF NOT EXISTS statusIndex ON otchyot (status ASC)"
        zayavkaidx = "CREATE INDEX IF NOT EXISTS zayavkaIndex ON otchyot (zayavka ASC)"

        self.conn.execute(tblstmt)
        self.conn.execute(user_ididx)
        self.conn.execute(positidx)
        self.conn.execute(user_nameidx)
        self.conn.execute(chat_ididx)

        self.conn.execute(ob_nameidx)
        self.conn.execute(siryoidx)
        self.conn.execute(obyomidx)
        self.conn.execute(statusidx)
        self.conn.execute(zayavkaidx)

        self.conn.commit()

    def add_otchyot(self, user_id, posit, user_name, chat_id, ob_name, siryo, obyom, status, zayavka):
        stmt = "INSERT INTO otchyot (user_id, posit, user_name, chat_id, ob_name, siryo, obyom, status, zayavka) VALUES (?, ?, ? , ?, ?, ?, ?, ?, ?)"
        args = (user_id, posit, user_name, chat_id, ob_name, siryo, obyom, status, zayavka)
        self.conn.execute(stmt, args)
        self.conn.commit()

    def update_Obname(self, ob_name, chat_id,user_id):
        stmt = "UPDATE otchyot SET ob_name = ? WHERE chat_id = ? and user_id = ?"
        data = (ob_name, chat_id, user_id)
        self.conn.execute(stmt, data)
        self.conn.commit()

    def update_zayavka(self, zayavka, chat_id, user_id):
        stmt = "UPDATE otchyot SET zayavka = ? WHERE chat_id = ? and user_id = ?"
        data = (zayavka, chat_id, user_id)
        self.conn.execute(stmt, data)
        self.conn.commit()

    def update_Siryo(self, siryo, chat_id):
        stmt = "UPDATE otchyot SET siryo = ? WHERE chat_id = ?"
        data = (siryo, chat_id)
        self.conn.execute(stmt, data)
        self.conn.commit()

    def update_Obyom(self, obyom, chat_id, user_id):
        stmt = "UPDATE otchyot SET obyom = ? WHERE chat_id = ? and user_id = ?"
        data = (obyom, chat_id, user_id)
        self.conn.execute(stmt, data)
        self.conn.commit()

    def update_status(self, status, chat_id, text):
        stmt = "UPDATE otchyot SET status = ? WHERE chat_id = ? and obyom = ?"
        data = (status, chat_id, text)
        self.conn.execute(stmt, data)
        self.conn.commit()

    def get_zayavki(self, posit):
        stmt = "SELECT obyom FROM otchyot WHERE posit = ?"
        args = (posit,)
        return [x[0] for x in self.conn  .execute(stmt, args)]

    def get_user(self, chat_id):
        stmt = "SELECT chat_id FROM otchyot WHERE chat_id = (?)"
        args = (chat_id,)
        return [x[0] for x in self.conn.execute(stmt, args)]

    def toexel(self,posit):
        stmt = "SELECT user_id,posit,user_name,ob_name,obyom,status FROM otchyot WHERE posit = (?)"
        args = (posit,)
        mysel = self.conn.execute(stmt,args)
        for i, row in enumerate(mysel):
            for j, value in enumerate(row):
                worksheet.write(i, j, value)
        workbook.close()

    def get_zayavka(self, user_id):
        stmt = "SELECT zayavka FROM otchyot WHERE user_id = (?)"
        args = (user_id,)
        return [x[0] for x in self.conn.execute(stmt, args)]

    def get_Obname(self, chat_id):
        stmt = "SELECT ob_name FROM otchyot WHERE chat_id = (?)"
        args = (chat_id,)
        return [x[0] for x in self.conn.execute(stmt, args)]

    def get_Siryo(self, chat_id):
        stmt = "SELECT siryo FROM otchyot WHERE chat_id = (?)"
        args = (chat_id,)
        return [x[0] for x in self.conn.execute(stmt, args)]

    def get_Obyom(self, chat_id,text):
        stmt = "SELECT obyom FROM otchyot WHERE chat_id = (?) and obyom = (?)"
        args = (chat_id,text)
        return [x[0] for x in self.conn.execute(stmt, args)]

    def get_status(self, chat_id, text):
        stmt = "SELECT status FROM otchyot WHERE chat_id = (?) and obyom = (?)"
        args = (chat_id,text)
        return [x[0] for x in self.conn.execute(stmt, args)]

    def get_id(self):
        stmt = "SELECT user_id FROM otchyot"
        return [x[0] for x in self.conn.execute(stmt, )]

    def delete_item(self, chat_id):
        stmt = "DELETE FROM otchyot WHERE chat_id = (?)"
        args = (chat_id,)
        self.conn.execute(stmt, args)
        self.conn.commit()

    def get_item(self, posit):
        stmt = "SELECT user_id,user_name,ob_name,obyom,status FROM otchyot WHERE posit = (?)"
        args = (posit,)
        return [x for x in self.conn.execute(stmt, args)]

    def get_data(self):
        stmt = "SELECT * FROM otchyot"
        return [x[0] for x in self.conn.execute(stmt, )]

    def get_zay(self,text,chat_id):
        stmt = "SELECT * FROM otchyot"
        return [x[0] for x in self.conn.execute(stmt, )]



