from connection_module import data_dict

def insert(**kwargs): # 추가
    '''

    :param kwargs: {'name': '상품명', 'price': 가격}
    '''
    name, price = kwargs.values()
    data_dict[name] = int(price)


def update(*, name, new_name, new_price): # 수정
    del data_dict[name]
    data_dict[new_name] = int(new_price)


def delete(name): # 삭제
    del data_dict[name]

def select_by_name(keyword): # 상품명(keyword)으로 검색
    result = {}
    if keyword in data_dict:
        result = {'name': keyword, 'price': data_dict[keyword]}

    return result

def select_by_price(price, range=50):
    result = []
    min = price * range * 0.01
    max = price * (range * 0.01 + 1)

    for name, price in data_dict.items():
        if min <= price <= max:
            result.append({'name': name, 'price': price})

    return result

def select_all():
    return data_dict