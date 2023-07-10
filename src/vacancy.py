import json


class Vacancy:
    """класс для работы с вакансиями"""

    def __init__(self, name, link, area, salary, requirement) -> None:
        self.name = name  # название вакансии
        self.link = link  # сылка на вакансию
        self.area = area  # местоположение
        self.salary = salary  # средняя заработная плата
        self.requirement = requirement  # требования к вакансии

    def __str__(self) -> str:
        return json.dumps(self.__dict__, ensure_ascii=False, indent=4)

    def __gt__(self, other):
        """метод для сравнения вакансий между собой по средней зарплате"""
        return self.salary > other.salary
