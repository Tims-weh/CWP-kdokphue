import sys

if len(sys.argv) > 1:
    params = sys.argv[1:]
    print(f"parameters: {len(params)}")
    for i in params:
        print(f"{i}: {len(i)}")
else:
    print("none")
