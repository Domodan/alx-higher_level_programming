#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return list(map(lamda i: replace if i == search else i, my_list))
