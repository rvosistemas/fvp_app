fund_create_example = {
    "name": "Growth Fund",
    "minimum_amount": 1000.0,
    "category": "Growth",
}

fund_response_example = {
    "id": "123",
    "name": "Growth Fund",
    "minimum_amount": 1000.0,
    "category": "Growth",
    "is_active": True,
}

fund_responses = {
    201: {
        "description": "Successfully created a fund",
        "content": {"application/json": {"example": fund_response_example}},
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
