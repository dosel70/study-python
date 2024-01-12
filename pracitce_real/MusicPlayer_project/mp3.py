import pygame

from mp3_module import MusicPlayer
from message_module import display_menu

if __name__ == '__main__':
    player = MusicPlayer()

    #MusicPlayer 클래스 기능을 담은 player 객체

    while True :
        display_menu()
        choice = input("메뉴를 선택해주세요(1-6) : ")
        if choice == '1': # 음악 추가
            title = input("노래 제목 : ")
            artist = input("가수명 : ")
            file_path = input("노래 파일 경로 : ")
            player.add_song(title, artist, file_path)

        elif choice =='2': # 음악 재생
            player.play_song() # 노래 재생

        elif choice =='3': # 음악 중지
            player.pause_song()

        elif choice =='4': # 음악 검색
            keyword = input("검색할 음악 제목 : ")
            player.search_song(keyword)

        elif choice == '5': # 음악 삭제
            title = input("삭제할 음악 제목 : ")
            player.delete_song(title)

        elif choice == '6':
           for title , artist in player.song_list :
               print(f'{title} - {artist}')


        elif choice == '7': # 프로그램 종료
            print("프로그램 종료")
            pygame.mixer.quit()
            # 프로그램을 종료하면 pygame mixer 종료


        else :
            print("올바르지 않은 선택입니다. 1번부터 5까지의 숫자중 선택해주세요 : ")


