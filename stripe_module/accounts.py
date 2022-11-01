from dataclasses import dataclass
import os


@dataclass
class Account:
    name: str
    api_key: str


accounts = {
    i.name: i
    for i in [
        Account(
            "BallpointMarketing",
            os.getenv("BALLPOINT_MARKETING_STRIPE_API_KEY", ""),
        ),
        Account(
            "CallPorter",
            os.getenv("CALL_PORTER_STRIPE_API_KEY", ""),
        ),
        Account(
            "CreateCashFlow",
            os.getenv("CREATE_CASH_FLOW_STRIPE_API_KEY", ""),
        ),
    ]
}
