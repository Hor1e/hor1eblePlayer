#импорты
from config import *
from music import MusicManager
from playsound3 import playsound as ps
import multiprocessing
import time
import os
import shutil
import random


#создаем класс 
class PlayerClass(MusicManager):

    #конструктор, все нановское потому что не передается ничо
    def __init__(self):
        self.plsound = None
        
    #метод для нахождения и воспроизведения трека
    def play(self):
        track = input('Введите название трека: ')
        if plsound and plsound.is_alive():
            plsound.terminate()
        
        self.name = track
        super().downloadtrack()
        #включение музычки
        plsound = multiprocessing.Process(target=ps, args=(self.final_filename,))
        plsound.start()
        self.plsound = plsound
    
    #метод для проигрывания музыки, которая уже скачана(в плейлисте)
    def play_alr_downloaded(self):
        plsound = multiprocessing.Process(target=ps, args=(self.randtrack,))
        plsound.start()
        self.plsound = plsound

    #метод для перемещения в лайки
    def track_to_likes(self):
        os.remove(self.final_filename)
        os.chdir('playlists')
        super().downloadtrack_tofolder()
        os.chdir('..')
        
    #метод для меню плейлистов
    def playlists(self):
        
        os.chdir('playlists')
        if not os.path.exists('likes'):
            os.makedirs('likes')
        playlistslist = os.listdir()
        print('Доступные плейлисты: ')
        count = 1
        for i in playlistslist:
            print(f'{count})', i)
            count += 1
        
        os.chdir('..')
        
    
    #метод для создания плейлиста
    def makeplaylist(self):
        os.chdir('playlists')
        newplname = input('Введите название плейлиста: ')
        try:
            os.mkdir(newplname)
        except OSError:
            print('Такой плейлист уже есть')
        
        os.chdir('..')
        
    #метод для удаления плейлиста
    def delplaylist(self):
        os.chdir('playlists')

        delplname = input('Введите название плейлиста: ')
        #4 строки снизу нагло украдены у ии
        def remove_readonly(func, path, excinfo):
            os.chmod(path, stat.S_IWRITE)
            func(path)
        shutil.rmtree(delplname, onerror=remove_readonly)
        
        os.chdir('..')
             

    #метод для остановки и удаления а то че оно память засоряет
    def stop_playing(self):
        self.plsound.terminate()
        try:
            os.remove(self.final_filename)
        except FileNotFoundError:
            pass
    
    #метод для проигрывания плейлиста
    def listen_to_playlist(self):
        os.chdir('playlists')
        viborplaylista = input('Введите название плейлиста: ') 
        os.chdir(viborplaylista)
        randlist = os.listdir()
        self.randtrack = random.choice(randlist)
        self.play_alr_downloaded()
        os.chdir('..')
        os.chdir('..')
        
        



        




#класс интерфейса, плеер его отец
class InterfaceClass(PlayerClass):
    def __init__(self):
        self.final_filename = None

    #метод для интерфейса
    def player_interface(self):
        while True:
            #очистка терминала
            os.system('cls' if os.name == 'nt' else 'clear')
            #создание интерфейса
            print(*greet, sep="\n")

            #ну тип определние играет или не
            if self.final_filename and self.plsound.is_alive():
                print('Сейчас играет/последнее, что играло: ', self.final_filename)
                print('4)Управление треком')

            #основные выборы
            option = int(input('\n1)Найти трек  2)Плейлисты  3)Экспорт/Импорт плейлиста 5)Выход \n\nВыберите действие: '))

            if option == 1:
                self.play()
            
            #заход в меню плейлистов
            elif option == 2:
                while True:
                    optionl2pl = int(input('\n1)Создать плейлист  2)Удалить плейлист  3)Доступные плейлисты  4)Главное меню \n\nВыберите действие: '))
                    if optionl2pl == 1:
                        self.makeplaylist()

                    elif optionl2pl == 2:
                        self.delplaylist()

                    elif optionl2pl == 3:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        self.playlists()
                        optionl3pl = int(input('\n1)Слушать  2)Открыть  3)Главное меню \n\nВыберите действие: '))
                        if optionl3pl == 1:
                            self.listen_to_playlist()
                            
                            



                    elif optionl2pl == 4:
                        break
                    
            elif option == 4:
                #выбор че с треком делать
                optionl2mn = int(input('\n1)В лайки  2)В плейлист  3)Остановить воспроизведение \n\nВыберите действие: '))
                if optionl2mn == 1:
                    self.track_to_likes()
                    
                elif optionl2mn == 3:
                    self.stop_playing()
                
            elif option == 111:
                print(os.getcwd())
                time.sleep(5)
            
            elif option == 5:
                break



#до сих пор не понял смысл этой конструкции и вообще при каких условиях __name__ меняет имя
if __name__ == '__main__':
    try:
        igrok = InterfaceClass()
        igrok.player_interface()
    except KeyboardInterrupt:
        print('\nПрограмма завершена самим пользователем')
        time.sleep(2) 






