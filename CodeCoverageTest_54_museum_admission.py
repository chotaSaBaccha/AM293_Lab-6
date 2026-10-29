import pytest
from museum_admission import ticket_price, group_discount, gallery_entry


def test_ticket_price_code_paths():
    with pytest.raises(ValueError, match="unknown category"):
        ticket_price("visitor", 30, "tuesday", False)
    with pytest.raises(ValueError, match="invalid age"):
        ticket_price("adult", -1, "tuesday", False)
    assert ticket_price("adult", 4, "tuesday", False) == 0
    assert ticket_price("adult", 30, "monday", False) == 150
    assert ticket_price("adult", 30, "saturday", False) == 350
    assert ticket_price("student", 20, "tuesday", True) == 200
    assert ticket_price("adult", 30, "tuesday", True) == 400


def test_group_discount_code_paths():
    with pytest.raises(ValueError, match="invalid group size"):
        group_discount(0, False)
    assert group_discount(20, True) == 40
    assert group_discount(4, True) == 25
    assert group_discount(15, False) == 20
    assert group_discount(8, False) == 10
    assert group_discount(4, False) == 0


def test_gallery_entry_code_paths():
    assert gallery_entry(10, 10, False) == "wait"
    assert gallery_entry(9, 10, False) == "queue"
    assert gallery_entry(9, 10, True) == "enter"
    assert gallery_entry(5, 10, False) == "enter"
