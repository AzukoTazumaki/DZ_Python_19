from faker import Faker
from operator import itemgetter


class Exercises:
    @staticmethod
    def ex_1(sort_and_name: list) -> list:
        fake = Faker('ru_RU')
        list_names_1 = [fake.first_name() for _ in range(100)]
        list_names_2 = [fake.first_name() for _ in range(100)]
        list_names_3 = [fake.first_name() for _ in range(100)]
        list_names_4 = [fake.first_name() for _ in range(100)]
        result_list = list_names_1 + list_names_2 + list_names_3 + list_names_4
        search_name = ''
        if sort_and_name[0] == 'sort_asc':
            result_list.sort()
        elif sort_and_name[0] == 'sort_desc':
            result_list.sort(reverse=True)
        for name in result_list:
            if name.lower() == sort_and_name[1].lower():
                search_name = 'Имя присутствует в списке.'
                return [result_list, search_name]
            search_name = 'Имя отсутствует в списке.'
        return [result_list, search_name]

    @staticmethod
    def ex_2(sort_and_name: list) -> list:
        fake = Faker('ru_RU')
        list_jobs_1 = [fake.job() for _ in range(100)]
        list_jobs_2 = [fake.job() for _ in range(100)]
        list_jobs_3 = [fake.job() for _ in range(100)]
        list_jobs_4 = [fake.job() for _ in range(100)]
        result_list = list_jobs_1 + list_jobs_2 + list_jobs_3 + list_jobs_4
        sorted_list = sorted(result_list)
        if sort_and_name[0] == 'sort_asc':
            result_list.sort()
        elif sort_and_name[0] == 'sort_desc':
            result_list.sort(reverse=True)

        left = 0
        right = len(result_list) - 1

        while left <= right:
            center = (left + right) // 2
            if sort_and_name[1].lower() == sorted_list[center].lower():
                search_job = 'Профессия присутствует в списке.'
                return [result_list, search_job]
            if sort_and_name[1].lower() > sorted_list[center].lower():
                left = center + 1
            else:
                right = center - 1
        else:
            search_job = 'Профессия отсутствует в списке.'
        return [result_list, search_job]
