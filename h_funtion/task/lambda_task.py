

# 'aPPle', 'BananA', 'meLON'을 모두 소문자로 변경
# words = ['aPPle', 'BananA', 'meLON']
#
# lower_words = list(map(lambda x: x.lower(), words))
#
# print(lower_words)



# 입력받은 한글을 정수로 변경

# korea = '공일이삼사오육칠팔구'
# data = 3519

# print(int("".join(list(map(lambda s: str(korea.index(s)),data)))))
# print("".join(list(map(lambda s : korea[ord(s) - 48],str(data)))))

# # print(list(filter(lambda url: url.split('/') != 'user' , url)))
# url = ['user/join', 'user/login', 'post/write', 'order/pay', 'order/list', 'post/read']
# print(list(filter(lambda service: service != 'user', list(map(lambda url : url[:url.index("/")],url)))))
# 'game' 서비스를 제공하는 경로 찾기
# urls = ['/app/game', '/app/news', '/app/fashion', '/app/ranking']






# 입력받은 정수를 한글로 변경
# 입력 예: 3519
# 출력 예: 삼오일구

# 'user/join', 'user/login', 'post/write', 'order/pay', 'order/list', 'post/read'
# print(list(filter(lambda url: url.split('/')[-1] == 'game' , urls)))
# url = 'user/join', 'user/login', 'post/write', 'order/pay', 'order/list', 'post/read'
# print(list(map(lambda url : '/user' + url , url)))
# 'game' 서비스를 제공하는 경로 찾기
# urls = ['/app/game', '/app/news', '/app/fashion', '/app/ranking']

# print(list(filter(lambda number : number for i in range(len(urls).split('/game') + [len(urls)])
# print(list(filter(lambda url: url.split('/') != 'user' , url)))
# print(list(map(lambda url: url.split('user') and url.split('user')[-1] , url)))

# 'aPPle', 'BananA', 'meLON'을 모두 소문자로 변경
# fruits = ['aPPle', 'BananA', 'meLON']
# result = list(map(lambda fruit: fruit.lower(), fruits))
# print(result)
#
# # 입력받은 한글을 정수로 변경
# # 입력 예: 삼오일구
# # 출력 예: 3519
hangul = "공일이삼사오육칠팔구"
data = "삼오일구"
#
print(int("".join(list(map(lambda s: str(hangul.index(s)), data)))))







# 입력받은 정수를 한글로 변경
# 입력 예: 3519
# 출력 예: 삼오일구
hangul = "공일이삼사오육칠팔구"
data = 8975 # 리스트 ㄴㄴ 그래서 이걸 str으로 형변환 시켜줘야함
# 풀이 순서 : data를 변환시켜야함 무엇으로?? 한글로(문자열)
print("".join(list(map(lambda s: hangul[int(s)],str(data)))))


print(type(str(data)))
print("".join(list(map(lambda s: hangul[int(s)], str(data)))))
# print("".join(list(map(lambda s: hangul[ord(s) - 48], str(data)))))

url =  'user/join', 'user/login', 'post/write', 'order/pay', 'order/list', 'post/read'
# 위 경로 중 회원 서비스가 아닌 경로만 추출
# 1. 서비스명(user, post, order)으로 변경(map)
list(map(lambda x : x.split("/"),url))

# 2. 서비스명 중 'user'가 아닌 경로만 추출(filter)
# 출력 예시
# ['post', 'order', 'order', 'post']
urls = ['user/join', 'user/login', 'post/write', 'order/pay', 'order/list', 'post/read']

print(list(filter(lambda service: service != 'user',
                  list(map(lambda url: url[:url.index("/")], urls)))))

print(list(filter(lambda service : service != 'order',
                  list(map(lambda url : url[:url.index("/")], urls)))))

print(list(map(lambda url:url[:url.index("/")], urls)))

print(list(filter(lambda url : url != 'user',urls)))