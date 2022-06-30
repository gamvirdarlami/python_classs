# a = 10
# b = 30
# if a > b:
#     print("a is greater than b")
# else:
#     print("b is greater than a")    

x = int(input("enter a number:"))
y = int(input("enter 2nd number:"))
z = int(input("enter 3rd number:"))
if x > y and x > z:
    print("x is greater than y and z")
elif y > x and y > z:
    print("y is greater than x and z")
else:
    print("z is greater than x and y")