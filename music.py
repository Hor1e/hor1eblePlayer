#импорты
from youtubesearchpython import VideosSearch as search
import yt_dlp
import os

#Переменная чтоб найти
idk = f'кислород капсайз'
#папка
folder = 'tracks'
#создание папки если ее нет
if not os.path.exists(folder):
    os.makedirs(folder)

#создание класса
class MusicManager:
    #инит
    def __init__(self, name):
        self.name = name
        
        
        
    #метод для получения ссылки на видео
    def getlink(self):
        
        music = search(self.name, limit=1)
        searchdict = music.result()
        self.link =  searchdict['result'][0]['link']
        #сохранение перемеенной в self, для обращения к ней в другом методе
        
        print('Ссылка на скачивание: ', self.link)
        
        
        
    #метод для скачивания трека(аудиодорожки из видео)
    def downloadtrack(self):
        #вызываем метод, чтобы воспользоваться переменной из него
        self.getlink()
        #настроечки для скачивания аудио
        ydl_opts = {
            #настройки подключения
            'source_address': '0.0.0.0', 
            'http_chunk_size': 262144,  
            'retries': 100,               
            'extractor_args': {
            'youtube': {
            'player_client': ['android', 'web'], # Использовать разные типы клиентов
            }
            #настройка высасывания аудио
            },
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
                'preferredquality': '192',
            }],
            'outtmpl': f'{folder}/%(title)s.%(ext)s',
                
        }
        #само скачивание
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.link])
     


        
       
        
            
        



idk2 = MusicManager(idk)
idk2.downloadtrack()



