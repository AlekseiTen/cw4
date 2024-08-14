
def sort_by_salary(vacancies_obj_list: object, top_n):
    '''сортирует по зарплате'''
    sorted_vac = sorted(vacancies_obj_list, reverse=True)
    top_n_int = int(top_n)
    return sorted_vac[:top_n_int]


def filter_by_salary_range(vacancies_list: object, salary_min: int, salary_max: int):
    '''фильтрует по диапазону зарплат'''
    filtred_list = []
    s_min = int(salary_min)
    s_max = int(salary_max)

    for vacancy in vacancies_list:
        if s_min <= vacancy.salary <= s_max:
            filtred_list.append(vacancy)

    return filtred_list
