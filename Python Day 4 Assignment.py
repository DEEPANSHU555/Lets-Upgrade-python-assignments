def sum_of_squares(numbers):
    """Returns the sum of the squares of all the numbers in the list."""
    return sum(x ** 2 for x in numbers)
list=[1,2,3,4,5]
print("The Sum Is:"+str(sum_of_squares(list)))
