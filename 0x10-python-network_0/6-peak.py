#!/usr/bin/python3
'python interview module'


def find_peak(list_of_integers):
    'finds a peak in a list of unsorted integers'
    if list_of_integers:
        peak = list_of_integers[0]
        for element in list_of_integers:
            if element > peak:
                peak = element
        return peak
    else:
        return None
