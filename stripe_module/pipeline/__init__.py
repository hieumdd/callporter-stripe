from stripe_module.pipeline import charge, customer

pipelines = {
    i.name: i
    for i in [
        j.pipeline
        for j in [
            charge,
            customer,
        ]
    ]
}
