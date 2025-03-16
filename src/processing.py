def filter_by_state(list_state: list, state: str = "EXECUTED") -> list:
    """
    принимает список словарей и опционально значение для ключа state(по умолчанию
    'EXECUTED'). Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению.
    """
    if not list_state:  # Проверка на пустую строку
        raise ValueError("Нет данных")
    new_list = []
    state_key = "state"
    for element in list_state:
        state_value = element.get(state_key)
        if state_value is not None:
            if len(state_value) == 0:
                raise ValueError("Нет данных")
        else:
            raise ValueError("Нет данных")
    for element in list_state:
        for key, value in element.items():
            if value == state:
                new_list.append(element)
    return new_list


def sort_by_date(list_state: list, reverse: bool = True) -> list:
    """
    принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание). Функция должна возвращать новый список, отсортированный
    по дате (date).
    """
    if len(list_state) == 0:  # Проверка на пустую строку
        raise ValueError("Нет данных")
    date_key = "date"
    for element in list_state:
        for key, value in element:
            if date_key in element:
                if reverse is True:
                    return sorted(list_state, key=lambda x: x["date"], reverse=True)
                else:
                    return sorted(list_state, key=lambda x: x["date"])
            else:
                raise ValueError("Нет данных")
