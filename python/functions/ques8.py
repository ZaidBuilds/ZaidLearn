def capitalize_list_items(lst):
    """
    Return a new list with each list item capitalized.
    """
    capitalized_list = []

    for item in lst:
        capitalized_list.append(item.capitalize())

    return capitalized_list


# Testing
print(capitalize_list_items(["apple", "banana", "mango"]))
# ['Apple', 'Banana', 'Mango']

print(capitalize_list_items(["hello", "zaid", "python"]))
# ['Hello', 'Zaid', 'Python']
