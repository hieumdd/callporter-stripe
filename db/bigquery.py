from google.cloud import bigquery

DATASET = "Stripe"


def get_client():
    return bigquery.Client()


def get_latest(table: str):
    rows = (
        get_client()
        .query(f"SELECT MAX(ModificationTimestamp) AS incre FROM {DATASET}.p_{table}")
        .result()
    )
    _start = [row for row in rows][0]["incre"]
    return _start


def load(table: str, schema: list[dict]):
    def _load(rows: list[dict]) -> int:
        output_rows = (  # type: ignore
            get_client()
            .load_table_from_json(
                rows,
                f"{DATASET}.p_{table}",
                job_config=bigquery.LoadJobConfig(
                    schema=schema,
                    create_disposition="CREATE_IF_NEEDED",
                    write_disposition="WRITE_APPEND",
                ),
            )
            .result()
            .output_rows
        )
        return output_rows

    return _load
