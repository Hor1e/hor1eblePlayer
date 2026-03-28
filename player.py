#импорты
from config import *
from music import MusicManager
from data import DbManager
from urllib.parse import unquote
import vlc, random, shutil, glob, time, os



#создаем класс 
class PlayerClass(MusicManager, DbManager):

    #конструктор, все нановское потому что не передается ничо
    def __init__(self):
        self.sound = None
        self.track = None

    #метод для нахождения и воспроизведения трека
    def play(self):
        self.track = input('Введите название трека: ')
        if self.sound and self.sound.is_playing():
            self.sound.stop()
            
        
        self.name = self.track
        super().downloadtrack()
        self.sound = vlc.MediaPlayer(self.final_filename)
        self.sound.audio_set_volume(volume)
        time.sleep(1)
        self.sound.play()
       
    #метод для проигрывания музыки, которая уже скачана(в плейлисте)
    def play_alr_downloaded_random(self):
        if self.sound and self.sound.is_playing():
            self.sound.stop()
        self.sound = vlc.MediaPlayer(self.randtrack)
        self.sound.audio_set_volume(volume)
        time.sleep(1)
        self.sound.play()
    
    #метод для проигрывания (после выбора трека в плейлисте)
    def play_alr_downloaded(self):
        tr = input('Выберите трек: ')
        if self.sound and self.sound.is_playing():
            self.sound.stop()
        self.sound = vlc.MediaPlayer(tr)
        self.sound.audio_set_volume(volume)
        time.sleep(1)
        self.sound.play()

    #метод для перемещения в лайки
    def track_to_likes(self):
        os.remove(os.path.basename(unquote(self.sound.get_media().get_mrl())))
        self.folder = "likes"
        self.playlist = self.folder
        self.track_to_add = self.track
        super().add_track_to_likes()
        os.chdir('playlists')
        super().downloadtrack_tofolder()
        os.chdir('..')
    #метод для меню плейлистов
    def playlists(self):
        
        os.chdir('playlists')
        if not os.path.exists('likes'):
            os.makedirs('likes')
        playlistslist = os.listdir()
        playlistslist.remove('likes')
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
        self.newpl = newplname
        try:
            os.mkdir(newplname)
        except OSError:
            print('Такой плейлист уже есть')
        
        os.chdir('..')
        self.create_table()
        
    #метод для удаления плейлиста
    def delplaylist(self):
        os.chdir('playlists')

        delplname = input('Введите название плейлиста: ')
        self.table_name = delplname
        #4 строки снизу нагло украдены у ии
        def remove_readonly(func, path, excinfo):
            os.chmod(path, stat.S_IWRITE)
            func(path)
        shutil.rmtree(delplname, onerror=remove_readonly)
        
        os.chdir('..')
        self.del_table()
             

    #метод для остановки и удаления а то че оно память засоряет
    def stop_playing(self):
        self.sound.stop()

    #метод для проигрывания плейлиста
    def listen_to_playlist(self):
        os.chdir('playlists')
        viborplaylista = input('Введите название плейлиста: ') 
        os.chdir(viborplaylista)
        
        try:
            randlist = os.listdir()
            self.randtrack = random.choice(randlist)
            self.play_alr_downloaded()
        except IndexError:
            print("Плейлист пуст")
        os.chdir('..')
        os.chdir('..')
        time.sleep(1)

        os.system('cls' if os.name == 'nt' else 'clear')

    
    #метод для добавления в плейлисты
    def track_to_pl(self):
        os.remove(os.path.basename(unquote(self.sound.get_media().get_mrl())))
        self.basename = os.path.basename(unquote(self.sound.get_media().get_mrl()))
        self.folder = input('Введите название плейлиста: ')
        self.playlist = self.folder
        self.track_to_add = self.track
        super().add_track_to_db()
        os.chdir('playlists')
        super().downloadtrack_tofolder()
        os.chdir('..')
    
    #метод показывает содержимое плейлиста и че с ним можно сделать
    def show_pl(self):
        vibor = input('Выберите плейлист: ')
        os.chdir('playlists')
        os.chdir(vibor)
        print(os.getcwd())
        playlistslist = os.listdir()
        count = 1
        for i in playlistslist:
            print(f'{count})', i)
            count += 1
        print('1)Слушать трек 2)Удалить трек 3)В главное меню')
        vibornext = int(input("Выберите действие: "))
        if vibornext == 1:
            vibornext1 = input("Выберите трек: ")
            if self.sound and self.sound.is_playing():
                self.sound.stop()
            self.sound = vlc.MediaPlayer(vibornext1)
            self.sound.audio_set_volume(volume)
            time.sleep(1)
            self.sound.play()

        elif vibornext == 2:
            vibornext1 = input("Выберите трек: ")
            os.remove(vibornext1)
            self.track_to_del = vibornext1
            self.playlist = vibor
            os.chdir('..')
            os.chdir('..')
            self.del_track_from_db()
            os.chdir('playlists')
            os.chdir(vibor)
        
        elif vibornext == 3:
            pass
        os.chdir('..')
        os.chdir('..')
    

    #метод для импорта
    def importplaylist(self):
        count = 1
        listdb = []
        for file in glob.glob("*.db"):
            listdb.append(file)
        listdb.remove('databasewithplaylists.db')
        for i in listdb:
            print(f'{count})', i)
            count += 1
        self.imp_db = input('Введите название бд, из которой хотите импортировать плейлист: ')
        self.imp()
        input()


    #просто в конце программы вызвать, чтоб удалил ненужное
    def endofprogramm(self):
        for file in glob.glob("*.wav"):
            os.remove(file)
        for file in glob.glob("*.part"):
                os.remove(file)
    
        
        




#класс интерфейса, плеер его отец
class InterfaceClass(PlayerClass):
    def __init__(self):
        self.final_filename = None
        self.sound = None

    #метод для интерфейса
    def player_interface(self):
        while True:
            #очистка терминала
            os.system('cls' if os.name == 'nt' else 'clear')
            #создание интерфейса
            print(*greet, sep="\n")

            #ну тип определние играет или не
            if self.sound and self.sound.is_playing():
                print('Сейчас играет: ', os.path.basename(unquote(self.sound.get_media().get_mrl())))
              

            #основные выборы
            option = int(input('\n1)Найти трек  2)Плейлисты  3)Экспорт/Импорт плейлиста\n4)Управление треком  5)Выход \n\nВыберите действие: '))

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
                        elif optionl3pl == 2:
                            self.show_pl()
                            
                            



                    elif optionl2pl == 4:
                        break

            elif option == 3:
                print("1)Экспорт 2)Импорт \n(импорты и экспорты используют формат .db)")
                optionl2ie = int(input('Выберите действие: '))
                if optionl2ie == 1:
                    self.playlists()
                    self.exp_playlist = input('Введите название плейлиста для экспорта: ')
                    self.export()
                elif optionl2ie == 2:
                    self.importplaylist()
                    
            elif option == 4:
                if self.sound and self.sound.is_playing():
                    optionl2mn = int(input('\n1)В лайки  2)В плейлист  3)Остановить воспроизведение \n\nВыберите действие: '))

                    if optionl2mn == 1:
                        self.track_to_likes()
                    
                    elif optionl2mn == 2:
                        self.playlists()
                        self.track_to_pl()
                        
                        
                    elif optionl2mn == 3:
                        self.stop_playing()
                else:
                    print('Сейчас ничего не играет.')
            
            elif option == 5:
                self.endofprogramm()
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            
            #скрытые опции для проверок
            elif option == 111:
                print(os.getcwd())
                time.sleep(5)

            elif option == 222:
                a = unquote(self.sound.get_media().get_mrl())
                print(os.path.basename(a))
                print(self.sound.get_state())
                print(self.sound.is_playing())
                time.sleep(5)


            else:
                print('Недоступно.')


#до сих пор не понял смысл этой конструкции и вообще при каких условиях __name__ меняет имя
if __name__ == '__main__':
    db = DbManager()
    db.create_table_likes()
    try:
        igrok = InterfaceClass()
        igrok.player_interface()

    except KeyboardInterrupt:
        for file in glob.glob("*.wav"):
            os.remove(file)
        for file in glob.glob("*.part"):
                os.remove(file)
        print('\nПрограмма завершена самим пользователем')
        time.sleep(2) 
        os.system('cls' if os.name == 'nt' else 'clear')

    except ValueError:
        pass
        
