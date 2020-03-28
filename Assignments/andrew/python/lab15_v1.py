tens_places = {
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
ones_place = {
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

def tens_plus(number):
  tens = number // 10
  ones = number % 10
  if number < 20: 
    return ones_place[number]
  elif number >= 20:
    return f"{tens_places[tens]}"-"{ones_place[ones]}".strip("-")

def hundreds_plus(number):
  if number < 100:
    return tens_plus(number)
  elif number >= 100:
    hundreds = number // 100
    return f"{ones_place[hundreds]} hundred {tens_plus(number % 100)}"

assert tens_plus(5) == "five"
assert tens_plus(12) == "twelve"
assert tens_plus(13) == "thirteen"
assert tens_plus(15) == "fifteen"
assert tens_plus(18) == "eighteen"
assert tens_plus(30) == "thirty"
assert tens_plus(55) == "fifty-five"

assert hundreds_plus(50) == "fifty"
assert hundreds_plus(666) == "six hundred sixty-six"
assert hundreds_plus(958) == "nine hundred fifty-eight"