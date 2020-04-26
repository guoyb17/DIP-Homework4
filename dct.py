from math import cos, sqrt, pi
from copy import deepcopy
import numpy as np


def my_dct_1d(f, N, M):
    '''
    1d First-Row-Then-Column DCT.
    f: input data (N * N).
    M: output size (M * M).
    M <= N.
    return: 2d array [
        [g0, g1, ..., g_(M - 1)],
        ......
    ]
    '''
    tmp = []
    for row in range(N):
        tmp.append([])
        for column in range(N):
            part_sum = 0.0
            for iter_c in range(N):
                part_sum += f[row][iter_c] * cos((2 * iter_c + 1) * column * pi / 2 / N)
            tmp[row].append(sqrt((1 if column == 0 else 2) / N) * part_sum)
    ans = deepcopy(tmp)
    for column in range(N):
        for row in range(N):
            part_sum = 0.0
            for iter_r in range(N):
                part_sum += tmp[iter_r][column] * cos((2 * iter_r + 1) * row * pi / 2 / N)
            ans[row][column] = sqrt((1 if row == 0 else 2) / N) * part_sum
    ret = []
    for row in range(M):
        ret.append(ans[row][0 : M])
    return np.array(ret)

def my_idct_1d(F, M, N):
    '''
    1d First-Row-Then-Column IDCT.
    f: input data (M * M).
    N: output size (N * N).
    M <= N.
    '''
    F_reshape = np.zeros((N, N))
    for row in range(N):
        if row < M:
            for column in range(M):
                F_reshape[row][column] = F[row][column]
            for column in range(M, N):
                F_reshape[row][column] = 0.0
        else:
            for column in range(N):
                F_reshape[row][column] = 0.0
    tmp = deepcopy(F_reshape)
    for column in range(N):
        for row in range(N):
            part_sum = 0.0
            for iter_r in range(N):
                part_sum += sqrt((1 if iter_r == 0 else 2) / N) * cos((2 * row + 1) * iter_r * pi / 2 / N) * F_reshape[iter_r][column]
            tmp[row][column] = part_sum
    ans = deepcopy(tmp)
    for row in range(N):
        for column in range(N):
            part_sum = 0.0
            for iter_c in range(N):
                part_sum += sqrt((1 if iter_c == 0 else 2) / N) * cos((2 * column + 1) * iter_c * pi / 2 / N) * tmp[row][iter_c]
            ans[row][column] = part_sum
    return np.array(ans)

def my_dct_2d(f, N, block, part):
    '''
    2d DCT.
    f: input data (N * N).
    block: partition size (rec: 8).
    part: n part for using only 1/n^2 of DCT coefficients. Please use 1, 2, 4, 8 with input 512 * 512 image.
    return: 2d array [
        [g0, g1, ..., g_(M - 1)],
        ......
    ]
    '''
    ans = np.zeros((int(N / part), int(N / part)))
    blocked_size = int(N / block)
    block_range = int(block / part)
    for iter_b_i in range(blocked_size):
        for iter_b_j in range(blocked_size):
            tmp = []
            for u in range(block):
                tmp.append([])
                for v in range(block):
                    part_sum = 0
                    for x in range(block):
                        for y in range(block):
                            part_sum += f[iter_b_i * block + x][iter_b_j * block + y] * cos((2 * x + 1) * u * pi / 2 / block) * cos((2 * y + 1) * v * pi / 2 / block)
                    tmp[u].append(part_sum * sqrt((1 if u == 0 else 2) / block) * sqrt((1 if v == 0 else 2) / block))
            for iter_ans_i in range(block_range):
                for iter_ans_j in range(block_range):
                    ans[iter_b_i * block_range + iter_ans_i][iter_b_j * block_range + iter_ans_j] = tmp[iter_ans_i][iter_ans_j]
    return ans

def my_idct_2d(F, N, block, part):
    '''
    2d IDCT.
    Please use the SAME input of my_dct_2d except for F, which is DCT result replacing f.
    '''
    ipt_reshape = np.zeros((N, N))
    blocked_size = int(N / block)
    block_range = int(block / part)
    for iter_b_i in range(blocked_size):
        for iter_b_j in range(blocked_size):
            for iter_ans_i in range(block):
                if iter_ans_i < block_range:
                    for iter_ans_j in range(block):
                        if iter_ans_j < block_range:
                            ipt_reshape[iter_b_i * block + iter_ans_i][iter_b_j * block + iter_ans_j] = F[iter_b_i * block_range + iter_ans_i][iter_b_j * block_range + iter_ans_j]
                        else:
                            ipt_reshape[iter_b_i * block + iter_ans_i][iter_b_j * block + iter_ans_j] = 0
                else:
                    for iter_ans_j in range(block):
                        ipt_reshape[iter_b_i * block + iter_ans_i][iter_b_j * block + iter_ans_j] = 0
    ans = np.zeros((N, N))
    for iter_b_i in range(blocked_size):
        for iter_b_j in range(blocked_size):
            tmp = []
            for x in range(block):
                tmp.append([])
                for y in range(block):
                    part_sum = 0
                    for u in range(block):
                        for v in range(block):
                            part_sum += ipt_reshape[iter_b_i * block + u][iter_b_j * block + v] * cos((2 * x + 1) * u * pi / 2 / block) * cos((2 * y + 1) * v * pi / 2 / block) * sqrt((1 if u == 0 else 2) / block) * sqrt((1 if v == 0 else 2) / block)
                    tmp[x].append(part_sum)
            for iter_ans_i in range(block):
                for iter_ans_j in range(block):
                    ans[iter_b_i * block + iter_ans_i][iter_b_j * block + iter_ans_j] = tmp[iter_ans_i][iter_ans_j]
    return ans
