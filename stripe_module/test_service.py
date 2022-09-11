import pytest

from stripe_module.pipeline import pipelines
from stripe_module.service import pipeline_service

TIMEFRAME = [
    ("auto", (None, None)),
    ("manual", ("2022-08-01", "2022-09-01")),
]


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
def test_service(pipeline, timeframe):
    res = pipeline_service(pipeline, *timeframe)
    assert res
