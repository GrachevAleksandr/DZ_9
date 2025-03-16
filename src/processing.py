from mypy.types import AnyType


def filter_by_state(list_state: list, state: str = "EXECUTED") -> list:
    """
    принимает список словарей и опционально значение для ключа state(по умолчанию
    'EXECUTED'). Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению.
    """
    if len(list_state) == 0:  # Проверка на пустую строку
        raise ValueError("Нет данных")
    new_list = []
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
    if reverse is True:
        return sorted(list_state, key=lambda x: x["date"], reverse=True)
    else:
        return sorted(list_state, key=lambda x: x["date"])

