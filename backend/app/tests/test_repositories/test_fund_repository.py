import pytest
from unittest.mock import MagicMock, patch
from sqlalchemy.orm import Session
from fastapi import HTTPException
from ...models.Fund import Fund
from ...repositories.fund_repository import FundRepository


def test_get_all_funds():
    mock_db = MagicMock(spec=Session)
    mock_funds = [Fund(name="Fund 1"), Fund(name="Fund 2")]

    mock_db.query().all.return_value = mock_funds

    result = FundRepository.get_all_funds(mock_db)

    assert result == mock_funds
    mock_db.query().all.assert_called_once()


@patch("app.app.repositories.fund_repository.get_fund_or_404")
def test_get_fund_by_id(mock_get_fund_or_404):
    mock_db = MagicMock(spec=Session)
    mock_fund = Fund(id="1", name="Test Fund")

    mock_get_fund_or_404.return_value = mock_fund

    mock_db.refresh = MagicMock()

    result = FundRepository.get_fund_by_id(mock_db, "1")

    assert result == mock_fund
    mock_get_fund_or_404.assert_called_once_with(mock_db, "1")


@patch("app.app.repositories.fund_repository.get_fund_or_404")
def test_get_fund_by_id_not_found(mock_get_fund_or_404):
    mock_db = MagicMock(spec=Session)

    mock_get_fund_or_404.side_effect = HTTPException(status_code=404)

    with pytest.raises(HTTPException) as excinfo:
        FundRepository.get_fund_by_id(mock_db, "999")

    assert excinfo.value.status_code == 404
    mock_get_fund_or_404.assert_called_once_with(mock_db, "999")


def test_create_fund_success():
    mock_db = MagicMock(spec=Session)
    mock_fund = Fund(name="New Fund")

    mock_db.query().filter().first.return_value = None

    mock_db.add.side_effect = lambda x: None
    mock_db.commit.side_effect = lambda: None
    mock_db.refresh.side_effect = lambda x: None

    result = FundRepository.create_fund(mock_db, mock_fund)

    assert result == mock_fund
    mock_db.add.assert_called_once_with(mock_fund)
    mock_db.commit.assert_called_once()


def test_create_fund_already_exists():
    mock_db = MagicMock(spec=Session)
    mock_fund = Fund(name="Existing Fund")

    mock_db.query().filter().first.return_value = mock_fund

    with pytest.raises(HTTPException) as excinfo:
        FundRepository.create_fund(mock_db, mock_fund)

    assert excinfo.value.status_code == 400
    assert excinfo.value.detail == "Fund with this name already exists"


@patch("app.app.repositories.fund_repository.get_fund_or_404")
def test_delete_fund_success(mock_get_fund_or_404):
    mock_db = MagicMock(spec=Session)
    mock_fund = Fund(id="1", name="Test Fund")

    mock_get_fund_or_404.return_value = mock_fund

    FundRepository.delete_fund(mock_db, "1")

    mock_db.delete.assert_called_once_with(mock_fund)
    mock_db.commit.assert_called_once()


@patch("app.app.repositories.fund_repository.get_fund_or_404")
def test_deactivate_fund(mock_get_fund_or_404):
    mock_db = MagicMock(spec=Session)
    mock_fund = Fund(id="1", name="Test Fund", is_active=True)

    mock_get_fund_or_404.return_value = mock_fund

    result = FundRepository.deactivate_fund(mock_db, "1")

    assert not result.is_active
    mock_db.commit.assert_called_once()
    mock_db.refresh.assert_called_once_with(mock_fund)
