import pytest
from fuel_station import fuel_bill, pump_allowed, session_status


# FUEL BILL TESTS

def test_unknown_grade():
    with pytest.raises(ValueError):
        fuel_bill("unknown", 10, "silver")


def test_negative_litres():
    with pytest.raises(ValueError):
        fuel_bill("regular", -5, "silver")


def test_regular_within_coverage():
    assert fuel_bill("regular", 8, "silver") == 0


def test_gold_regular_coverage():
    assert fuel_bill("regular", 12, "gold") == 0


def test_gold_premium_coverage():
    assert fuel_bill("premium", 20, "gold") == 0


def test_diesel_bill():
    assert fuel_bill("diesel", 30, "silver") == 900


def test_regular_bill():
    assert fuel_bill("regular", 20, "silver") == 1050


def test_large_extra_silver_bill():
    assert fuel_bill("regular", 50, "silver") == 3960


def test_large_extra_gold_bill():
    assert fuel_bill("regular", 50, "gold") == 3325


# PUMP ALLOWED TESTS

def test_fleet_allowed():
    assert pump_allowed(200, 5, True) is True


def test_fleet_not_allowed():
    assert pump_allowed(201, 1, True) is False


def test_non_fleet_allowed():
    assert pump_allowed(60, 1, False) is True


def test_non_fleet_exceeds_limit():
    assert pump_allowed(61, 1, False) is False


def test_multiple_containers():
    assert pump_allowed(30, 2, False) is False


# SESSION STATUS TESTS

def test_card_active():
    assert session_status(60, True, False) == "active"


def test_card_warning():
    assert session_status(50, True, False) == "warning"


def test_card_timed_out():
    assert session_status(40, True, False) == "timed_out"


def test_cash_active():
    assert session_status(30, False, False) == "active"


def test_cash_warning():
    assert session_status(20, False, False) == "warning"


def test_cash_timed_out():
    assert session_status(10, False, False) == "timed_out"


def test_night_active():
    assert session_status(90, True, True) == "active"


def test_night_warning():
    assert session_status(80, True, True) == "warning"