from datetime import datetime
from typing import Optional

from compose import compose

from stripe_module.pipeline import interface
from stripe_module import repo
from db import bigquery


def pipeline_service(
    pipeline: interface.Pipeline,
    start: Optional[str],
    end: Optional[str],
):
    _start = (
        datetime.strptime(start, "%Y-%m-%d")
        if start
        else bigquery.get_latest(pipeline.name)
    )

    _end = datetime.strptime(end, "%Y-%m-%d") if end else datetime.utcnow()

    return compose(
        bigquery.load(pipeline.name, pipeline.schema),
        pipeline.transform,
        repo.get(pipeline.module, pipeline.options),
    )((_start, _end))
