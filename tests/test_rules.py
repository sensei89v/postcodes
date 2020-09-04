import pytest
from src.uk_rules import (
    _check_first_position,
    _check_second_position,
    _check_third_position,
    _check_fourth_position,
    _check_final_two_letters,
    _check_only_one_double_position,
    _check_zero_district,
    _check_single_digit_district,
    _check_central_london
)


@pytest.mark.parametrize("area, district, result", [
    ('SK', '9', True),
    ('S', '9', True),
    ('Q', '9', False),
    ('QA', '9', False),
    ('V', '9', False),
    ('VA', '9', False),
    ('X', '9', False),
    ('XA', '9', False),
    ('SQ', '9A', True),
    ('SV', '9A', True),
])
def test_check_first_position(area, district, result):
    assert _check_first_position(area, district, "1", "ZZ") == result


@pytest.mark.parametrize("area, district, result", [
    ('SK', '9', True),
    ('S', '9', True),
    ('SI', '9', False),
    ('SJ', '9', False),
    ('SZ', '9', False),
    ('IJ', '9', False),
    ('IS', '9', True),
    ('JS', '95', True),
    ('ZS', '91', True),
])
def test_check_second_position(area, district, result):
    assert _check_second_position(area, district, "1", "ZZ") == result


@pytest.mark.parametrize("area, district, result", [
    ('S', '9A', True),
    ('S', '9D', True),
    ('S', '9I', False),
    ('SP', '9I', True),
    ('S', '91', True),
    ('S', '9', True),
])
def test_check_third_position(area, district, result):
    assert _check_third_position(area, district, "1", "ZZ") == result


@pytest.mark.parametrize("area, district, result", [
    ('SA', '9A', True),
    ('SA', '9E', True),
    ('SA', '9I', False),
    ('S', '9I', True),
    ('SA', '91', True),
    ('S', '91', True),
    ('SA', '9', True),
])
def test_check_fourth_position(area, district, result):
    assert _check_fourth_position(area, district, "1", "ZZ") == result


@pytest.mark.parametrize("unit, result", [
    ('SA', True),
    ('SC', False),
    ('CS', False),
    ('AA', True),
    ('JJ', True),
    ('SV', False),
    ('VO', False),
])
def test_check_final_two_letters(unit, result):
    assert _check_final_two_letters("SA", "9", "9", unit) == result


@pytest.mark.parametrize("area, district, result", [
    ('AB', '9A', False),
    ('AB', '93', True),
    ('AB', '9', False),
    ('LL', '9A', False),
    ('LL', '93', True),
    ('LL', '9', False),
    ('SO', '9A', False),
    ('SO', '93', True),
    ('SO', '9', False),
    ('A', '9A', True),
    ('A', '93', True),
    ('A', '9', True),
    ('AA', '9A', True),
    ('AA', '93', True),
    ('AA', '9', True),
])
def test_check_only_one_double_position(area, district, result):
    assert _check_only_one_double_position(area, district, "1", "ZZ") == result


@pytest.mark.parametrize("area, district, result", [
    ('BL', '0', True),
    ('BL', '9', True),
    ('BL', '10', False),
    ('BL', '1A', True),
    ('BL', '11', True),
    ('BA', '0', False),
    ('BA', '10', True),
    ('BA', '1A', True),
])
def test_check_zero_district(area, district, result):
    assert _check_zero_district(area, district, "1", "ZZ") == result


@pytest.mark.parametrize("area, district, result", [
    ('BR', '0', True),
    ('BR', '9', True),
    ('BR', '22', False),
    ('BL', '0', True),
    ('BL', '9', True),
    ('BL', '22', True),
])
def test_check_single_digit_district(area, district, result):
    assert _check_single_digit_district(area, district, "1", "ZZ") == result


@pytest.mark.parametrize("area, district, result", [
    ('EC', '2A', True),
    ('EC', '1', False),
    ('EC', '21', False),
    ('EC', '5', True),          # TODO: think
    ('WC', '1B', True),
    ('WC', '2C', True),
    ('WC', '2', False),
    ('WC', '22', False),
    ('W', '1A', True),
    ('W', '2', True),
    ('W', '1', False),
    ('W', '24', True),
    ('W', '14', True),
    ('W', '2A', False),
    ('SW', '1A', True),
    ('SW', '1', False),
    ('SW', '2', True),
    ('SW', '24', True),
    ('SW', '14', True),
    ('SW', '2A', False),
    ('E', '1', True),
    ('E', '1C', False),
    ('E', '1W', True),
    ('E', '11', True),
    ('E', '2', True),
    ('E', '21', True),
    ('E', '2W', False),
    ('N', '1', True),
    ('N', '1C', True),
    ('N', '1P', True),
    ('N', '1W', False),
    ('N', '11', True),
    ('N', '2', True),
    ('N', '21', True),
    ('N', '2W', False),
    ('NW', '1', True),
    ('NW', '1C', False),
    ('NW', '1W', True),
    ('NW', '11', True),
    ('NW', '2', True),
    ('NW', '21', True),
    ('NW', '2W', False),
    ('SE', '1', True),
    ('SE', '1C', False),
    ('SE', '1P', True),
    ('SE', '11', True),
    ('SE', '2', True),
    ('SE', '21', True),
    ('SE', '2P', False),
    ('P', '1', True),
    ('P', '12', True),
    ('P', '1A', False),
    ('PA', '1', True),
    ('PA', '12', True),
    ('PA', '1A', False),
])
def test_check_central_london(area, district, result):
    assert _check_central_london(area, district, "1", "ZZ") == result
