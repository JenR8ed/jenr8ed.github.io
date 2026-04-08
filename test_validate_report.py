import json
import pytest
from unittest.mock import patch, mock_open
from validate_report import validate

def test_validate_success():
    """Test validate() with a valid JSON array."""
    mock_data = json.dumps([{"id": 1, "status": "pass"}])
    with patch("builtins.open", mock_open(read_data=mock_data)):
        # Should not raise any exception
        validate()

def test_validate_not_a_list():
    """Test validate() when root is not a JSON array."""
    mock_data = json.dumps({"id": 1, "status": "pass"})
    with patch("builtins.open", mock_open(read_data=mock_data)):
        with pytest.raises(AssertionError) as excinfo:
            validate()
        assert str(excinfo.value) == "Root should be a JSON array"

def test_validate_file_not_found():
    """Test validate() when file is missing."""
    with patch("builtins.open", side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            validate()

def test_validate_invalid_json():
    """Test validate() with malformed JSON."""
    mock_data = "not a json"
    with patch("builtins.open", mock_open(read_data=mock_data)):
        with pytest.raises(json.JSONDecodeError):
            validate()

def test_validate_custom_filepath():
    """Test validate() with a custom filepath."""
    mock_data = json.dumps([])
    custom_path = "custom_report.json"
    with patch("builtins.open", mock_open(read_data=mock_data)) as mocked_open:
        validate(filepath=custom_path)
        mocked_open.assert_called_once_with(custom_path, 'r')
