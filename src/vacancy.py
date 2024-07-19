class Vacancy:
    """Класс для организации данных по вакансиям в удобном виде. хранит в себе полезные атрибуты по вакансиям"""

    def __init__(self, id, name, alternate_url, salary, requirement):
        """ Конструктор класса """

        self.id = id
        self.name = name
        self.alternate_url = alternate_url
        self.salary = salary
        self.requirement = requirement

    def __lt__(self, other):
        """ Метод сравнения зарплат """

        if self.salary is not None and other.salary is not None:
            return self.salary < other.salary

    def __str__(self):
        """ Строковое представление вакансии """

        return (f'ID вакансии: {self.id}\n'
                f'Наименование вакансии: - {self.name}\n'
                f'Ссылка на вакансию {self.alternate_url}\n'
                f'Зарплата от - {self.salary},\n'
                f'Краткое описание: {self.requirement}\n')
