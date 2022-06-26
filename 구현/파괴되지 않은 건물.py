def solution(board, skill):
    answer = 0
    R = len(board)
    C = len(board[0])
    tmp = [[0] * (C + 1) for _ in range(R + 1)]  # 누적합 기록을 위한 배열

    for type, r1, c1, r2, c2, degree in skill:
        # 누적합 기록, 부호에 주의할 것
        tmp[r1][c1] += degree if type == 2 else -degree
        tmp[r1][c2 + 1] += -degree if type == 2 else degree
        tmp[r2 + 1][c1] += -degree if type == 2 else degree
        tmp[r2 + 1][c2 + 1] += degree if type == 2 else -degree

    # 행 기준 누적합
    for i in range(R):
        for j in range(C):
            tmp[i][j + 1] += tmp[i][j]

    # 열 기준 누적합
    for j in range(C):
        for i in range(R):
            tmp[i + 1][j] += tmp[i][j]

    # 기존 배열과 합함
    for i in range(R):
        for j in range(C):
            board[i][j] += tmp[i][j]
            # board에 값이 1이상인 경우 answer++
            if board[i][j] > 0: answer += 1

    return answer