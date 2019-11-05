
def rot13(message):
  encoded_message = []
  for c in message:
    e = ord(c)
    if e >= 97 and e < 97 + 26:
      e -= 97
      e += 13
      e %= 26
      e += 97
      encoded_message.append(chr(e))
    elif e >= 65 and e < 65 + 26:
      e -= 65
      e += 13
      e %= 26
      e += 65
      encoded_message.append(chr(e))
    else:
      encoded_message.append(chr(e))


  return "".join(encoded_message)
  


print(rot13(rot13("HaIl CaEsAr")))
print(rot13("hedwig dies on page 17"))