import json
import pytest
from unittest.mock import patch, mock_open
from validate_report import validate

def test_validate_success():
    """Test validate() with a valid JSON array and all required fields."""
    mock_data = json.dumps([{
        "title": "Test Title",
        "description": "Test Description",
        "deepLink": "http://example.com",
        "filePath": "src/main.py",
        "lineNumber": 10
    }])
    with patch("builtins.open", mock_open(read_data=mock_data)):
        # Should not raise any exception
        validate()

def test_validate_not_a_list():
    """Test validate() when root is not a JSON array."""
    mock_data = json.dumps({"id": 1, "status": "pass"})
    with patch("builtins.open", mock_open(read_data=mock_data)):
        with pytest.raises(ValueError) as excinfo:
            validate()
        assert str(excinfo.value) == "Root should be a JSON array"

def test_validate_missing_field():
    """Test validate() when a required field is missing."""
    mock_data = json.dumps([{
        "title": "Test Title",
        "description": "Test Description",
        # "deepLink": "http://example.com",  # Missing field
        "filePath": "src/main.py",
        "lineNumber": 10
    }])
    with patch("builtins.open", mock_open(read_data=mock_data)):
        with pytest.raises(ValueError) as excinfo:
            validate()
        assert "is missing required field: deepLink" in str(excinfo.value)

def test_validate_file_not_found():
    """Test validate() when testing_report.json is missing."""
    with patch("builtins.open", side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            validate()

def test_validate_invalid_json():
    """Test validate() with malformed JSON."""
    mock_data = "not a json"
    with patch("builtins.open", mock_open(read_data=mock_data)):
        with pytest.raises(json.JSONDecodeError):
            validate()

@pytest.mark.parametrize("missing_field", [
    'title', 'description', 'deepLink', 'filePath', 'lineNumber'
])
def test_validate_each_required_field(missing_field):
    """Test validate() for each required field missing individually."""
    data = {
        "title": "Test Title",
        "description": "Test Description",
        "deepLink": "http://example.com",
        "filePath": "src/main.py",
        "lineNumber": 10
    }
    del data[missing_field]
    mock_data = json.dumps([data])

    with patch("builtins.open", mock_open(read_data=mock_data)):
        with pytest.raises(ValueError) as excinfo:
            validate()
        assert f"is missing required field: {missing_field}" in str(excinfo.value)

def test_validate_custom_path():
    """Test validate() with a custom file path."""
    mock_data = json.dumps([])
    with patch("builtins.open", mock_open(read_data=mock_data)) as mocked_open:
        validate("custom_report.json")
        mocked_open.assert_called_once_with("custom_report.json", 'r')
