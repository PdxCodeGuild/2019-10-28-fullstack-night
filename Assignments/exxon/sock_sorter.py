import random 

# generating new list of random socks 

sock_types = ['ankle', 'crew', 'calf', 'thigh']
new_sock_list = []
sock_pairs = {}
loner_socks_list = []


for i in range(100):
    sock_chosen = random.choice(sock_types)
    new_sock_list.append(sock_chosen)

print(new_sock_list)








print('\n')

# searching new sock list for pairs getting a count and adding to duplicate socks dictionary 

for item in (new_sock_list):
    if item in sock_pairs:
        sock_pairs[item] +=1
    else:
        sock_pairs[item] =1 

# print(sock_pairs)







# Calculating if there are lone socks  in the sock pair dictionaries by dividing and mod


for key in sock_pairs:
    
    
    # math to calculate single socks 
    
    loner_socks = sock_pairs[key] % 2

    for i in range(loner_socks):

        loner_socks_list.append(key)
        
# print (loner_socks_list)    

print('\n')




print('you have these single socks :')
print(', '.join(loner_socks_list))
print('\n')
print ("you have these pairs :")
print('\n'.join("{}: {}".format(k, v) for k, v in sock_pairs.items()))


