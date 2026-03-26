#код для управления базой данных, все ради экспорта и импорта плейлистов
#(я надеюсь, что соберу какое-никакое комьюнити плееру)
import sqlite3

class DbManager:

    def __init__(self, database):
        self.database = database
        self.newpl = None
        self.table_name = None

    def create_table_likes(self):
        con = sqlite3.connect(self.database)
        cur = con.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS likes(title)
        """)
        con.close()
    
    def create_table(self):
        con = sqlite3.connect(self.database)
        cur = con.cursor()
        cur.execute(f"""
        CREATE TABLE IF NOT EXISTS {self.newpl}(title)
        """)
        con.close()
    
    def del_table(self):
        con = sqlite3.connect(self.database)
        cur = con.cursor()
        cur.execute(f"""
        DROP TABLE IF EXISTS {self.table_name}
        """)
        con.close()
        

        


idk = DbManager('databasewithplaylists')
idk.create_table_likes()
