def validate_trade(trade):
    errors = []

    if not trade.get("uti"):
        errors.append("Missing UTI")

    if not trade.get("currency"):
        errors.append("Missing currency")

    if trade.get("notional", 0) <= 0:
        errors.append("Invalid notional")

    if errors:
        return {
            "status": "FAILED",
            "errors": errors
        }

    return {
        "status": "PASSED",
        "errors": []
    }


def reconcile_trade(source, reported):
    discrepancies = []

    if source["uti"] != reported["uti"]:
        discrepancies.append("UTI mismatch")

    if source["currency"] != reported["currency"]:
        discrepancies.append("Currency mismatch")

    if source["notional"] != reported["notional"]:
        discrepancies.append("Notional mismatch")

    if discrepancies:
        return {
            "status": "FAILED",
            "discrepancies": discrepancies
        }

    return {
        "status": "PASSED",
        "discrepancies": []
    }
