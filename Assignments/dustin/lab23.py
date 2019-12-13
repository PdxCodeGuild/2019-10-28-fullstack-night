'''
By: Dustin DeShane
Filename: lab23.py
'''
songs = []

with open("songlist.csv", 'r') as song_list:
    rows = song_list.read().split('\n')
    headers = rows.pop(0).split(',') #set first row as headers/keys
    #print(headers)
    for row in rows:
        row = row.split(',') #iterate through rows and split them into component parts

        # Normal way
        # song = {}
        # for i in range(len(headers)):
        #     song[headers[i]] = row[i]

        # Fancy python way
        song = dict(zip(headers, row))
        
        songs.append(song)

print(songs)
















