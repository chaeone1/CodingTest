def solution(want, number, discount):
    answer = 0

    for i in range(len(discount) - 9):
        ten_days = discount[i:i+10]

        is_possible = True

        for j in range(len(want)):
            if ten_days.count(want[j]) < number[j]:
                is_possible = False
                break

        if is_possible:
            answer += 1

    return answer