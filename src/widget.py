from src.mask import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """
    которая умеет маскировать информацию как о картах, так и о счетах.
    """
    card = account_card.split()  # ['Visa', 'Classic', '1234567890123456']
    if len(card[-1]) == 20:
        card[-1] = get_mask_account(card[-1])
        return " ".join(card)  # Счет **9589
    else:
        card[-1] = get_mask_card_number(card[-1])
        return " ".join(card)  # Visa Classic 6831 98** **** 7658
# def mask_account_card(account_card: str) -> str:
#     name, number = account_card.rsplit(maxsplit=1)
#     if name.lower().startswith('счет'):
#         hidden_number = get_mask_account(number)
#     else:
#         hidden_number = get_mask_card_number(number)
#     return f"{name} {hidden_number}"


def get_date(date: str) -> str:
    """
    которая принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ"("11.03.2024").
    """
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"

