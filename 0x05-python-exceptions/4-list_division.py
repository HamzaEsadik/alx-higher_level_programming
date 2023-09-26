#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newlist = []
    for j in range(0, list_length):
        try:
            dv = my_list_1[j] / my_list_2[j]
        except TypeError:
            print("wrong type")
            dv = 0
        except ZeroDivisionError:
            print("division by 0")
            dv = 0
        except IndexError:
            print("out of range")
            dv = 0
        finally:
            newlist.append(dv)
    return (newlist)
