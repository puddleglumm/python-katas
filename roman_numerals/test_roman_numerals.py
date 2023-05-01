from roman_numerals import roman_numeral_of
import pytest


@pytest.mark.parametrize("arabic_number,expected",
                         [(1, "I"), (2, "II"), (3, "III"),
                          (4, "IV"),
                          (5, "V"), (6, "VI"), (7, "VII"), (8, "VIII"),
                          (9, "IX"),
                          (10, "X"), (13, "XIII"), (14, "XIV"),
                          (15, "XV"), (18, "XVIII"),
                          (19, "XIX"), (20, "XX"), (29, "XXIX"), (34, "XXXIV"),
                          (40, "XL"), (47, "XLVII"), (50, "L"), (53, "LIII"),
                          (80, "LXXX"), (83, "LXXXIII"), (89, "LXXXIX")
                          ])
def test_roman_numeral_of(arabic_number, expected):
    roman = roman_numeral_of(arabic_number)
    assert roman == expected
