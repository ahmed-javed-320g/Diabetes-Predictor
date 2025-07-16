age = int(input("Enter your age:"))
has_license = False

if age >= 18:
    is_eligible = True
else:
    is_eligible = False

if has_license and is_eligible:
    print("you can drive")
else:
    if is_eligible == False:
        print("you are not eligible")
    if has_license == False:
        print("you do not have a license")
    print("you can not drive")