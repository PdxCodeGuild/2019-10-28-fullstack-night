'''
lab18-peaks-and-valleys-v1.py

Version1:

Define the following functions:

1: peaks() - Returns the indices of peaks. A peak has a lower number on both the left and the right.

2: valleys() - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

3: peaks_and_valleys() - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.

Good luck
'''

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

#peaks function
def peaks(data):
    peaks_list = []
    index_count = 0
    for datum in data:
        try:
            if data[index_count + 1] < datum > data[index_count - 1]:
                peaks_list.append(index_count)
        except:
            pass
        index_count += 1
    return peaks_list

#print peaks to see that it works
print(peaks(data))

#valleys
def valleys(data):
    valleys_list = []
    index_count = 0
    for datum in data:
        if index_count != 0 or len(data) - 1 < index_count:
            try:
                if data[index_count + 1] > datum < data[index_count - 1]:
                    valleys_list.append(index_count)
            except:
                pass
        index_count += 1
    return  valleys_list

#print valleys to see that it works
print(valleys(data))

#peaks and valleys function
def peaks_and_valleys(data):
    peaks_data = peaks(data)
    valleys_data = valleys(data)
    peaks_and_valleys_data = peaks_data + valleys_data
    peaks_and_valleys_data.sort()
    return peaks_and_valleys_data

#print to see if it works
print(peaks_and_valleys(data))