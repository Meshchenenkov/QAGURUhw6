"""
Найдите нужного пользователя по условиям в списке пользователей
"""
users = [
    {"name": "Oleg", "age": 32},
    {"name": "Sergey", "age": 24},
    {"name": "Stanislav", "age": 15},
    {"name": "Olga", "age": 45},
    {"name": "Maria", "age": 18},
]



# TODO найдите всех пользователей младше 20 лет
suitable_users = list()
for user in users:
    if user['age'] < 20:
        suitable_users.append(user)
assert suitable_users == [
    {"name": "Stanislav", "age": 15},
    {"name": "Maria", "age": 18},
]


