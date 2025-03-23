from typing import Iterator


def filter_by_currency(transactions: list[dict], currency_type: str) -> list[dict]:
    """
    которая принимает на вход список словарей, представляющих транзакции.
     :return: Функция должна возвращать итератор, который поочередно выдает транзакции,
     где валюта операции соответствует заданной (например, USD).
    """
    transactions_iter = iter(transactions)
    return list(
        i for i in transactions_iter if currency_type == i.get("operationAmount", {}).get("currency", {}).get("code")
    )


def transaction_descriptions(transactions: list[dict], key: str = "description") -> Iterator[str]:
    """
    Функция возвращает список описаний транзакций
    """
    list_transactions = transactions
    description = ""
    for x in list_transactions:
        descript = description + x["description"]
        yield str(descript)


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    который выдает номера банковских карт в формате 'XXXX''XXXX''XXXX''XXXX', где 'X'— цифра номера карты.
    Генератор может сгенерировать номера карт в
    заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    """
    numbers = range(start, stop + 1)
    card_number_low = "0000000000000000"
    for x in numbers:
        if len(str(x)) >= 17:
            yield ValueError
        card_number = card_number_low[: -len(str(x))] + str(x)
        yield f"{card_number[0:4]} {card_number[4:8]} {card_number[8:12]} {card_number[-4:]}"
