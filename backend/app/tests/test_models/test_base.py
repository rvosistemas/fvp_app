import pytest
from app.models.Base import Base


def test_base_deactivate():
    base_instance = Base()
    base_instance.deactivate()
    assert base_instance.is_active is False
    assert base_instance.updated_at is not None
