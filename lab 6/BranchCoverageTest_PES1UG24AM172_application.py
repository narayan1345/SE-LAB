import pytest
from fuel_station import fuel_bill, pump_allowed, session_status


# ---------------- FUEL BILL ----------------

def test_unknown_grade():
    with pytest.raises(ValueError):
        fuel_bill("unknown", 10, "silver")


def test_negative_litres():
    with pytest.raises(ValueError):
        fuel_bill("regular", -5, "silver")


def test_covered_litres():
    assert fuel_bill("regular", 8, "silver") == 0


def test_gold_non_diesel():
    assert fuel_bill("regular", 12, "gold") == 0


def test_gold_diesel():
    assert fuel_bill("diesel", 10, "gold") == 0


def test_exact_covered_litres():
    assert fuel_bill("regular", 10, "silver") == 0


def test_extra_litres_below_discount_threshold():
    assert fuel_bill("regular", 40, "silver") == 3150


def test_diesel_rate():
    assert fuel_bill("diesel", 30, "silver") == 900


def test_regular_rate():
    assert fuel_bill("regular", 20, "silver") == 1050


def test_large_extra_silver():
    assert fuel_bill("regular", 50, "silver") == 3960


def test_large_extra_gold():
    assert fuel_bill("regular", 50, "gold") == 3325


# ---------------- PUMP ALLOWED ----------------

def test_fleet_within_limit():
    assert pump_allowed(200, 5, True) is True


def test_fleet_above_limit():
    assert pump_allowed(201, 1, True) is False


def test_non_fleet_within_limit():
    assert pump_allowed(60, 1, False) is True


def test_non_fleet_above_limit():
    assert pump_allowed(61, 1, False) is False


def test_non_fleet_multiple_containers():
    assert pump_allowed(30, 2, False) is False


# ---------------- SESSION STATUS ----------------

def test_card_day_active():
    assert session_status(60, True, False) == "active"


def test_card_day_warning():
    assert session_status(45, True, False) == "warning"


def test_card_day_timed_out():
    assert session_status(44, True, False) == "timed_out"


def test_cash_day_active():
    assert session_status(30, False, False) == "active"


def test_cash_day_warning():
    assert session_status(15, False, False) == "warning"


def test_cash_day_timed_out():
    assert session_status(14, False, False) == "timed_out"


def test_card_night_active():
    assert session_status(90, True, True) == "active"


def test_card_night_warning():
    assert session_status(75, True, True) == "warning"


def test_card_night_timed_out():
    assert session_status(74, True, True) == "timed_out"


def test_cash_night_active():
    assert session_status(60, False, True) == "active"


def test_cash_night_warning():
    assert session_status(45, False, True) == "warning"


def test_cash_night_timed_out():
    assert session_status(44, False, True) == "timed_out"