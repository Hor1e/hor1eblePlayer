#импорты
from config import *
from music import MusicManager
import simpleaudio as sa


#надпись-приветсвие, можете изменить на любой ascii арт или текст в config'е
print(*greet, sep="\n")

#выбираем действие
option = int(input('Выберите действие:\n1)Найти трек  2)Плейлисты  3)Экспорт/Импорт плейлиста \n'))


#создаем класс
class player:
    #инит
    def __init__(self):
        pass
    

    #метод для нахождения и воспроизведения трека
    def play(self):
        track = input('Введите название трека: ')
        music = MusicManager(track)
        music.downloadtrack()
        #включение музычки
        
        wave_obj = sa.WaveObject.from_wave_file(music.final_filename)
        play_obj = wave_obj.play()
        play_obj.wait_done()
        print('kdfsfjsfj')

        





Player = player()
if option == 1:
    Player.play()



















