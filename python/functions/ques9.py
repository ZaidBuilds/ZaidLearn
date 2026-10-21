def add_item(lst, item):
    """ return a new list with the given item added at the end
    """
    new_list = lst.copy()
    new_list.append(item)
    return new_list

#testing 
food_staff = ['potato','tomato','mango','milk']
print(add_item(food_staff,'meat'))

numbers =[2,3,7,9]
print(add_item(numbers, 5))
print(numbers)
