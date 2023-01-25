import requests

def get_github_users(location: str, count: int = 100):
    # Отправляем GET запрос на URL для поиска пользователей на GitHub с указанной локацией
    # и максимальным количеством возвращаемых результатов
    response = requests.get(f'https://api.github.com/search/users?q=location:{location}&per_page={count}')
    # Парсим ответ в формате JSON
    data = response.json()
    # Возвращаем список найденных пользователей
    return data['items']

def print_usernames(users):
    # Печатаем имена пользователей из списка
    for user in users:
        print(user['login'])

# Ищем пользователей с локацией "Kyrgyzstan"
users = get_github_users('Kyrgyzstan')
# Печатаем их имена
print_usernames(users)



# Этот код использует библиотеку requests для отправки GET запроса на API GitHub, и поиска пользователей по локации. 

# Он отправляет запрос на API GitHub с параметрами локации и максимального количества возвращаемых результатов, 
# и разбирает полученный ответ в формате JSON. 
# Затем он вызывает функцию print_usernames, которая функция печатает имена пользователей из списка.

# В конце кода вызывается функция get_github_users с аргументом 'Kyrgyzstan' для поиска пользователей с этой локацией, 
# затем результат передается в функцию print_usernames для печати их имен.
