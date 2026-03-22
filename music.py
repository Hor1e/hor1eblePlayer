#импорты
from youtubesearchpython import VideosSearch as search
import yt_dlp
import os


#папка
folderlikes = 'likes'
#создание папки если ее нет
if not os.path.exists(f'playlists/{folderlikes}'):
    os.makedirs(f'playlists/{folderlikes}')

#создание класса
class MusicManager:
    #инит
    def __init__(self, name):
        self.name = name
        
        
        
    #метод для получения ссылки на видео
    def getlink(self):
        
        music = search(self.name, limit=1)
        searchdict = music.result()
        #сохранение перемеенной в self, для обращения к ней в другом методе
        self.link = searchdict['result'][0]['link']
        
        
        
        
        
        
    #метод для скачивания трека(аудиодорожки из видео)
    def downloadtrack(self):
        #вызываем метод, чтобы воспользоваться переменной из него
        self.getlink()
        #настроечки для скачивания аудио
        ydl_opts = {
            #скрытие того что он пишет
            'quiet': True,
            'no_warnings': True,
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
            'outtmpl': f'%(title)s.%(ext)s',
                
        }
        #само скачивание
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.link])

            #получение конечного названия файла после конвертации в вав
            info = ydl.extract_info(self.link, download=False)
            filepath = ydl.prepare_filename(info)
            filename = os.path.basename(filepath)
            self.final_filename = os.path.splitext(filename)[0] + ".wav"

    def downloadtrack_tofolder(self):
        #вызываем метод, чтобы воспользоваться переменной из него
        self.getlink()
        #настроечки для скачивания аудио
        ydl_opts = {
            #скрытие того что он пишет
            'quiet': True,
            'no_warnings': True,
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
            'outtmpl': f'{folderlikes}/%(title)s.%(ext)s',
                
        }
        #само скачивание
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.link])

            #получение конечного названия файла после конвертации в вав
            info = ydl.extract_info(self.link, download=False)
            filepath = ydl.prepare_filename(info)
            filename = os.path.basename(filepath)
            self.final_filename = os.path.splitext(filename)[0] + ".wav"

            
            
     


        
       
        
            



