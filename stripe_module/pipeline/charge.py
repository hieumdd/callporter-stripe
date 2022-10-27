from stripe_module.repo import stripe
from stripe_module.pipeline import interface

pipeline = interface.Pipeline(
    "Charge",
    stripe.Charge,
    lambda rows: [
        {
            "id": row["id"],
            "amount": row.get("amount"),
            "billing_details": {
                "address": {
                    "city": row["billing_details"].get("address").get("city"),
                    "country": row["billing_details"].get("address").get("country"),
                    "line1": row["billing_details"].get("address").get("line1"),
                    "line2": row["billing_details"].get("address").get("line2"),
                    "postal_code": row["billing_details"]
                    .get("address")
                    .get("postal_code"),
                    "state": row["billing_details"].get("address").get("state"),
                },
                "email": row["billing_details"].get("email"),
                "name": row["billing_details"].get("name"),
                "phone": row["billing_details"].get("phone"),
            },
            "currency": row.get("currency"),
            "customer": row.get("customer"),
            "disputed": row.get("disputed"),
            "invoice": row.get("invoice"),
            "receipt_email": row.get("receipt_email"),
            "refunded": row.get("refunded"),
            "status": row.get("status"),
            "object": row.get("object"),
            "amount_captured": row.get("amount_captured"),
            "amount_refunded": row.get("amount_refunded"),
            "captured": row.get("captured"),
            "created": row.get("created"),
            "order": row.get("order"),
            "paid": row.get("paid"),
            "dispute": row.get("dispute"),
        }
        for row in rows
    ],
    [
        {"name": "id", "type": "STRING"},
        {"name": "amount", "type": "INTEGER"},
        {
            "name": "billing_details",
            "type": "record",
            "fields": [
                {
                    "name": "address",
                    "type": "record",
                    "fields": [
                        {"name": "city", "type": "STRING"},
                        {"name": "country", "type": "STRING"},
                        {"name": "line1", "type": "STRING"},
                        {"name": "line2", "type": "STRING"},
                        {"name": "postal_code", "type": "STRING"},
                        {"name": "state", "type": "STRING"},
                    ],
                },
                {"name": "email", "type": "STRING"},
                {"name": "name", "type": "STRING"},
                {"name": "phone", "type": "STRING"},
            ],
        },
        {"name": "currency", "type": "STRING"},
        {"name": "customer", "type": "STRING"},
        {"name": "disputed", "type": "BOOLEAN"},
        {"name": "invoice", "type": "STRING"},
        {"name": "receipt_email", "type": "STRING"},
        {"name": "refunded", "type": "BOOLEAN"},
        {"name": "status", "type": "STRING"},
        {"name": "object", "type": "STRING"},
        {"name": "amount_captured", "type": "INTEGER"},
        {"name": "amount_refunded", "type": "INTEGER"},
        {"name": "captured", "type": "BOOLEAN"},
        {"name": "created", "type": "TIMESTAMP"},
        {"name": "order", "type": "STRING"},
        {"name": "paid", "type": "BOOLEAN"},
        {"name": "dispute", "type": "STRING"},
    ],
)
