number = int(input("enter a number: "))
is_even  = False

if number % 2 == 0:
    is_even = True
else:
    is_even = False

if is_even:
    print("it is even")
else:
    print("it is odd")