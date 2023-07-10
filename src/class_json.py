from abc import ABC, abstractmethod
import json


class FILESaver(ABC):
    """Абстактный класс для обавления вакансий в файл"""

    @abstractmethod
    def add_vacancy(self, vacancy):
        """метод для добавления вакансий в файл"""
        pass

    @abstractmethod
    def get_vacancies_by_city(self, vacancy_list, city):
        """метод для получения данных из файла по указанным критериям"""
        pass

    @abstractmethod
    def delete_vacancy(self, list_vacancies, link_vacancy):
        """метод для  удаления информации о вакансиях"""
        pass


class JSONSaver(FILESaver):

    def add_vacancy(self, vacancy_list):
        with open('filtered_vacancy.json', 'w', encoding='utf-8') as f:
            json.dump(vacancy_list, f, indent=4, ensure_ascii=False)

    def get_vacancies_by_city(self, vacancy_list, city):
        city_vacancies = []
        for vacancy in vacancy_list:
            vacancy = json.loads(vacancy)
            if vacancy["area"] == city:
                city_vacancies.append(vacancy)
        return city_vacancies

    def delete_vacancy(self, list_vacancies, link_vacancy):
        for vac in list_vacancies:
            if vac["link"] == link_vacancy:
                list_vacancies.remove(vac)

        with open('filtered_vacancy.json', 'w', encoding='utf-8') as f:
            json.dump(list_vacancies, f, indent=4, ensure_ascii=False)
