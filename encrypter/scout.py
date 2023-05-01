import sqlite3
from requests import get

class Scout:
    def __init__(self):
        self.con = sqlite3.connect(".ديسيبل")
        self.cur = self.con.cursor()
        try:
            self.cur.execute("""
            CREATE TABLE info(
                pid INTEGER PRIMARY KEY AUTOINCREMENT,
                ip varchar(30),
                isBorn number(1)
                )
            """)
        except Exception as e:
            pass

    def putBorn(self):
        self.cur.execute("INSERT INTO info (isBorn) VALUES (1)")
        self.con.commit()

    def getBorn(self):
        return self.cur.execute("SELECT isBorn FROM info").fetchone()

    def getIP(self):
        ip = [(get('https://api.ipify.org').content.decode('utf8'))]
        self.cur.execute('UPDATE info SET ip=? WHERE pid=1',ip)
        self.con.commit()