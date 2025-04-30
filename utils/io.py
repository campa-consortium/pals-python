def custom_encoder(data):
    if isinstance(data, dict):
        kind = data.get("kind")
        if kind in ["Drift", "Quadrupole"]:
            return {kind: {k: v for k, v in data.items() if k != "kind"}}
        return {k: custom_encoder(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [custom_encoder(item) for item in data]
    else:
        return data


def custom_decoder(data):
    if isinstance(data, dict):
        if len(data) == 1:
            kind, element_data = next(iter(data.items()))
            if kind in ["Drift", "Quadrupole"]:
                element_data["kind"] = kind
                return element_data
        return {k: custom_decoder(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [custom_decoder(item) for item in data]
    else:
        return data
