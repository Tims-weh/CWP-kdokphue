nums = input().split()

if len(nums) == 2:
    start_num, end_num = int(nums[0]), int(nums[1])
    step = 1 if start_num < end_num else -1
    print(list(range(start_num, end_num + step, step)))
else:
    print("none")