import json
from abc import ABC, abstractmethod

from src.api import HH
from src.vacancy import Vacancy

file_path = 'C:\\Users\\Victus\\PycharmProjects\\CW4\\data\\vacancies.json'


class Connector(ABC):

    @abstractmethod
    def load_file(self) -> list:
        pass

    @abstractmethod
    def save_vacancies(self):
        pass

    @abstractmethod
    def del_vacancy(self):
        pass


class JsonConnector(Connector):

    def create_vacancy_list(self, list_) -> list:
        """
        Метод для создания списка объектов класса Vacancy из списка словарей.
        """
        new_list = []
        for item in list_:
            create_vac_obj = Vacancy(item["vacancy_id"], item["vacancy_name"], item["vacancy_url"], item["salary_from"],
                                     item["snippet_requirement"])
            new_list.append(create_vac_obj)

        return new_list

    def save_vacancies(self, vacancies_list, filename=file_path):
        """сохраняет экземпляры вакансий в файл"""

        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(vacancies_list, file, ensure_ascii=False, indent=4)

    def load_file(self, filename=file_path):
        """Загружает данные из файла JSON"""

        with open(filename, 'r', encoding='utf-8') as file:
            top_list = json.load(file)
            return top_list

    def del_vacancy(self, vacancies_list: list[dict], id: str):
        """Удаляет вакансию по id"""
        new_list = []
        for vac in vacancies_list:
            if vac['id'] != id:
                new_list.append(vac)
            else:
                print(f'Вакансия с id {id} удаленна')
        return new_list


if __name__ == "__main__":
    hh_api = HH()
    load_vac = hh_api.load_vacancies('python')
    parse = hh_api.parse_vacancies(load_vac)

    jsVac = JsonConnector()
    jsVac.save_vacancies(parse)
    load_vac_data = jsVac.load_file()
    # deleted = jsVac.del_vacancy(load_vac_data, "104857154")
    vac_obj_list = jsVac.create_vacancy_list(load_vac_data)

    # print(save_vac)
