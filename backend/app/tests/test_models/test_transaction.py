import pytest
from ...models.Transaction import Transaction


def test_transaction_generate_code():
    transaction = Transaction(
        fund_id=1, code="ABC123", amount=100.0, type="SUBSCRIPTION"
    )
    assert transaction.code.startswith("ABC123-1-")
    assert len(transaction.code) > len("ABC123-1-")
