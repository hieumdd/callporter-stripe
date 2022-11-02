from datetime import datetime
from typing import Optional

from compose import compose

from stripe_module.pipeline import interface
from stripe_module import repo, accounts, pipeline
from db import bigquery
from tasks import cloud_tasks


def pipeline_service(
    pipeline: interface.Pipeline,
    account: accounts.Account,
    start: Optional[str],
    end: Optional[str],
):
    table = f"{pipeline.name}__{account.name}"
    _start = (
        datetime.strptime(start, "%Y-%m-%d")
        if start
        else bigquery.get_latest(table)
    )

    _end = datetime.strptime(end, "%Y-%m-%d") if end else datetime.utcnow()

    return compose(
        bigquery.load(table, pipeline.schema),
        pipeline.transform,
        repo.get(pipeline.module, account.api_key, pipeline.options),
    )((_start, _end))


def tasks_service(start: Optional[str], end: Optional[str]):
    return {
        "tasks": cloud_tasks.create_tasks(
            [
                {
                    "table": table,
                    "name": account.name,
                    "start": start,
                    "end": end,
                }
                for table in pipeline.pipelines.keys()
                for account in accounts.accounts.values()
            ],
            lambda x: x["table"],
        )
    }
