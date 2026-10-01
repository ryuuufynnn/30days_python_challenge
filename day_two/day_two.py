def find_smallest_missing_num(nums: int) -> int:
    
    is_found = True
    candidate = 1
    
    while True:
        is_found = False
        
        for n in nums:
            if n == candidate:
                is_found = True
                break
        if is_found == False:
            return candidate
        
        candidate += 1
    
nums = [-3, -2, 0, 1, 2]

print(find_smallest_missing_num(nums)) # result: 3