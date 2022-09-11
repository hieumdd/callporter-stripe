import os
from datetime import datetime
from math import floor

import stripe

stripe.api_key = os.getenv("API_KEY", "")


def get(module, options: dict = {}):
    def _get(timeframe: tuple[datetime, datetime]) -> list[dict]:
        start, end = [floor(i.timestamp()) for i in timeframe]
        data = module.list(
            created={
                "gte": start,
                "lte": end,
            },
            limit=100,
            **options,
        )
        return [i.to_dict_recursive() for i in data.auto_paging_iter()]

    return _get
