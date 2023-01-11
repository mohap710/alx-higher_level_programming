#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    " @my_list is the initial list
    " @search is the element to replace in the list
    " @replace is the new element
    """
    return (list(map(lambda x: replace if x == search else x, my_list)))
