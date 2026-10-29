import pytest
from museum_admission import ticket_price, group_discount, gallery_entry


@pytest.mark.parametrize(
    "category, age, day, tour, expected",
    [
        ("adult", 30, "tuesday", False, 300),
        ("adult", 30, "monday", False, 150),
        ("adult", 30, "saturday", False, 350),
        ("adult", 30, "sunday", False, 350),
        ("student", 20, "tuesday", True, 200),
        ("adult", 30, "tuesday", True, 400),
        ("child", 4, "tuesday", False, 0),
    ],
)
def test_ticket_price_branches(category, age, day, tour, expected):
    assert ticket_price(category, age, day, tour) == expected


@pytest.mark.parametrize("category", ["unknown", "visitor"])
def test_ticket_price_unknown_category(category):
    with pytest.raises(ValueError, match="unknown category"):
        ticket_price(category, 30, "tuesday", False)


def test_ticket_price_invalid_age():
    with pytest.raises(ValueError, match="invalid age"):
        ticket_price("adult", -1, "tuesday", False)


@pytest.mark.parametrize(
    "group_size, is_school, expected",
    [(20, True, 40), (19, True, 25), (15, False, 20), (8, False, 10), (7, False, 0)],
)
def test_group_discount_branches(group_size, is_school, expected):
    assert group_discount(group_size, is_school) == expected


def test_group_discount_invalid_size():
    with pytest.raises(ValueError, match="invalid group size"):
        group_discount(0, False)


@pytest.mark.parametrize(
    "inside, capacity, timed_slot, expected",
    [(10, 10, False, "wait"), (9, 10, False, "queue"), (9, 10, True, "enter"), (8, 10, False, "enter")],
)
def test_gallery_entry_branches(inside, capacity, timed_slot, expected):
    assert gallery_entry(inside, capacity, timed_slot) == expected
