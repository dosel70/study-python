import pygame
from message_module import *
# 음악 정보를 담은 클래스
class Song:
    # 제목, 가수명, 파일 경로를 담을 것이다.
    def __init__(self,title,artist,file_path):
        self.title = title
        self.artist = artist
        self.file_path = file_path

    # "노래제목 - 가수명" 출력
    def __str__(self):
        return f"{self.title} by {self.artist}"

# 음악 검색, 재생, 추가, 삭제 등의 기능을 담은 클래스
class MusicPlayer :
    # Song 클래스를 상속하지 않은 이유는 불필요한 의존성이 있기 때문에 일부로 상속을 받지 않았다.
    # 예를 들어, 음악을 MusicPlayer 내에서 수정 하고 싶은데, 굳이 Song 클래스에서 상속을 받기 위해
    # super() 같은 호출 함수를 쓰면 코드가 직관적이지 않고 난해해지기 때문에 안썼다.

    # 음악들을 담을 리스트를 생성, 음악 재생 기능을 위한 is_Playing 필드 생성
    def __init__(self):
        self.song_list = []
        # 음악 정보들을 담을 리스트 생성
        self.is_Playing = False
        # 음악 재생을 하려면 처음에 전원이 꺼진 상태에서 버튼을 눌러야 실행되는것처럼 값을 False 로 해놓음


    # 노래 추가 기능 메서드
    # song 이라는 필드에 Song클래스 내의 title,artist,file_path 기능들을 객체로 담으면서
    # 값을 전달받을 수 있다. (굳이 상속을 쓸 필요 x, add_song 메서드 내에서 충분히 활용을 할 수 있고 불필요한
    # 의존성을 줄여주니깐)
    def add_song(self, title, artist, file_path):
        try : # 혹시 몰라서 예외 처리를 해두었다.
            song = Song(title, artist, file_path)
            self.song_list.append(song)
            print_song_added(song)
            # 노래가 성공적으로 추가되었을때, 사용자에게 메시지를 출력하는 함수
            # 사용한 이유 : 코드를 모듈화 하여 가독성을 높이고,
            # 같은 메시지를 여러곳에서 출력해야 할때 중복을 피하기 위해서
        except Exception as e :
            print(e)
    def play_song(self):
        if not self.song_list:
            # 만약 노래 리스트에 존재 하지 않다면

            print_no_songs()
            # 재생할 노래가 없습니다. 메세지 출력

        else :
            song = self.song_list[0]
            # 첫 번째 노래를 재생하도록 한다.
            print_song_playing()
            # 노래 재생중... 메세지 출력
            self.is_Playing = True
            # 재생을 한다면
            pygame.mixer.init()
            # pygame 음악 서비스 기능을 구현한다.
            pygame.mixer.music.load(song.file_path)
            # 입력받은 노래 경로를 통해서 음악을 전달받는다.
            pygame.mixer.music.play()
            # 음악이 실행된다.

    def pause_song(self):
        if self.is_Playing :
            # 음악이 재생되고 있는 상태일때
            pygame.mixer.music.pause()
            # pygame 음악 중지
            print_song_paused()
            #"노래 일시 중지" 메세지 출력
            self.is_Playing = False
            # 실제로 일시중지됨
        else :
            print_song_paused()
            # print("노래 일시 중지") << 원래부터 음악이 재생되고 있지 않았을때 그냥 출력

    def search_song(self,keyword):
        try :
            found_songs = [song for song in self.song_list if keyword.lower()
                          in song.title.lower() or keyword.lower()
                          in song.artist.lower()]
            print_search_result(found_songs)
        except Exception as e :
            print(e)

    def delete_song(self,title):
        for song in self.song_list :
            if title.lower() == song.title.lower():
                self.song_list.remove(song)
                print_song_deleted(song)
                break
        else :
            print_song_not_found(title)
    def show_songs(self):
         print(self.song_list)


