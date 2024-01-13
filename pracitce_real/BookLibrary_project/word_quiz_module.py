

# --------------------------
# 1. 단어 추가
# 2. 단어 삭제
# 3. 문제 풀기
# --------------------------
# 메뉴 선택 : (번호 입력)


word_dict = {}
def insert(word,word1):
    global word_dict
    if word not in word_dict:
        word_dict[word] = word
        if word1 not in word_dict:
            word_dict[word] = word1
            print("모두 추가되었습니다 ! ")
    else :
        print("중복된 단어 입니다.")
def delete(word):
    global word_dict
    if word in word_dict:
        del word_dict[word]
        print("삭제가 완료되었습니다 !")
    else :
        print("해당되는 단어가 없습니다.")
def solution():
    global word_dict

    for i in word_dict:
        print(word_dict[i])
        word = input("뜻을 입력하세요 : ")
        if word not in word_dict:
            print("틀렸습니다 ㅜㅜ")


        else :
            print("축하합니다 정답입니다 !")


