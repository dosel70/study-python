# https://ocr.space/OCRAPI
# K82277197388957
# https://api.ocr.space/parse/imageurl?apikey=&url=
# https://api.ocr.space/parse/imageurl?apikey=&url= &language= &isOverlayRequired=true
import requests
url = "https://api.ocr.space/parse/imageurl?apikey=K82277197388957&url=https://i.pinimg.com/474x/34/8b/c5/348bc51a10af4a96dea207318f88cc6b.jpg&language=kor&isOverlayRequired=true"
response = requests.get(url)
response.raise_for_status()

result = response.json()
print(response.json())
print(type(response.json())) # 딕셔너리 but json 그 자체의 타입은 문자열 형태
print(type(result))
print(result)
# OCR을 활용한 외부 API 사용
print(result['ParsedResults'][0]['ParsedText'])
first_item = result['ParsedResults'][0]
print(first_item)
# 활용 예제 >> 회원가입 ( 증명서, 주민등록증  등등을 첨부해야할때)
