from functools import partial

import pytest
from pytest_bdd import parsers, scenarios, given, when, then, scenario

from cucumbers import CucumberBasket

EXTRA_TYPES = {
    'Number': int,
}

CONVERTORS = {
    'initial': int,
    'some': int,
    'total': int,
}

parse_num = partial(parsers.cfparse, extra_types=EXTRA_TYPES)


@pytest.mark.parametrize(
    ['initial', 'some', 'total'],
    [(0, 3, 3),
     (2, 4, 6),
     (5, 5, 10)])
@scenario('../features/cucumbers.feature', 'Add cucumbers to a basket')
def test_add(initial, some, total):
    pass


# scenarios('../features/cucumbers.feature', example_converters=CONVERTORS)
"""
@scenario('../features/cucumbers.feature', 'Add cucumbers to a basket')
def test_add():
    pass


@scenario('../features/cucumbers.feature', 'Remove cucumbers from the basket')
def test_remove():
    pass
"""


@given(parse_num('the basket has "{initial:Number}" cucumbers'))
@given(parse_num('the basket has "<initial>" cucumbers'))
def basket(initial):
    return CucumberBasket(initial_count=initial)


@when(parse_num('"{some:Number}" cucumbers are added to the basket'))
@when(parse_num('"<some>" cucumbers are added to the basket'))
def add_cucumbers(basket, some):
    basket.add(some)


@when(parse_num('"{some:Number}" cucumbers are removed from the basket'))
@when(parse_num('"<{>some>" cucumbers are removed from the basket'))
def remove_cucumbers(basket, some):
    basket.remove(some)


@then(parse_num('the basket contains "{total:Number}" cucumbers'))
@then(parse_num('the basket contains "<total>" cucumbers'))
def basket_has_total(basket, total):
    assert basket.count == total
