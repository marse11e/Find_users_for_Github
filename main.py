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
