def peaks(data):
    peak_indices = []
    for i in range(1, len(data)-1):  
        left = data[i-1]
        middle = data[i]
        right = data[i+1]
        if left < middle and right < middle:
            peak_indices.append(i)
    return peak_indices

def valleys(data):
    valley_indices = []
    for i in range(1, len(data)-1):
        left = data[i-1]
        middle = data[i]
        right = data[i+1]
        if left > middle and right > middle:
            valley_indices.append(i)
    return valley_indices


def main():
    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
    print(peaks(data))
    print(valleys(data))


main()
