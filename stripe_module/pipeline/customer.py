from stripe_module.repo import stripe
from stripe_module.pipeline import interface

pipeline = interface.Pipeline(
    "Customer",
    stripe.Customer,
    lambda rows: [
        {
            "id": row["id"],
            "object": row["object"],
            "created": row["created"],
            "name": row["name"],
            "email": row["email"],
            "tax_ids": {
                "data": [
                    {
                        "id": d.get("id"),
                        "country": d.get("country"),
                        "created": d.get("created"),
                        "customer": d.get("customer"),
                        "livemode": d.get("livemode"),
                        "type": d.get("type"),
                        "value": d.get("value"),
                    }
                    for d in row["tax_ids"]["data"]
                ]
                if row["tax_ids"].get("data")
                else []
            },
        }
        for row in rows
    ],
    [
        {"name": "id", "type": "STRING"},
        {"name": "object", "type": "STRING"},
        {"name": "created", "type": "TIMESTAMP"},
        {"name": "name", "type": "STRING"},
        {"name": "email", "type": "STRING"},
        {
            "name": "tax_ids",
            "type": "RECORD",
            "fields": [
                {
                    "name": "data",
                    "type": "RECORD",
                    "mode": "REPEATED",
                    "fields": [
                        {"name": "id", "type": "STRING"},
                        {"name": "country", "type": "STRING"},
                        {"name": "created", "type": "TIMESTAMP"},
                        {"name": "customer", "type": "STRING"},
                        {"name": "livemode", "type": "BOOLEAN"},
                        {"name": "type", "type": "STRING"},
                        {"name": "value", "type": "STRING"},
                    ],
                },
            ],
        },
    ],
    options={"expand": ["data.tax_ids"]},
)
