from src.api import HH
from src.connector import JsonConnector
from src.user_interaction import start_user_interaction

VACANCIES_PATH = "../CW4/data/vacancies.json"
api_client = HH()
connector = JsonConnector()


def main():
    print('Добро пожаловать в программу')
    search_text = input('Введите текст для поиска вакансий: ')

    print('Получаем вакансии...')
    vacancies = api_client.load_vacancies(search_text)
    parse = api_client.parse_vacancies(vacancies)

    print('Сохраняем в базу')
    connector.save_vacancies(parse, VACANCIES_PATH)

    start_user_interaction(connector)


if __name__ == "__main__":
    main()
