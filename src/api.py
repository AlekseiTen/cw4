from abc import ABC, abstractmethod
import requests


class Parser(ABC):
    """
    Абстрактный класс для работы с API
    """

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def load_vacancies(self, keyword):
        pass


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом
    """

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '',
                       'page': 0,
                       'only_with_salary': True,
                       'per_page': 20}
        self.vacancies = []

    def load_vacancies(self, keyword):
        """загружает данные c АПИ"""
        self.params['text'] = keyword
        while self.params.get('page') != 5:
            response = requests.get(self.url, headers=self.__headers, params=self.params)
            response.raise_for_status()
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
        return self.vacancies

    def parse_vacancies(self, vacancies: list[dict]) -> list[dict]:
        """ Метод фильтрует с API по заданным ключам и возвращает список словарей """

        items = []

        for i in vacancies:
            id = i.get('id')
            name = i.get('name')
            salary_dict = i.get('salary')

            salary_from = salary_dict.get('from')
            if salary_from is None:
                salary_from = 0

            url = i.get('alternate_url')

            snippet_dict = i.get('snippet')
            snippet_requirement = snippet_dict.get('requirement')
            if snippet_requirement:
                snippet_requirement = snippet_requirement.replace('<highlighttext>', '').replace('</highlighttext>', '')
            else:
                snippet_requirement = 'нет требований'

            dict = {'id': id,
                    'name': name,
                    'url': url,
                    'salary_from': salary_from,
                    'snippet_requirement': snippet_requirement}
            items.append(dict)

        return items


# hh_api = HH()
# load_vac = hh_api.load_vacancies('python')
# parse = hh_api.parse_vacancies(load_vac)
# print(type(parse))
