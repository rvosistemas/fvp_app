import pytest
from unittest.mock import ANY, MagicMock, call
from sqlalchemy.orm import Session
from ...models.Transaction import Transaction, TransactionType
from ...repositories.transaction_repository import TransactionRepository


def test_get_all_transactions():
    mock_db = MagicMock(spec=Session)
    mock_transactions = [
        Transaction(id=1, fund_id=1, code="TXN001"),
        Transaction(id=2, fund_id=2, code="TXN002"),
    ]

    mock_db.query().all.return_value = mock_transactions

    result = TransactionRepository.get_all_transactions(mock_db)

    assert result == mock_transactions
    mock_db.query().all.assert_called_once()


def test_get_active_transactions():
    mock_db = MagicMock(spec=Session)
    mock_transactions = [
        Transaction(id=1, fund_id=1, is_active=True, code="TXN001"),
        Transaction(id=2, fund_id=2, is_active=True, code="TXN002"),
    ]

    mock_filter_by = mock_db.query().filter_by
    mock_filter_by.return_value.all.return_value = mock_transactions

    result = TransactionRepository.get_active_transactions(mock_db)

    mock_filter_by.assert_called_once_with(is_active=True)
    assert result == mock_transactions


def test_get_active_subscription():
    mock_db = MagicMock(spec=Session)
    mock_transaction = Transaction(id=1, fund_id=100, is_active=True, code="SUB001")

    mock_filter_by = mock_db.query().filter_by
    mock_filter_by.return_value.first.return_value = mock_transaction

    result = TransactionRepository.get_active_subscription(mock_db, fund_id=100)

    assert result == mock_transaction
    mock_filter_by.assert_called_once_with(fund_id=100, is_active=True)


def test_create_transaction():
    mock_db = MagicMock(spec=Session)
    mock_transaction = Transaction(id=1, fund_id=1, code="TXN001")

    mock_db.add.side_effect = lambda x: None
    mock_db.commit.side_effect = lambda: None
    mock_db.refresh.side_effect = lambda x: None

    result = TransactionRepository.create_transaction(mock_db, mock_transaction)

    assert result == mock_transaction
    mock_db.add.assert_called_once_with(mock_transaction)
    mock_db.commit.assert_called_once()
    mock_db.refresh.assert_called_once_with(mock_transaction)


def test_is_fund_already_subscribed_true():
    mock_db = MagicMock(spec=Session)
    mock_transaction = Transaction(
        id=1, fund_id=100, type=TransactionType.SUBSCRIPTION, code="SUB001"
    )

    mock_filter = mock_db.query().filter
    mock_filter.return_value.first.return_value = mock_transaction

    result = TransactionRepository.is_fund_already_subscribed(mock_db, fund_id=100)

    assert result is True

    mock_filter.assert_called_once_with(ANY, ANY)


def test_is_fund_already_subscribed_false():
    mock_db = MagicMock(spec=Session)

    mock_db.query().filter().first.return_value = None

    result = TransactionRepository.is_fund_already_subscribed(mock_db, fund_id=100)

    assert result is False

    expected_calls = [
        call(ANY, ANY),
        call().first(),
    ]

    mock_db.query().filter.assert_has_calls(expected_calls, any_order=False)
