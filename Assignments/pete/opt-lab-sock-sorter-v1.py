'''
Lab: Sock Sorter
V1:
You've just finished laundry and your expansive sock collection is in complete disorder. Sort your socks into pairs and pull out any loners.
'''
import random
# Generate a list of 100 random socks, randomly chosen from a set of types: sock_types = ['ankle', 'crew', 'calf', 'thigh']:
sock_types = ['ankle', 'crew', 'calf', 'thigh']
random_socks = []
for i in range(100):
    random_socks.append(random.choice(sock_types))
print(random_socks) #test print

# Find the number of duplicates and loners for each sock type. Hint: dictionaries are helpful here.
sock_dictionary = {}
for sock in random_socks:
    if sock not in sock_dictionary:
        sock_dictionary[sock] = 1
    if sock in sock_dictionary:
        sock_dictionary[sock] += 1
print(sock_dictionary) #test print

for sock in sock_dictionary:
    sock_dictionary[sock] = f"pairs: {sock_dictionary[sock] // 2} singles: {sock_dictionary[sock] % 2}"
print(sock_dictionary) #test print