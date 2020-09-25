max_num = 0
nums = 0
for i in range(1016, 7937 + 1):
    if i % 3 == 0:
        if i % 7 != 0:
            if i % 17 != 0:
                if i % 19 != 0:
                    if i % 27 != 0:
                        nums += 1
                        if i > max_num:
                            max_num = i
print(nums, max_num)