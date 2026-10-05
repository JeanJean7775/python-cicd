from emir_validator import validate_trade, reconcile_trade


def test_valid_trade():
    trade = {
        "uti": "UTI-12345",
        "currency": "EUR",
        "notional": 1_000_000
    }

    result = validate_trade(trade)

    assert result["status"] == "PASSED"
    assert result["errors"] == []


def test_missing_uti():
    trade = {
        "uti": None,
        "currency": "EUR",
        "notional": 1_000_000
    }

    result = validate_trade(trade)

    assert result["status"] == "FAILED"
    assert "Missing UTI" in result["errors"]


def test_notional_mismatch():
    source = {
        "uti": "UTI-12345",
        "currency": "EUR",
        "notional": 1_200_000
    }

    reported = {
        "uti": "UTI-12345",
        "currency": "EUR",
        "notional": 1_000_000
    }

    result = reconcile_trade(source, reported)

    assert result["status"] == "FAILED"
    assert "Notional mismatch" in result["discrepancies"]
