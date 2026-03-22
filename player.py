#импорты
from config import *
from music import MusicManager
from playsound3 import playsound as ps
import multiprocessing
import time
import os



#создаем класс 
class PlayerClass(MusicManager):

    #конструктор, все нановское потому что не передается ничо
    def __init__(self):
        self.plsound = None
        
    #метод для нахождения и воспроизведения трека
    def play(self):
        track = input('Введите название трека: ')
        self.name = track
        super().downloadtrack()
        #включение музычки
        plsound = multiprocessing.Process(target=ps, args=(self.final_filename,))
        plsound.start()
        self.plsound = plsound

    #метод для перемещения в лайки
    def track_to_likes(self):
        os.remove(self.final_filename)
        os.chdir('playlists')
        super().downloadtrack_tofolder()
        os.chdir('..')
        
    
    def playlists(self):
        if not os.path.exists('playlists'):
            os.makedirs('playlists')
        if not os.path.exists('playlists/likes'):
            os.makedirs('likes')
        
        os.chdir('playlists')
        playlistslist = os.listdir()
        print('Доступные плейлисты: ')
        count = 1
        for i in playlistslist:
            print(f'{count})', i)
        
        os.chdir('..')
        input()
    
    def makeplaylist(self):
        os.chdir('playlists')
        newplname = input('Введите название плейлиста: ')
        try:
            os.mkdir(newplname)
        except OSError:
            print('Такой плейлист уже есть')
        
        os.chdir('..')
        
        

        

    def delplaylist(self):
        os.chmod('playlists', 0o777)
        os.chdir('playlists')
        
        delplname = input('Введите название плейлиста: ')
        
        os.remove(delplname)
        
        
        os.chdir('..')
             


    #метод для остановки и удаления а то че оно память засоряет
    def stop_playing(self):
        self.plsound.terminate()
        try:
            os.remove(self.final_filename)
        except FileNotFoundError:
            pass


        
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
            option = int(input('\n1)Найти трек  2)Плейлисты  3)Экспорт/Импорт плейлиста \n\nВыберите действие: '))

            if option == 1:
                self.play()
            
            
            elif option == 2:
                while True:
                    optionl2pl = int(input('\n1)Создать плейлист  2)Удалить плейлист  3)Доступные плейлисты \n\nВыберите действие: '))
                    if optionl2pl == 1:
                        self.makeplaylist()

                    elif optionl2pl == 2:
                        self.delplaylist()

                    elif optionl2pl == 3:
                        self.playlists()

            elif option == 4:
                #выбор че с треком делать
                optionl2mn = int(input('\n1)В лайки  2)В плейлист  3)Остановить воспроизведение \n\nВыберите действие: '))
                if optionl2 == 1:
                    self.track_to_likes()
                    
                elif optionl2 == 3:
                    self.stop_playing()
                
            elif option == 111:
                print(os.getcwd())
                time.sleep(5)




                

#до сих пор не понял смысл этой конструкции и вообще при каких условиях __name__ меняет имя
if __name__ == '__main__':
    igrok = InterfaceClass()
    igrok.player_interface() 






