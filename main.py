with open('27-A.txt') as f:
    count_row = int(f.readline())
    count_even, count_odd, total_sum = 0, 0, 0
    diff_parity_more_less_array = []
    for row in range(count_row):
        numbers_array = sorted(list(map(int, f.readline().split())))
        max_number = numbers_array[1]
        if max_number % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
        total_sum += max_number
        a, b = numbers_array
        if a % 2 == b % 2:
            diff_parity_more_less_array.append([abs(a - b), '00'])
        else:
            if a % 2 == 0:
                diff_parity_more_less_array.append([abs(a - b), '01'])
            else:
                diff_parity_more_less_array.append([abs(a - b), '01'])

diff_parity_more_less_array = sorted(diff_parity_more_less_array)
i = 0
while True:
    if count_even > count_odd and total_sum % 2 != 0 or count_odd > count_even and total_sum % 2 == 0:
        total_sum -= diff_parity_more_less_array[i][0]
        if diff_parity_more_less_array[i][1] == '01':
            count_even += 1
            count_odd -= 1
        elif diff_parity_more_less_array[i][1] == '10':
            count_even -= 1
            count_odd += 1
    else:
        print(total_sum)
        break
    i += 1