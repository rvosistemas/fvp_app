import pytest
from app.models.Fund import Fund


def almost_equal(a, b, tolerance=0.0001):
    return abs(a - b) <= tolerance


def test_fund_creation():
    fund = Fund(name="Test Fund", minimum_amount=100.0, category="Stocks")
    assert fund.name == "Test Fund"
    assert almost_equal(fund.minimum_amount, 100.0)
    assert fund.category == "Stocks"
