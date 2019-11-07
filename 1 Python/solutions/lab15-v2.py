tens_words = {
  0: '',
  2: 'twenty',
  3: 'thirty',
  4: 'fourty',
  5: 'fifty',
  6: 'sixty',
  7: 'seventy',
  8: 'eighty',
  9: 'ninety',
}
ones_words = {
  0: '',
  1: 'one',
  2: 'two',
  3: 'three',
  4: 'four',
  5: 'five',
  6: 'six',
  7: 'seven',
  8: 'eight',
  9: 'nine',
  10: 'ten',
  11: 'eleven',
  12: 'twelve',
  13: 'thirteen',
  14: 'fourteen',
  15: 'fifteen',
  16: 'sixteen',
  17: 'seventeen',
  18: 'eighteen',
  19: 'nineteen'
}

def two_digit_number_to_phrase(number):
  tens = number // 10
  ones = number % 10
  if number < 20: 
    return ones_words[number]
  elif number >= 20:
    return f"{tens_words[tens]}-{ones_words[ones]}".strip("-")

def three_digit_number_to_phrase(number):
  if number < 100:
    return two_digit_number_to_phrase(number)
  elif number >= 100:
    hundreds = number // 100
    return f"{ones_words[hundreds]} hundred {two_digit_number_to_phrase(number % 100)}"

# Test two_digit_number_to_phrase!
assert two_digit_number_to_phrase(5) == "five"
assert two_digit_number_to_phrase(12) == "twelve"
assert two_digit_number_to_phrase(13) == "thirteen"
assert two_digit_number_to_phrase(15) == "fifteen"
assert two_digit_number_to_phrase(18) == "eighteen"
assert two_digit_number_to_phrase(30) == "thirty"
assert two_digit_number_to_phrase(55) == "fifty-five"

# Test three_digit_number_to_phrase
assert three_digit_number_to_phrase(50) == "fifty"
assert three_digit_number_to_phrase(666) == "six hundred sixty-six"
assert three_digit_number_to_phrase(958) == "nine hundred fifty-eight"