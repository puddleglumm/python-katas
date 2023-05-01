roman_symbol_values = {
    "I": 1,
    "IV": 4,
    "V": 5,
    "IX": 9,
    "X": 10
}


def roman_numeral_of(arabic_number: int):
    remaining_value: int = arabic_number
    roman_representation: str = ""

    for symbol in reversed(roman_symbol_values):
        symbol_value = roman_symbol_values[symbol]
        while remaining_value >= symbol_value:
            remaining_value -= symbol_value
            roman_representation += symbol

    return roman_representation
