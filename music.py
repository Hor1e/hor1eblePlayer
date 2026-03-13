#импорты
from youtubesearchpython import VideosSearch as search
import youtube_dl


#Переменная чтоб найти
idk = 'плачь - rizza'


#создание класса
class MusicManager:
    #инит
    def __init__(self, name):
        self.name = name
        
        
        
    #метод для получения ссылки на видео
    def getlink(self):
        music = search(self.name, limit=1)
        searchdict = music.result()
        searchlist = searchdict['result']
        #сохранение перемеенной в self, для обращения к ней в другом методе
        self.link = searchlist[0]['link']
        
        
        
    #метод для скачивания трека(аудиодорожки из видео)
    def downloadtrack(self):
        #вызываем метод, чтобы воспользоваться переменной из него
        self.getlink()

        


idk2 = MusicManager(idk)


