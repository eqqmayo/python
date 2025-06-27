# key: value로 구분
user = {'name': 'Calia', 'city': 'Seoul'}
print(user)

user['city'] = 'Busan'
print(user['city'])
print(user)

user['car'] = 'Tesla'
print(user)

user['car'] = ''
print(user)


# 특정 키를 지우는 키워드는 del
del user['car']
print(user)

print(user.keys)
print(user.values)
print(user.items)