from src.class_api import HeadHunterAPI, SuperJobAPI
from src.class_json import JSONSaver
from src.utils import get_top_vacancies, add_hh_vacancies, add_superjob_vacancies


def user_interaction():

    # Создание экземпляра класса для работы с API сайтов с вакансиями
    hh_api = HeadHunterAPI()
    superjob_api = SuperJobAPI()

    #  Поиск по ключевому слову
    key_word = input("Введите ключевое слово для поиска вакансий: \n")

    #  Выбор платформы для поиска вакансий
    while True:
        user_input = input('Введите платформы, с которых хотите получать дынне:\n'
                           '0 - hh и superjob\n'
                           '1 - hh\n'
                           '2 - superjob\n')
        if user_input == "0":
            hh_vacancies = hh_api.get_vacancies(key_word)
            superjob_vacancies = superjob_api.get_vacancies(key_word)
            hh_vacancies_list = add_hh_vacancies(hh_vacancies)
            superjob_vacancies_list = add_superjob_vacancies(superjob_vacancies)
            vacancies_list = hh_vacancies_list + superjob_vacancies_list
            break
        elif user_input == "1":
            hh_vacancies = hh_api.get_vacancies(key_word)
            hh_vacancies_list = add_hh_vacancies(hh_vacancies)
            vacancies_list = hh_vacancies_list
            break
        elif user_input == "2":
            superjob_vacancies = superjob_api.get_vacancies(key_word)
            superjob_vacancies_list = add_superjob_vacancies(superjob_vacancies)
            vacancies_list = superjob_vacancies_list
            break
        else:
            print('Введены некорректные данные')

    #  Сохранение в файл 'filtered_vacancy.json' всех вакансий по Выбранному городу
    json_saver = JSONSaver()
    city = input('Введите город для поиска вакансий\n')
    filtered_vacancies = json_saver.get_vacancies_by_city(vacancies_list, city)
    json_saver.add_vacancy(filtered_vacancies)
    json_saver.delete_vacancy(filtered_vacancies, "https://hh.ru/vacancy/83091712")

    #  Получение топ вакансий по зп
    top_user_input = int(input('Введите количество вакансий для вывода в топ\n'))
    get_top_vacancies(filtered_vacancies, top_user_input)


if __name__ == "__main__":
    user_interaction()
