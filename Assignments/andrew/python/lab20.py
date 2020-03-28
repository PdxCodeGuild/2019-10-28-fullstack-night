def get_second_digit(num):
    if num < 10:
        return None
    return num % 10


def validate_credit_card(cc_str):
    if len(cc_str) != 16:
        return False

    cc = []
    for i in range(len(cc_str)):
        cc.append(int(cc_str[i]))

    check_digit = cc.pop(-1)
    cc.reverse()
    for i in range(0, len(cc), 2):
        cc[i] *= 2
    total = 0
    for i in range(len(cc)):
        if cc[i] > 9:
            cc[i] -= 9
        total += cc[i]
    second_digit = get_second_digit(total)
    return second_digit == check_digit


credit_card_str = '4556737586899855'
print(validate_credit_card(credit_card_str))
