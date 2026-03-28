#код для управления базой данных, все ради экспорта и импорта плейлистов
#(я надеюсь, что соберу какое-никакое комьюнити плееру)
import sqlite3, os
from music import MusicManager

class DbManager:
    #конструктор
    def __init__(self):

        self.newpl = None
        self.table_name = None
        self.exp_playlist = None
        self.playlist = None
        self.track_to_add = None
        self.del_track_from_db = None
        self.basename = None
        self.imp_db = None
    #метод для создания плейлиста с лайками
    def create_table_likes(self):
        con = sqlite3.connect('databasewithplaylists.db')
        cur = con.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS likes(name PK TEXT, nameasfile PK TEXT)
        """)
        con.close()
    #метод для создания плейлиста
    def create_table(self):
        con = sqlite3.connect('databasewithplaylists.db')
        cur = con.cursor()
        cur.execute(f"""
        CREATE TABLE IF NOT EXISTS {self.newpl}
        (title PK TEXT, nameasfile PK TEXT)
        """)
        con.close()
    #метод для удаления всего плейлиста
    def del_table(self):
        con = sqlite3.connect('databasewithplaylists.db')
        cur = con.cursor()
        cur.execute(f"""
        DROP TABLE IF EXISTS {self.table_name}
        """)
        con.close()
    #метод для добавления трека в плейлист
    def add_track_to_db(self):
        con = sqlite3.connect('databasewithplaylists.db')
        cur = con.cursor()
        cur.execute(f"""
        INSERT INTO {self.playlist} VALUES (?,?)
        """,(self.track_to_add, self.basename,))
        con.commit()
        con.close()
    #метод для добавления трека в лайки
    def add_track_to_likes(self):
        con = sqlite3.connect('databasewithplaylists.db')
        cur = con.cursor()
        cur.execute(f"""
        INSERT INTO likes VALUES (?,?)
        """,(self.track_to_add, self.basename,))
        con.commit()
        con.close()
    #метод для удаления трека из плейлиста
    def del_track_from_db(self):
        con = sqlite3.connect('databasewithplaylists.db')
        
        cur = con.cursor()
        cur.execute(f"""
        DELETE FROM {self.playlist} WHERE nameasfile = ?
        """,(self.track_to_del,))
        con.commit()
        con.close()


    #метод для экспорта плейлиста в другую бд(потом с такой же можно будет скачать чужой плейлист)
    def export(self):
        con = sqlite3.connect("export.db")
        cur = con.cursor()
        cur.execute(f"""
        CREATE TABLE IF NOT EXISTS playlist(name)
        """)
        con.close()

        con = sqlite3.connect('databasewithplaylists.db')
        cur = con.cursor()
        cur.execute(f"""
        ATTACH DATABASE "export.db" AS exp
        """)
        cur.execute(f"""
        INSERT INTO exp.playlist
        SELECT title FROM {self.exp_playlist}
        """)
        con.commit()
        con.close()
    
    #метод для импортирования плейлиста(скачивания плейлиста по базе данных)
    def imp(self):
        con = sqlite3.connect(self.imp_db)
        cur = con.cursor()
        cur.execute("""
        SELECT name FROM playlist
        """)
        rows = cur.fetchall()
        
        os.chdir('playlists')
        plimport = input('Напишите название импортного плейлиста: ')
        os.mkdir(plimport)
        os.chdir(plimport)
        for row in rows:
            name = row[0]
            msc = MusicManager(name)
            msc.downloadtrack()
        os.chdir('..')
        os.chdir('..')
        con.close()
        

        





