import pytest


def test_total_divisible_by_5(input_total):
    assert input_total % 5 == 0


def test_total_divisible_by_13(input_total):
    assert input_total % 13 == 0

def test_total_divisible_by_20(input_total):
    assert input_total % 20 == 0


def test_total_divisible_by_25(input_total):
    assert input_total % 25 == 0