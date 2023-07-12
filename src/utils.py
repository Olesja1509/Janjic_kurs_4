import json
from src.vacancy import Vacancy


def get_top_vacancies(filtered_vacancies, top_user_input):
    """Получение топ 10 вакансий по зп"""
    sorted_vacancies = sorted(filtered_vacancies, key=lambda x: x['salary'], reverse=True)
    for i in sorted_vacancies[:int(top_user_input)]:
        print(i)


def add_hh_vacancies(hh_vacancies):
    """Перебор данных о вакансиях с hh и инициализируем вакансии как класс Vacancy"""
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
    return hh_vacancies_list


def add_superjob_vacancies(superjob_vacancies):
    """Перебор данных о вакансиях с superjob и инициализируем вакансии как класс Vacancy"""
    superjob_vacancies_dict = json.loads(superjob_vacancies)["objects"]
    superjob_vacancies_list = []

    for vacancy in superjob_vacancies_dict:
        name = vacancy["profession"]
        link = 'https://api.superjob.ru/2.0/vacancies/' + str(vacancy["id"])
        area = vacancy["town"]["title"]

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
    return superjob_vacancies_list
