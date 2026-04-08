import json

def validate(filepath='testing_report.json'):
    """Validates that the given JSON file has a list at its root.

    Args:
        filepath (str): The path to the JSON file to validate.
    """
    with open(filepath, 'r') as f:
        data = json.load(f)

    assert isinstance(data, list), "Root should be a JSON array"
