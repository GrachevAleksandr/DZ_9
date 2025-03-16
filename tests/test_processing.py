import pytest
from mypy.types import AnyType

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def list_state() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", },
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", },
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.mark.parametrize(
    "state, expected",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", },
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        )
    ],
)
def test_filter_by_state_executed(list_state: list[AnyType], state: str, expected: list[AnyType]) -> None:
    assert filter_by_state(list_state) == expected


def test_filter_by_state_invalid() -> None:
    with pytest.raises(ValueError):
        filter_by_state([])


@pytest.mark.parametrize(
    "reverse, expected",
    [
        (
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        )
    ],
)
def test_sort_by_date(list_state: list[AnyType], reverse: bool, expected: list[AnyType]) -> None:
    assert sort_by_date(list_state) == expected


def test_sort_by_date_invalid() -> None:
    with pytest.raises(ValueError):
        sort_by_date([])
