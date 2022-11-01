import pytest

from stripe_module.accounts import accounts
from stripe_module.pipeline import pipelines
from stripe_module.service import pipeline_service

TIMEFRAME = [
    ("auto", (None, None)),
    # ("manual", ("2022-01-01", "2022-11-01")),
]


@pytest.mark.parametrize(
    "account",
    accounts.values(),
    ids=lambda account: account.name,
)
@pytest.mark.parametrize(
    "pipeline",
    pipelines.values(),
    ids=pipelines.keys(),
)
@pytest.mark.parametrize(
    "timeframe",
    [i[1] for i in TIMEFRAME],
    ids=[i[0] for i in TIMEFRAME],
)
def test_service(pipeline, account, timeframe):
    res = pipeline_service(pipeline, account, *timeframe)
    assert res >= 0
