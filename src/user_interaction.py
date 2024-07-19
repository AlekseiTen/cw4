from src.connector import JsonConnector
from prettytable import PrettyTable


def start_user_interaction(connector: JsonConnector):
    while True:
        print(
            'Действия:\n',
            '1. Получить топ вакансий\n',
            '0. Выйти'
        )
        user_command = input()

        if user_command == '1':
            additional_parameter = int(input("Введите желаемую стартовую сумму: "))
            print_top_vacancies("salary_from", additional_parameter)
        elif user_command == '0':
            return


def print_top_vacancies(*args):
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))

    vacancies = JsonConnector()
    info = vacancies.load_file(*args)

    t = PrettyTable(['Номер вакансии', 'Название', 'Ссылка', 'Зарплата, от', 'Зарплата, до'])

    for vac in info[:top_n]:
        t.add_row([vac['id'], vac['name'], vac['url'], vac['salary_from'], vac['snippet_requirement']])
    print(t)
