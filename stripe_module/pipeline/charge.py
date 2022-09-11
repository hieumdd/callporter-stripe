from stripe_module.repo import stripe
from stripe_module.pipeline import interface

pipeline = interface.Pipeline(
    "Charge",
    stripe.Charge,
    lambda rows: [
        {
            "id": row["id"],
            "amount": row["amount"],
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
            "currency": row["currency"],
            "customer": row["customer"],
            "disputed": row["disputed"],
            "invoice": row["invoice"],
            "receipt_email": row["receipt_email"],
            "refunded": row["refunded"],
            "status": row["status"],
            "object": row["object"],
            "amount_captured": row["amount_captured"],
            "amount_refunded": row["amount_refunded"],
            "captured": row["captured"],
            "created": row["created"],
            "order": row["order"],
            "paid": row["paid"],
            "dispute": row["dispute"],
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
