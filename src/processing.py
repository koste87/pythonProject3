from typing import List, Dict, Any

def filter_by_state(data: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """
    Filters a list of dictionaries by the specified state.

    Args:
        data (list): List of dictionaries.
        state (str): State to filter by (default is 'EXECUTED').

    Returns:
        list: Filtered list of dictionaries.
    """
    return [entry for entry in data if entry.get('state') == state]


def sort_by_date(data: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """
    Sorts a list of dictionaries by the 'date' key.

    Args:
        data (list): List of dictionaries.
        reverse (bool): Sort in descending order if True (default is True).

    Returns:
        list: Sorted list of dictionaries.
    """
    return sorted(data, key=lambda x: x['date'], reverse=reverse)
