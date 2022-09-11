from stripe_module import pipeline, service


def main(request):
    data: dict = request.get_json()
    print(data)

    if "table" in data:
        response = service.pipeline_service(
            pipeline.pipelines[data["table"]],
            data.get("start"),
            data.get("end"),
        )
    else:
        raise ValueError(data)

    print(response)
    return response
