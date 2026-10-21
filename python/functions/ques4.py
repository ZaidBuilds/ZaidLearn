def check_season(month):
    """
    Return the season name based on the given month.
    """
    month = month.lower()

    if month in ("september", "october", "november"):
        return "Autumn"
    elif month in ("december", "january", "february"):
        return "Winter"
    elif month in ("march", "april", "may"):
        return "Spring"
    elif month in ("june", "july", "august"):
        return "Summer"
    else:
        return "Invalid month"


# Testing
print(check_season("march"))     # Spring
print(check_season("october"))   # Autumn
print(check_season("january"))   # Winter
print(check_season("july"))      # Summer
print(check_season("hello"))     # Invalid month
