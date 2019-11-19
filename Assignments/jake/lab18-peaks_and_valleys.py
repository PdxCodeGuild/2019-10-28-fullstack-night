from math import sin
from matplotlib import pylab
from pylab import *

def peakdet(v, thresh):
    maxthresh = []
    minthresh = []
    peaks = []
    valleys = []

    for x, y in v:
        if y > thresh:
            maxthresh.append((x, y))
        elif y < -thresh:
            minthresh.append((x, y))

    for x, y in maxthresh:
        try:
            if (v[x - 1][1] < y) & (v[x + 1][1] < y):
                peaks.append((x, y))
        except Exception:
            pass

    for x, y in minthresh:
        try:
            if (v[x - 1][1] > y) & (v[x + 1][1] > y):
                valleys.append((x, y))
        except Exception:
            pass

    return peaks, valleys


# input signal
t = array(range(100))
series = 0.3 * sin(t) + 0.7 * cos(2 * t) - 0.5 * sin(1.2 * t)

arr = [*zip(t, series)]  # create a list of tuples where the tuples represent the (x, y) values of the function
thresh = 0.54

peaks, valleys = peakdet(arr, thresh)

scatter([x for x, y in peaks], [y for x, y in peaks], color = 'purple')
scatter([x for x, y in valleys], [y for x, y in valleys], color = 'maroon')
plot(t, 100 * [thresh], color='green', linestyle='--', dashes=(5, 3))
plot(t, 100 * [-thresh], color='green', linestyle='--', dashes=(5, 3))
plot(t, series, 'k')
show()