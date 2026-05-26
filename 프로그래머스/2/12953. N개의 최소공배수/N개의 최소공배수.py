def solution(arr):
    max_num = max(arr)

    candidate = max_num

    while True:
        is_lcm = True

        for num in arr:
            if candidate % num != 0:
                is_lcm = False
                break

        if is_lcm:
            return candidate

        candidate += 1