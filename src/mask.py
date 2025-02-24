from typing import Union


def get_mask_account(account: Union[str, int]) -> str:
    """
    Функция принимает на вход номер счета и возвращает его маску.
    """
    mask_account = str(account)
    return f"**{mask_account[-4:]}"


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """
    Функция принимает на вход номер карты и возвращает ее маску.
    """
    n = str(card_number)
    return f"{n[0:4]} {n[4:6]}** **** {n[-4:]}"
