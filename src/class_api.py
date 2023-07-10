import requests
import os

from abc import ABC, abstractmethod


class API(ABC):
    """Абстактный класс для работы с API сайтов с вакансиями"""

    @abstractmethod
    def get_vacancies(self, keyword):
        pass


class HeadHunterAPI(API):
    """Класс для работы с API сайта hh.ru"""

    def get_vacancies(self, keyword):
        url = 'https://api.hh.ru/vacancies'
        params = {'text': keyword, 'per_page': 100}

        req = requests.get(url, params=params)
        data = req.content.decode()
        req.close()
        return data


class SuperJobAPI(API):
    """Класс для работы с API сайта superjob.ru"""

    def get_vacancies(self, keyword):
        api_key: str = os.getenv('SUPERJOB_API_KEY')
        params = {'keyword': keyword, 'per_page': 100, 'count': 100}
        headers = {'X-Api-App-Id': api_key}
        url = 'https://api.superjob.ru/2.0/vacancies/'

        req = requests.get(url, params=params, headers=headers)
        data = req.content.decode()
        req.close()
        return data
