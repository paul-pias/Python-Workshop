limit = 40

number = 1
while number**2 <limit:
    square = number**2
    print("{}:{}".format(number, square))
    number += 1
    
nearest_square = square
print(nearest_square)