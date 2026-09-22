parts = input().strip().split('" "', 1)

if len(parts) != 2:
    print("none")
else:
    key = parts[0].strip('"')
    text = parts[1].strip('"')
    found = text.count(key)
    print(found if found else "none")