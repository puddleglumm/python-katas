from roman_numerals import roman_numeral_of
import pytest


@pytest.mark.parametrize("arabic_number,expected",
                         [(1, "I"), (2, "II"), (3, "III"),
                          (4, "IV"),
                          (5, "V"), (6, "VI"), (7, "VII"), (8, "VIII"),
                          (9, "IX"),
                          (10, "X"), (13, "XIII"), (14, "XIV"),
                          (15, "XV"), (18, "XVIII")
                          ])
def test_roman_numeral_of(arabic_number, expected):
    roman = roman_numeral_of(arabic_number)
    assert roman == expected
