transaction_create_example = {
    "type": "subscription",
    "fund_id": "123",
    "amount": 500.0,
    "date": "2024-10-01",
}

transaction_response_example = {
    "id": "abc123",
    "type": "subscription",
    "fund_id": "123",
    "amount": 500.0,
    "date": "2024-10-01",
    "is_active": True,
}

transaction_responses = {
    201: {
        "description": "Successfully created a transaction",
        "content": {"application/json": {"example": transaction_response_example}},
    },
    422: {
        "description": "Validation Error",
        "content": {
            "application/json": {
                "example": {
                    "detail": [
                        {
                            "loc": ["body", "type"],
                            "msg": "field required",
                            "type": "value_error.missing",
                        }
                    ]
                }
            }
        },
    },
}
