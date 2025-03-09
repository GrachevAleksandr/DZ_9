def filter_by_state(list_state: list, state="EXECUTED") -> list:
    """
    принимает список словарей и опционально значение для ключа state(по умолчанию
    'EXECUTED'). Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению.
    """
    new_list = []
    for element in list_state:
        for key, value in element.items():
            if value == state:
                new_list.append(element)

    return new_list


def sort_by_date(list_state: list, type_of_sorting="decreasing") -> list:
    """
    принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание). Функция должна возвращать новый список, отсортированный
    по дате (date).
    """
    if type_of_sorting == "decreasing":
        return sorted(list_state, key=lambda x: x["date"], reverse=True)
    else:
        return sorted(list_state, key=lambda x: x["date"])
