from pathlib import Path
import json


def test_report_exists():
    """The agent produced a report file."""
    assert Path("/app/report.json").exists(), "no report.json found"


def test_report_nonempty():
    """The report file is not empty."""
    assert Path("/app/report.json").stat().st_size > 0, "report.json is empty"


def test_report_valid_json():
    """The report file contains valid JSON."""
    with open("/app/report.json", "r") as f:
        data = json.load(f)
    assert isinstance(data, dict), "report.json must contain a JSON object"


def test_report_has_required_fields():
    """The report contains all required fields."""
    with open("/app/report.json", "r") as f:
        data = json.load(f)
    assert "total_requests" in data, "missing total_requests field"
    assert "unique_ips" in data, "missing unique_ips field"
    assert "top_path" in data, "missing top_path field"


def test_report_correct_types():
    """The report fields have correct types."""
    with open("/app/report.json", "r") as f:
        data = json.load(f)
    assert isinstance(data["total_requests"], int), "total_requests must be an integer"
    assert isinstance(data["unique_ips"], int), "unique_ips must be an integer"
    assert isinstance(data["top_path"], str), "top_path must be a string"
