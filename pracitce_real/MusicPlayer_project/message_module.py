def display_menu():
    print("1. 음악 추가")
    print("2. 음악 재생")
    print("3. 음악 중지")
    print("4. 음악 검색")
    print("5. 음악 삭제")
    print("6. 플레이리스트")
    print("7. 프로그램 종료")

def print_song_added(song):
    print(f"노래 추가: {song}")

def print_song_playing():
    print("노래 재생 중...")

def print_song_paused():
    print("노래 일시 중지")

def print_no_songs():
    print("재생할 노래가 없습니다.")

def print_search_result(found_songs):
    if found_songs:
        print("검색 결과 : ")
        for song in found_songs:
            print(song)
    else:
        print("검색 결과가 없습니다.")

def print_song_deleted(song):
    print(f"{song}이 삭제 되었습니다.")

def print_song_not_found(title):
    print(f"{title}에 해당하는 노래를 찾을 수 없습니다.")