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
            vacancy = response.json()['items']
            self.vacancies.extend(vacancy)
            self.params['page'] += 1

        return self.vacancies

    def parse_vacancies(self, vacancies: list[dict]) -> list[dict]:
        """ Метод фильтрует с API по заданным ключам и возвращает список словарей """

        items = []

        for i in vacancies:
            vacancy_id = i.get('id')
            vacancy_name = i.get('name')
            salary_dict = i.get('salary')
            salary_from = salary_dict.get('from')
            if salary_from is None:
                salary_from = 0
            vacancy_url = i.get('alternate_url')

            snippet_dict = i.get('snippet')
            snippet_requirement = snippet_dict.get('requirement')
            if snippet_requirement:
                snippet_requirement = snippet_requirement.replace('<highlighttext>', '').replace('</highlighttext>', '')
            else:
                snippet_requirement = 'нет требований'

            dict = {'vacancy_id': vacancy_id,
                    'vacancy_name': vacancy_name,
                    'vacancy_url': vacancy_url,
                    'salary_from': salary_from,
                    'snippet_requirement': snippet_requirement}
            items.append(dict)

        return items


if __name__ == "__main__":
    hh_api = HH()
    hh_api.load_vacancies('python')
    load_vac = hh_api.vacancies
    #load_vac = hh_api.load_vacancies('python')
    parse = hh_api.parse_vacancies(load_vac)

    print(*parse, sep='\n')


