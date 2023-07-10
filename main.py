from src.class_api import HeadHunterAPI, SuperJobAPI
from src.vacancy import Vacancy
from src.class_json import JSONSaver
from src.utils import use_platforms, get_top_vacancies, filter_vacancies
import json


# Создание экземпляра класса для работы с API сайтов с вакансиями
hh_api = HeadHunterAPI()
superjob_api = SuperJobAPI()

# Получение вакансий с разных платформ
hh_vacancies = hh_api.get_vacancies("Python")
superjob_vacancies = superjob_api.get_vacancies("Python")


#  Перебор полученных данных о вакансиях с hh и инициализируем вакансии как класс Vacancy
hh_vacancies_dict = json.loads(hh_vacancies)["items"]
hh_vacancies_list = []
for vacancy in hh_vacancies_dict:
    name = vacancy["name"]
    link = 'https://hh.ru/vacancy/' + vacancy["id"]
    area = vacancy["area"]["name"]

    salary = 0
    if vacancy["salary"] is not None:
        salary_from = vacancy["salary"]["from"]
        salary_to = vacancy["salary"]["to"]
        if salary_from is not None and salary_to is not None:
            salary = int((salary_from + salary_to) / 2)
        elif salary_from is not None:
            salary = salary_from
        elif salary_to is not None:
            salary = salary_to
    else:
        salary = 0

    requirement = vacancy["snippet"]["requirement"]
    vacancy = Vacancy(name, link, area, salary, requirement)
    hh_vacancies_list.append(vacancy.__str__())

#  Перебор полученных данных о вакансиях с hh и инициализируем вакансии как класс Vacancy
superjob_vacancies_dict = json.loads(superjob_vacancies)["objects"]
superjob_vacancies_list = []

for vacancy in superjob_vacancies_dict:
    name = vacancy["profession"]
    link = 'https://api.superjob.ru/2.0/vacancies/' + str(vacancy["id"])
    area = vacancy["town"]["title"]

    salary = 0
    if vacancy["payment_from"] > 0 and vacancy["payment_to"] > 0:
        salary = int((vacancy["payment_from"] + vacancy["payment_to"]) / 2)
    elif vacancy["payment_from"] > 0:
        salary = vacancy["payment_from"]
    elif vacancy["payment_to"] > 0:
        salary = vacancy["payment_to"]
    else:
        salary = 0

    requirement = vacancy["candidat"]
    vacancy = Vacancy(name, link, area, salary, requirement)
    superjob_vacancies_list.append(vacancy.__str__())


#  Сохранение в файл 'filtered_vacancy.json' всех вакансий по городу Москва
json_saver = JSONSaver()

city_vacancies_hh = json_saver.get_vacancies_by_city(hh_vacancies_list, "Москва")
city_vacancies_superjob = json_saver.get_vacancies_by_city(superjob_vacancies_list, "Москва")
city_vacancies = city_vacancies_hh + city_vacancies_superjob

json_saver.add_vacancy(city_vacancies)

json_saver.delete_vacancy(city_vacancies, "https://hh.ru/vacancy/83091712")


#  Функция для взаимодействия с пользователем
def user_interaction():
    while True:
        user_input = input('Введите платформы, с которых хотите получать дынне:\n'
                           '0 - hh и superjob\n'
                           '1 - hh\n'
                           '2 - superjob\n')
        if user_input == "0" or user_input == "1" or user_input == "2":
            vacancies_by_platforms = use_platforms(user_input)
            break
        else:
            print('Введены некорректные данные')

    #  Получение топ вакансий по зп
    top_user_input = input('Введите количество вакансий для вывода в топ\n')
    get_top_vacancies(vacancies_by_platforms, top_user_input)

    #  Поиск по ключевому слову
    filter_words = input("Введите ключевое слово для фильтрации вакансий: \n")
    filter_vacancies(vacancies_by_platforms, filter_words)


if __name__ == "__main__":
    user_interaction()
