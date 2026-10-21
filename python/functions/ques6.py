def print_list(item):
    """ print each element of a list on a new line
    """

    for item in item:
        print(item)

        print_list(["A","B","C"])
        print_list([10,20,30,40])