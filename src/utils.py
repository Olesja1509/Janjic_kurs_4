import json


def open_file():
    """Открывает файл с вакансиями для чтения"""
    with open('filtered_vacancy.json', 'r', encoding='utf-8') as f:
        return json.load(f)


def use_platforms(user_input):
    """Функция для выбора платформы для поиска вакансий
    user_input = 'Введите платформы, с которых хотите получать дынне:
                           0 - hh и superjob
                           1 - hh
                           2 - superjob)"""
    used_platforms = []
    for vacancy in open_file():
        if user_input == "0":
            return open_file()
        elif user_input == "1":
            if vacancy["link"][:13] == "https://hh.ru":
                used_platforms.append(vacancy)
        elif user_input == "2":
            if vacancy["link"][:23] == "https://api.superjob.ru":
                used_platforms.append(vacancy)
    return used_platforms


def get_top_vacancies(filtered_vacancies, top_user_input):
    """Получение топ 10 вакансий по зп"""
    sorted_vacancies = sorted(filtered_vacancies, key=lambda x: x['salary'], reverse=True)
    for i in sorted_vacancies[:int(top_user_input)]:
        print(i)


def filter_vacancies(vacancies_by_platforms: list, filter_word: str):
    """Фильтрация вакансии по ключевым словам"""
    filtred_vacancies = []
    for vacancy in vacancies_by_platforms:
        values_list = list(vacancy.values())
        for value in values_list:
            if filter_word.lower() in str(value).lower():
                filtred_vacancies.append(vacancy)

    for i in filtred_vacancies:
        print(i)

    if len(filtred_vacancies) == 0:
        print('Нет вакансий, соответствующих заданным критериям.')
