emotion_dict = {}
while True:
    user_feeling = input('how are you feeling? ')

    if user_feeling in emotion_dict:
        emotion_dict[user_feeling] +=1
    else:
        emotion_dict[user_feeling] = 1

print(emotion_dict)
