from typing import Union


def get_mask_account(account: Union[str, int]) -> str:
    """
    Функция принимает на вход номер счета и возвращает его маску.
    """
    str_account = str(account)
    if str_account.isdigit() is not True:  # Проверка не цифры
        raise ValueError("Неверный номере")
    if len(str_account) != 20:  # Проверка на количество цифр
        raise ValueError("Неверный номер")
    return f"**{str_account[-4:]}"


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """
    Функция принимает на вход номер карты и возвращает ее маску.
    """
    str_card_number = str(card_number)
    if str_card_number.isdigit() is not True:  # Проверка не цифры
        raise ValueError("Неверный номер")
    if len(str_card_number) != 16:  # Проверка на количество цифр
        raise ValueError("Неверный номер")
    return f"{str_card_number[0:4]} {str_card_number[4:6]}** **** {str_card_number[-4:]}"
