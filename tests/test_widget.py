import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "account, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
    ],
)
def test_mask_account_card(account: str, expected: str) -> None:
    assert mask_account_card(account) == expected


def test_mask_account_card_invalid() -> None:
    with pytest.raises(ValueError):
        mask_account_card("")


@pytest.mark.parametrize(
    "account, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-12-07T02:26:18.671407", "07.12.2024"),
    ],
)
def test_get_date(account: str, expected: str) -> None:
    assert get_date(account) == expected


def test_get_date_invalid() -> None:
    with pytest.raises(ValueError):
        mask_account_card("")
