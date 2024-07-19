import json
from abc import ABC, abstractmethod
from src.vacancy import Vacancy

file_path = "../CW4/data/vacancies.json"


class Connector(ABC):

    @abstractmethod
    def load_file(self, key_name: str, value_name: str | int) -> list:
        pass

    @abstractmethod
    def save_vacancies(self):
        pass

    @abstractmethod
    def del_vacancy(self):
        pass


class JsonConnector(Connector):
    def __init__(self) -> None:
        self._finish_list = []

    def load_file(self, key_name, value_name, filename=file_path):
        """Загружает данные из файла JSON"""
        with open(filename, 'r', encoding='utf-8') as file:
            top_list = json.load(file)

        top_ = sorted(top_list, key=lambda x: x[key_name], reverse=True)

        for item in top_:
            if value_name == item[key_name]:
                self._finish_list.append(item)

        return self._finish_list

    def create_vacancy_list(self, list_) -> list:
        """
        Метод класса для формирования списка вакансий по новому
        :return: список вакансий после обработки классом Vacancy
        """
        new_list = []
        for item in list_:
            new_list.append(Vacancy(item["id"],
                                    item["name"],
                                    item["url"],
                                    item["salary_from"],
                                    item["snippet_requirement"]))

        return new_list

    def save_vacancies(self, vacancies_list, filename=file_path):
        """сохраняет экземпляры вакансий в файл"""
        new_list = []
        list_class = self.create_vacancy_list(vacancies_list)
        for item in list_class:
            new_dict = {'id': item.id,
                        'name': item.name,
                        'url': item.alternate_url,
                        'salary_from': item.salary,
                        'snippet_requirement': item.requirement}

            new_list.append(new_dict)

        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(new_list, file, ensure_ascii=False, indent=4)

    def del_vacancy(self, vacancies_list: list[dict], id: str):
        """Удаляет вакансию по id"""
        new_list = []
        for vac in vacancies_list:
            if vac['id'] != id:
                new_list.append(vac)
            else:
                print(f'Вакансия с id {id} удаленна')
        return new_list

# api_hh = HH()
# jsVac = JsonConnector()
# vacancies = api_hh.load_vacancies('python')
# parse = api_hh.parse_vacancies(vacancies)
# print(jsVac.save_vacancies(parse, file_path))


# data = jsVac.load_file()
# jsVac.del_vacancy(data)

# vacancies = [{'id': '1', 'title': 'Developer'}, {'id': '2', 'title': 'Designer'}]
# new_vacancy = {'id': '1', 'title': 'Senior Developer'}
#
# updated_vacancies = add_vacancy(vacancies, new_vacancy)
# print(updated_vacancies)
