input = input()

parts = input.split()
nums = []

for item in parts:
    try:
        item = int(item)
        nums.append(item)
    except ValueError:
        pass

print("YES" if nums[0] + nums[1] == nums[2] else "NO")