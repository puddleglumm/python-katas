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
        while remaining_value >= roman_symbol_values[symbol]:
            remaining_value -= roman_symbol_values[symbol]
            roman_representation += symbol

    return roman_representation
