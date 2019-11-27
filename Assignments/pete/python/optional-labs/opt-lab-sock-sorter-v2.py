'''
Lab: Sock Sorter
V2:
Now you have a mix of types and colors. Represent socks using tuples containing one color and one type ('black', 'crew'). Randomly generate these, and then group them into pairs.
'''
import random
sock_types = ['ankle', 'crew', 'calf', 'thigh']
sock_colors = ['black', 'white', 'blue']
random_socks = []
for i in range(100):
    sock_tuple = (random.choice(sock_types), random.choice(sock_colors))
    random_socks.append(sock_tuple)
# print(random_socks) #test print

# Find the number of duplicates and loners for each sock type. Hint: dictionaries are helpful here.
sock_dictionary = {}
for sock in random_socks:
    if sock not in sock_dictionary:
        sock_dictionary[sock] = 1
    if sock in sock_dictionary:
        sock_dictionary[sock] += 1
# print(sock_dictionary) #test print

for sock in sock_dictionary:
    sock_dictionary[sock] = f"pairs: {sock_dictionary[sock] // 2} singles: {sock_dictionary[sock] % 2}"
print(sock_dictionary) #test print