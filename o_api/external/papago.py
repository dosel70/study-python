import requests
# id : Bv9_0vus1XYI_3dFSY0u
# pw : yog6tEBH4s



import urllib.request
import json

# import ssl
#
# ssl._create_default_https_context = ssl._create_unverified_context # 강제 되는 보안을 꺼서 url 요청을 받을 수 있게 한다.
# 보안이 강한 컴퓨터 설정의 경우 사용!

client_id = "Bv9_0vus1XYI_3dFSY0u"
client_secret = "yog6tEBH4s"
encoding_text = urllib.parse.quote("안녕하세요, 제 이름은 조성현입니다.")
data = f"source=ko&target=en&text={encoding_text}"
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)

# -H
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()

if rescode == 200:
    response = json.loads(response.read().decode("utf-8"))
    print(response['message']['result']['translatedText'])
