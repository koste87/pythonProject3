import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 1,
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Transaction 1"
        },
        {
            "id": 2,
            "operationAmount": {"currency": {"code": "EUR"}},
            "description": "Transaction 2"
        },
        {
            "id": 3,
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Transaction 3"
        }
    ]


@pytest.mark.parametrize("currency,expected", [
    ("USD", [
        {
            "id": 1,
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Transaction 1"
        },
        {
            "id": 3,
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Transaction 3"
        }
    ]),
    ("EUR", [
        {
            "id": 2,
            "operationAmount": {"currency": {"code": "EUR"}},
            "description": "Transaction 2"
        }
    ]),
    ("GBP", [])
])
def test_filter_by_currency(sample_transactions, currency, expected):
    result = list(filter_by_currency(sample_transactions, currency))
    assert result == expected


def test_transaction_descriptions(sample_transactions):
    descriptions = list(transaction_descriptions(sample_transactions))
    assert descriptions == ["Transaction 1", "Transaction 2", "Transaction 3"]


@pytest.mark.parametrize("start,stop,expected", [
    (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
    (10, 12, ["0000 0000 0000 0010", "0000 0000 0000 0011", "0000 0000 0000 0012"])
])
def test_card_number_generator(start, stop, expected):
    result = list(card_number_generator(start, stop))
    assert result == expected
