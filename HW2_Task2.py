#Exercise_2a
a = int(input("a = "))
b = int(input("b = "))
x = int(input("x = "))
y = int(input("y = "))
print("Total -", a*b*x*y)


#Exercise_2a_alt_sol
four_digit_num = input("Only four digits please - ")
result_2a = int(four_digit_num[0]) * int(four_digit_num[1]) * int(four_digit_num[2]) * int(four_digit_num[3])
print(result_2a)


#Exercise_2b
number1 = input("Please enter a number - ")
reverse_number = int(str(number1)[::-1])
print("The reverse number - {}".format(reverse_number))


#Exercise_2c
number2 = input("Please enter a value - ")
ascending = "".join(sorted(str(number2)))
print("The ascending order - {}".format(ascending))

number3 = input("Please enter a value - ")
descending = "".join(sorted(str(number3), reverse=True))
print("The descending order - {}".format(descending))