'''
By: Dustin DeShane
Filename: lab18.py
'''

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks():
    peak_list = []
    for i, val in enumerate(data):
        if i > 0 and i < len(data)-1:
            if data[i] > data[i-1] and data[i] > data[i+1]:
                peak_list.append(i)
                #print(i, val)
    #print(peak_list)
    return peak_list

def valleys():
    valley_list = []
    for i, val in enumerate(data):
        if i > 1 and i < len(data)-1:
            if data[i] < data[i-1] and data[i] < data[i+1]:
                valley_list.append(i)
                #print(i, val)
    #print(valley_list)
    return valley_list

def peak_and_valleys():
    pv_list = []
    peaks_list = peaks()
    valleys_list = valleys()
    for i in peaks_list:
        pv_list.append(i)
    for i in valleys_list:
        pv_list.append(i)
    
    pv_list.sort()
    
    print(pv_list)




peaks()
valleys()
peak_and_valleys()


