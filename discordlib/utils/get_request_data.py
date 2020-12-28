def get_request_data(locals: dict):
    data = {}
    for key, value_ in locals.items():
        if key not in ["self", "return_raw_response"] and value_ is not None:
            if isinstance(value_, list):
                value_ = ",".join(str(item) for item in value_)
            data[key] = value_
    return data
