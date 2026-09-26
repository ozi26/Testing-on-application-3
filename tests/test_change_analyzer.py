# Analyzer Tests: verifies source and configuration classification.
from analyzer.change_analyzer import classify_changes  # Imports the analyzer classifier.

def test_classify_changes():  # Defines the analyzer unit test.
    result = classify_changes(["rideshare_services/config/rider_config.py", "rideshare_services/rider_service.py"])  # Classifies two files.
    assert result[0]["type"] == "configuration"  # Confirms the config file classification.
    assert result[1]["type"] == "source"  # Confirms the source file classification.
