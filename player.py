#импорты
from config import *
from music import MusicManager
from playsound3 import playsound as ps
import multiprocessing
import time
import os

#создаем класс 
class PlayerClass:

    #конструктор, все нановское потому что не передается ничо
    def __init__(self):
        self.nowplaying = None
        self.plsound = None
        self.music = None
    #метод для нахождения и воспроизведения трека
    def play(self):
        track = input('Введите название трека: ')
        self.music = MusicManager(track)
        self.music.downloadtrack()
        #включение музычки
        plsound = multiprocessing.Process(target=ps, args=(self.music.final_filename,))
        plsound.start()
        self.plsound = plsound

        #без этого не горит желанием работать код другой функции
        self.nowplaying = self.music.final_filename

        
        
        
        
    
    #метод для интерфейса
    def player_interface(self):
        while True:
            #очистка терминала
            os.system('cls' if os.name == 'nt' else 'clear')
            #создание интерфейса
            print(*greet, sep="\n")

            #ну тип определние играет или не
            if self.nowplaying and self.plsound.is_alive():
                print('Сейчас играет/последнее, что играло: ', self.nowplaying)
                print('4)Управление треком')

            #основные выборы
            option = int(input('\n1)Найти трек  2)Плейлисты  3)Экспорт/Импорт плейлиста \n\nВыберите действие: '))

            if option == 1:
                self.play()
            elif option == 4:
                #выбор че с треком делать
                optionl2 = int(input('\n1)В лайки  2)В плейлист  3)Остановить воспроизведение \n\nВыберите действие: '))
                #добавление в лайки
                if optionl2 == 1:
                    os.remove(self.nowplaying)
                    self.music.downloadtrack_tofolder()

                #остановка и удаление а то че оно память засоряет
                elif optionl2 == 3:
                    self.plsound.terminate()
                    os.remove(self.nowplaying)
                
             
                
            
                

#до сих пор не понял смысл этой конструкции и вообще при каких условиях __name__ меняет имя
if __name__ == '__main__':
    igrok = PlayerClass()
    igrok.player_interface() 






