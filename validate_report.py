import json

def validate(file_path='testing_report.json'):
    """
    Validates a JSON testing report file.

    Ensures the root is a JSON array and each item contains the required fields:
    title, description, deepLink, filePath, and lineNumber.

    Args:
        file_path (str): The path to the JSON testing report file. Defaults to 'testing_report.json'.

    Raises:
        ValueError: If validation fails.
        FileNotFoundError: If the report file is missing.
        json.JSONDecodeError: If the report file is not valid JSON.
    """
    with open(file_path, 'r') as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError("Root should be a JSON array")

    required_fields = [
        'title', 'description', 'deepLink', 'filePath', 'lineNumber'
    ]

    for index, item in enumerate(data):
        for field in required_fields:
            if field not in item:
                raise ValueError(f"Item at index {index} is missing required field: {field}")
