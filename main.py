from src.api import HH
from src.connector import JsonConnector

from src.utils import sort_by_salary, filter_by_salary_range


file_path = 'C:\\Users\\Victus\\PycharmProjects\\CW4\\data\\vacancies.json'


def main():
    hh_api = HH()  # Создаем экземпляр API для работы с вакансиями
    jsVac = JsonConnector()  # Создаем экземпляр для работы с JSON-файлами

    print('Добро пожаловать в программу')  # Приветствие пользователя
    search_text = input('Введите текст для поиска вакансий: ')  # Запрашиваем текст для поиска вакансий у пользователя

    load_vac = hh_api.load_vacancies(search_text)  # Загружаем вакансии с помощью API на основе введенного текста
    parse = hh_api.parse_vacancies(load_vac)  # Парсим загруженные вакансии для извлечения нужной информации

    save_data = jsVac.save_vacancies(parse)  # Сохраняем распарсенные данные в JSON-файл
    load_vac_data = jsVac.load_file(file_path)  # Загружаем данные из сохраненного JSON-файла
    # deleted = jsVac.del_vacancy(load_vac_data, "104857154") УДАЛЯЕМ ВАКАНСИЮ, НЕ ИСПОЛЬЗУЕМ. ЗА НЕНАДОБНОСТЬЮ

    vac_obj_list = jsVac.create_vacancy_list(load_vac_data)  # Создаем список объектов вакансий из загруженных данных

    salary_range = input('Введите диапазон зарплат (через пробел): ')  # Запрашиваем у пользователя диапазон зарплат
    splitted_range = salary_range.split(' ')  # Разделяем введенный диапазон на минимальную и максимальную зарплату

    # Фильтруем список вакансий по введенному диапазону зарплат
    filtred_salary_by_range = filter_by_salary_range(vac_obj_list, *splitted_range)

    # Запрашиваем количество вакансий для вывода пользователю
    top_n = input('Введите количество для вывода топ-N вакансий: ')

    # Сортируем отфильтрованные вакансии по зарплате и выбираем топ-N
    sorted_top_salary = sort_by_salary(filtred_salary_by_range, top_n)

    # Выводим отсортированные вакансии на экран
    print(*sorted_top_salary, sep='\n')


# Запуск основной функции, если файл выполняется как основной
if __name__ == "__main__":
    main()
