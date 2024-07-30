import pytest
from decorators.log_decorator import log
import datetime
import os
import re


@pytest.fixture
def setup_logging():
    filename = 'test_log.txt'
    yield filename
    if os.path.exists(filename):
        os.remove(filename)


@log(filename="test_log.txt")
def my_function(x, y):
    return x + y


@log(filename="test_log.txt")
def error_function():
    raise ValueError("Test error")


def test_log_decorator_successful_execution(setup_logging):
    my_function(1, 2)
    with open('test_log.txt', 'r') as f:
        log_contents = f.read().strip()
    log_pattern = re.compile(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+ - my_function - ok")
    assert log_pattern.match(log_contents) is not None


def test_log_decorator_error_handling(setup_logging):
    with pytest.raises(ValueError):
        error_function()

    with open('test_log.txt', 'r') as f:
        log_contents = f.read().strip()
    assert "ValueError" in log_contents


def test_log_decorator_no_filename(capsys):
    @log
    def no_file_log_function():
        return 42

    no_file_log_function()
    captured = capsys.readouterr()
    log_pattern = re.compile(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+ - no_file_log_function - ok")
    assert log_pattern.search(captured.out) is not None
