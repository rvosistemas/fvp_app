import pytest
from fastapi.testclient import TestClient
from ...main import app

client = TestClient(app)


def test_fund_create_example_structure():
    fund_create_example = {
        "name": "Growth Fund",
        "minimum_amount": 1000.0,
        "category": "Growth",
    }

    assert "name" in fund_create_example
    assert "minimum_amount" in fund_create_example
    assert "category" in fund_create_example

    assert isinstance(fund_create_example["name"], str)
    assert isinstance(fund_create_example["minimum_amount"], float)
    assert isinstance(fund_create_example["category"], str)


def test_fund_response_example_structure():
    fund_response_example = {
        "id": "123",
        "name": "Growth Fund",
        "minimum_amount": 1000.0,
        "category": "Growth",
        "is_active": True,
    }

    assert "id" in fund_response_example
    assert "name" in fund_response_example
    assert "minimum_amount" in fund_response_example
    assert "category" in fund_response_example
    assert "is_active" in fund_response_example

    assert isinstance(fund_response_example["id"], str)
    assert isinstance(fund_response_example["name"], str)
    assert isinstance(fund_response_example["minimum_amount"], float)
    assert isinstance(fund_response_example["category"], str)
    assert isinstance(fund_response_example["is_active"], bool)


# Test para la estructura de fund_responses
def test_fund_responses_structure():
    fund_responses = {
        201: {
            "description": "Successfully created a fund",
            "content": {
                "application/json": {
                    "example": {
                        "id": "123",
                        "name": "Growth Fund",
                        "minimum_amount": 1000.0,
                        "category": "Growth",
                        "is_active": True,
                    }
                },
            },
        },
        422: {
            "description": "Validation Error",
            "content": {
                "application/json": {
                    "example": {
                        "detail": [
                            {
                                "loc": ["body", "name"],
                                "msg": "field required",
                                "type": "value_error.missing",
                            }
                        ]
                    }
                }
            },
        },
    }

    assert 201 in fund_responses
    assert 422 in fund_responses

    assert fund_responses[201]["description"] == "Successfully created a fund"
    assert fund_responses[422]["description"] == "Validation Error"

    assert "application/json" in fund_responses[201]["content"]
    assert "application/json" in fund_responses[422]["content"]

    error_example = fund_responses[422]["content"]["application/json"]["example"]
    assert "detail" in error_example
    assert isinstance(error_example["detail"], list)
    assert error_example["detail"][0]["loc"] == ["body", "name"]
    assert error_example["detail"][0]["msg"] == "field required"
    assert error_example["detail"][0]["type"] == "value_error.missing"
