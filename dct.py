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

def my_dct_2d(f, N, block):
    '''
    2d DCT.
    f: input data (N * N).
    block: partition size (rec: 8).
    return: 2d array [
        [g0, g1, ..., g_(M - 1)],
        ......
    ]
    '''
    pass
