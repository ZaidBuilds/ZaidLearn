def calculate_slope(x1,y1,x2,y2):

    if x2 ==x1:
        return "slope is undefined (vertical line)."
    
    return (y2-y1)/(x2-x1)

#teting
print(calculate_slope(2,3,6,15))
print(calculate_slope(1,4,1,10))
print(calculate_slope(0,0,5,5))
