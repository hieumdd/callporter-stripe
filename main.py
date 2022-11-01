from stripe_module import accounts, pipeline, service


def main(request):
    data: dict = request.get_json()
    print(data)

    if "table" in data:
        response = service.pipeline_service(
            pipeline.pipelines[data["table"]],
            accounts.accounts[data["name"]],
            data.get("start"),
            data.get("end"),
        )
    elif "tasks" in data:
        response = service.tasks_service(
            data.get("start"),
            data.get("end"),
        )
    else:
        raise ValueError(data)

    print(response)
    return {"data": response}
