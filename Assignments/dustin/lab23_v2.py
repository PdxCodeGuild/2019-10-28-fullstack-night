


def create():
    questions = ["Name a song: ", "Who's it by?: ", "What genre?: ", "Duration?: ", "What's the date?: "]
    new_row = []
    for i in range(5):
        answer = input(f"{questions[i]}")
        new_row.append(answer)
    new_song = dict(zip(headers, new_row))
    songs.append(new_song)
    #return new_row

def retrieve(songs):
    print("Please select a song below: ")
    for i in range(len(songs)):
        print(songs[i]['title'])
    user_choice = input("Which song?: ")
    for i in range(len(songs)):
        if user_choice == songs[i]['title']:
            print(songs[i])

    return songs[i]

def update(songs, headers):
    song_choice = retrieve(songs)
    print("Please select a field to update: ")
    for i in headers:
        print(i, end = " " )
    update_choice = input("Which field?: ")
    for i, val in enumerate(headers):
        if update_choice == val:
            print(update_choice)
            print(i)
            print(val)
            print(songs[i-1])
            print(song_choice)
            change = input("What do you want to change it to?: ")
            song_choice.update({song_choice[update_choice]: change})
            print(song_choice)
    #return update_choice  

def delete():
    pass
    

songs = []
with open('songlist.csv', 'r') as song_list:
    rows = song_list.read().split('\n')
    headers = rows.pop(0).split(',')
    
    
    for row in rows:
        row = row.split(',')
        song = dict(zip(headers, row))
        songs.append(song)
    
    #create()    

    #retrieve(songs)
    
    update(songs, headers)
    


    #print(songs)

        