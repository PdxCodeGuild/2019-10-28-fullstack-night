ones = ['zero', 
        'one', 
        'two',
        'three', 
        'four', 
        'five', 
        'six', 
        'seven', 
        'eight', 
        'nine']
teen = ['ten', 
        'eleven', 
        'twelve', 
        'thirteen', 
        'fourteen', 
        'fifteen', 
        'sixteen', 
        'seventeen', 
        'eighteen', 
        'nineteen']
tens = ['zeroty', 
        'onety', 
        'twenty', 
        'thirty', 
        'forty', 
        'fifty', 
        'sixty', 
        'seventy', 
        'eighty', 
        'ninety']

def find_thou(num):
    hundreds_num = num % 1000
    thou_num = num // 1000
    thou_word = ones[thou_num]+'-thousand'

    return thou_word + ' ' + find_hundred(hundreds_num)

def find_hundred(num):
    tens_num = num % 100
    hundred_num = num // 100

    hundreds_phrase = ones[hundred_num]+'-hundred'

    return hundreds_phrase + ' ' + find_ten(tens_num)

def find_ten(num):
    if num < 10:
        return ones[num]
    elif num < 20:
        return teen[num - 10]
    elif num < 100:
        ten_num = num // 10
        one_num = num % 10
        if one_num == 0:
            return tens[ten_num]
        else:
            return tens[ten_num] + '-' + ones[one_num]

num = int(input('what number would you like to convert? '))

if num < 100:
    print(find_ten(num))
elif num < 1000:
    print(find_hundred(num))
else:
    print(find_thou(num))