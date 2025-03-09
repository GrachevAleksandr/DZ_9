def filter_by_state(data_lists : list, state="EXECUTED") -> list:
    """
    принимает список словарей и опционально значение для ключа state(по умолчанию
    'EXECUTED'). Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению.
    """
    new_list = []
    for element in data_lists:
        for key, value in element.items():
            if value == state :
                new_list.append(element)

    return new_list


def sort_by_date(data_lists : list, type_of_sorting="decreasing") -> list:
    """
    принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание). Функция должна возвращать новый список, отсортированный
    по дате (date).
    """
    if type_of_sorting == "decreasing":
        return  sorted(data_lists, key=lambda x: x["date"], reverse=True)
    else:
        return sorted(data_lists, key=lambda x: x["date"])

