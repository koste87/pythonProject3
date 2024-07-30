import pytest
from src.processing import filter_by_state, sort_by_date

@pytest.fixture
def sample_data():
    return [
        {'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01'},
        {'id': 2, 'state': 'PENDING', 'date': '2023-02-01'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2023-01-15'},
        {'id': 4, 'state': 'CANCELLED', 'date': '2023-03-01'},
        {'id': 5, 'state': 'EXECUTED', 'date': '2023-01-05'}
    ]

@pytest.mark.parametrize("state,expected_count", [
    ('EXECUTED', 3),
    ('PENDING', 1),
    ('CANCELLED', 1),
    ('NOT_EXIST', 0)
])
def test_filter_by_state(sample_data, state, expected_count):
    result = filter_by_state(sample_data, state)
    assert len(result) == expected_count
    assert all(entry['state'] == state for entry in result)

def test_sort_by_date_descending(sample_data):
    result = sort_by_date(sample_data)
    assert result == [
        {'id': 4, 'state': 'CANCELLED', 'date': '2023-03-01'},
        {'id': 2, 'state': 'PENDING', 'date': '2023-02-01'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2023-01-15'},
        {'id': 5, 'state': 'EXECUTED', 'date': '2023-01-05'},
        {'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01'}
    ]

def test_sort_by_date_ascending(sample_data):
    result = sort_by_date(sample_data, reverse=False)
    assert result == [
        {'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01'},
        {'id': 5, 'state': 'EXECUTED', 'date': '2023-01-05'},
        {'id': 3, 'state': 'EXECUTED', 'date': '2023-01-15'},
        {'id': 2, 'state': 'PENDING', 'date': '2023-02-01'},
        {'id': 4, 'state': 'CANCELLED', 'date': '2023-03-01'}
    ]
