T = int(input())

for tc in range(1, T+1):
    N = 10
    numbers = list(map(int, input().split()))

    cnt_0 = 0

    for i in range(1 << N):
        num_lst = []
        for j in range(N):
            if i & (1 << j):
                num_lst.append(numbers[j])
        if sum(num_lst) == 0:
            cnt_0 += 1

    print(f'{tc} {cnt_0}')