import sys
import re

if len(sys.argv) == 3:
    key = sys.argv[1]
    text = sys.argv[2]
    found = len(re.findall(key, text))
    if found:
        print(found)
    else:
        print("none")
else:
    print("none")
