def reverse_list(lst):
    # return a new list that is the reverse of the input list
    reversed_list = []

    # iterate from last index to first index
    for i in range(len(lst) - 1, -1, -1):
        reversed_list.append(lst[i])

    return reversed_list


# testing (print OUTSIDE the function)
print(reverse_list([1, 2, 3, 4, 5]))

