from roman_numerals import roman_numeral_of
import pytest


@pytest.mark.parametrize("arabic_number,expected",
                         [(1, "I"), (2, "II"), (3, "III")])
def test_i(arabic_number, expected):
    roman = roman_numeral_of(arabic_number)
    assert roman == expected

def test_iv():
    roman = roman_numeral_of(4)
    assert roman == "IV"

@pytest.mark.parametrize("arabic_number,expected",
                         [(5, "V"), (6, "VI"), (7, "VII"), (8, "VIII")])
def test_5_through_8(arabic_number, expected):
    roman = roman_numeral_of(arabic_number)
    assert roman == expected

def test_ix():
    roman = roman_numeral_of(9)
    assert roman == "IX"


@pytest.mark.parametrize("arabic_number,expected",
                         [(10, "X"), (13, "XIII"), (14, "XIV"), (15, "XV"), (18, "XVIII")])
def test_10_through_18(arabic_number, expected):
    roman = roman_numeral_of(arabic_number)
    assert roman == expected


