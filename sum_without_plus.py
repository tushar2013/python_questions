def add_numbers(x, y):
    while y != 0:
        temp = x & y
        x = x ^ y
        y = temp << 1
    return x
 
num1 = 16
num2 = 29
sum_result = add_numbers(num1, num2)
print(f"Sum of {num1} and {num2} is: {sum_result}")
