import json

def validate():
    with open('testing_report.json', 'r') as f:
        data = json.load(f)

    assert isinstance(data, list), "Root should be a JSON array"
