import json

def validate(file_path='testing_report.json'):
    """
    Validates a JSON testing report file.

    Ensures the root is a JSON array and each item contains the required fields:
    title, description, deepLink, filePath, and lineNumber.

    Args:
        file_path (str, optional): The path to the report file. Defaults to 'testing_report.json'.

    Raises:
        ValueError: If validation fails.
        FileNotFoundError: If the report file is missing.
        json.JSONDecodeError: If the report file is not valid JSON.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError("Root should be a JSON array")

    required_fields = [
        'title', 'description', 'deepLink', 'filePath', 'lineNumber'
    ]
    required_fields_set = set(required_fields)

    for index, item in enumerate(data):
        if not required_fields_set.issubset(item.keys()):
            for field in required_fields:
                if field not in item:
                    raise ValueError(f"Item at index {index} is missing required field: {field}")
