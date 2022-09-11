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
            "metadata": {
                "kjb_member_id": row["metadata"].get("kjb_member_id"),
                "street_line_1": row["metadata"].get("street_line_1"),
                "street_line_2": row["metadata"].get("street_line_2"),
                "city": row["metadata"].get("city"),
                "country": row["metadata"].get("country"),
                "region": row["metadata"].get("region"),
                "postal_code": row["metadata"].get("postal_code"),
                "phone_number": row["metadata"].get("phone_number"),
            }
            if row.get("metadata")
            else {},
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
            "name": "metadata",
            "type": "RECORD",
            "fields": [
                {"name": "kjb_member_id", "type": "STRING"},
                {"name": "street_line_1", "type": "STRING"},
                {"name": "street_line_2", "type": "STRING"},
                {"name": "city", "type": "STRING"},
                {"name": "country", "type": "STRING"},
                {"name": "region", "type": "STRING"},
                {"name": "postal_code", "type": "STRING"},
                {"name": "phone_number", "type": "STRING"},
            ],
        },
    ],
)
