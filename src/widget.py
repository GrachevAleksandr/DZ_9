from src.mask import get_mask_account
from src.mask import get_mask_card_number


def mask_account_cart(account_cart: str) -> str:
    """
    которая умеет обрабатывать информацию как о картах, так и о счетах.
    """
    if account_cart.find("Maestro") == 0:
        return f"{account_cart[0:7]} {get_mask_card_number(account_cart[8:])}"
    if account_cart.find("MasterCard") == 0:
        return f"{account_cart[0:10]} {get_mask_card_number(account_cart[11:])}"
    if account_cart.find("Visa Classic") == 0:
        return f"{account_cart[0:12]} {get_mask_card_number(account_cart[13:])}"
    if account_cart.find("Visa Gold") == 0:
        return f"{account_cart[0:9]} {get_mask_card_number(account_cart[10:])}"
    if account_cart.find("Visa Platinum") == 0:
        return f"{account_cart[0:13]} {get_mask_card_number(account_cart[14:])}"
    else:
        return f"{account_cart[0:4]} {get_mask_account(account_cart[5:])}"


def get_date(date: str) -> str:
    """
    которая принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ"("11.03.2024").
    """
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
