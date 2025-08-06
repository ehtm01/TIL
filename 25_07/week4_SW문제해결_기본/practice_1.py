# import sys
#
# sys.stdin = open("연습문제1_in.txt", "r")
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#     max_sum = 0
#
#     matrix = [list(map(int, input().split())) for _ in range(N)]
#
#     for i in range(N):
#         for j in range(N):
#             sum_x = matrix[i][j]
#             for di, dj in [-1, -1], [-1, 1], [1, -1], [1, 1]:
#                 for dist in range(1, 3):
#                     ni, nj = i + di * dist, j + dj * dist
#                     if 0 <= ni < N and 0 <= nj < N:
#                         sum_x += matrix[ni][nj]
#
#             max_sum = max(max_sum, sum_x)
#
#     print(f'#{tc} {max_sum}')

import sys

sys.stdin = open("연습문제1_in.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 대각선의 합 구하기
    total = 0

    # ↘ 대각선
    # total_right = matrix[0][0] + matrix[1][1] + ... + matrix[N-1][N-1]
    for i in range(N):
        total += matrix[i][i]

    # ↙ 대각선
    # total_left = matrix[0][N-1] + matrix[1][N-1-1] + ... + matrix[N-1][N-1 - (N-1)]
    for i in range(N):
        total += matrix[i][N-1-i]

    # N = 5 라고 했으니 정중앙 겹치는 부분 존재
    total -= matrix[N//2][N//2]

    print(f"#{tc} {total}")