inp = float(input("Give me a number: "))
if inp % 1 == 0:
    print(int(inp))
else:
    print(int((inp + 1) // 1))