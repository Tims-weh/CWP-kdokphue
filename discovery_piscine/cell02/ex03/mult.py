first_num = int(input("Enter the first number: "))
sec_num = int(input("Enter the second number: "))
multi = first_num * sec_num
print(f"{first_num} x {sec_num} = {multi}")
if multi > 0:
    print("The result is positive.")
elif multi < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")