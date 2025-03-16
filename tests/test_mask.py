from typing import Union

import pytest

from src.mask import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "account, expected",
    [
        (70007958622289606361, "**6361"),
        (73654253610843013587, "**3587"),
    ],
)
def test_mask_account(account: Union[str, int], expected: str) -> None:
    assert get_mask_account(account) == expected


def test_mask_account_invalid_account() -> None:
    with pytest.raises(ValueError):
        get_mask_account(3642581672593648)


def test_mask_account_invalid() -> None:
    with pytest.raises(ValueError):
        get_mask_account("3643y9n67r25k93i64l8")


@pytest.mark.parametrize(
    "account, expected",
    [
        (1234567890123456, "1234 56** **** 3456"),
        (7000792289606361, "7000 79** **** 6361"),
    ],
)
def test_mask_card_number(account: Union[str, int], expected: str) -> None:
    assert get_mask_card_number(account) == expected


def test_mask_card_number_invalid_account() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(26843642581672593648)


def test_mask_card_number_invalid() -> None:
    with pytest.raises(ValueError):
        get_mask_account("37l00792s89606361")
