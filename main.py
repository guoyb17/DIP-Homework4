import os, argparse
from math import log10
from PIL import Image as image
import numpy as np

from dct import my_dct_1d, my_idct_1d, my_dct_2d, my_idct_2d


def main(ipt_pic, mode):
    src = image.open(ipt_pic).convert("1")
    width, height = src.size
    assert(width == height)
    N = width
    bitmap = np.array(src).astype(np.int)
    if mode == 1:
        print("[INFO] Exp1: Are they equivalent in effect?")
        print("[INFO] 1        Compare DCT coefficients")
        print("[INFO] 1.1      1d DCT and IDCT")
        print("[INFO] 1.1.1    All DCT coefficients")
        mid = my_dct_1d(bitmap, N, N)
        fin = my_idct_1d(mid, N, N).astype(int)
        PSNR_1_1_1 = 0.0
        for x in range(N):
            for y in range(N):
                PSNR_1_1_1 += (bitmap[x][y] - fin[x][y]) ** 2
        PSNR_1_1_1 = 10 * log10(255 * 255 * N * N / PSNR_1_1_1)
        print("[INFO] PSNR =", PSNR_1_1_1)
        print("[INFO] 1.1.2    1/4 DCT coefficients")
        M = int(N / 2)
        mid = my_dct_1d(bitmap, N, M)
        fin = my_idct_1d(mid, M, N).astype(int)
        PSNR_1_1_2 = 0.0
        for x in range(N):
            for y in range(N):
                PSNR_1_1_2 += (bitmap[x][y] - fin[x][y]) ** 2
        PSNR_1_1_2 = 10 * log10(255 * 255 * N * N / PSNR_1_1_2)
        print("[INFO] PSNR =", PSNR_1_1_2)
        print("[INFO] 1.1.3    1/16 DCT coefficients")
        M = int(N / 4)
        mid = my_dct_1d(bitmap, N, M)
        fin = my_idct_1d(mid, M, N).astype(int)
        PSNR_1_1_3 = 0.0
        for x in range(N):
            for y in range(N):
                PSNR_1_1_3 += (bitmap[x][y] - fin[x][y]) ** 2
        PSNR_1_1_3 = 10 * log10(255 * 255 * N * N / PSNR_1_1_3)
        print("[INFO] PSNR =", PSNR_1_1_3)
        print("[INFO] 1.1.4    1/64 DCT coefficients")
        M = int(N / 8)
        mid = my_dct_1d(bitmap, N, M)
        fin = my_idct_1d(mid, M, N).astype(int)
        PSNR_1_1_4 = 0.0
        for x in range(N):
            for y in range(N):
                PSNR_1_1_4 += (bitmap[x][y] - fin[x][y]) ** 2
        PSNR_1_1_4 = 10 * log10(255 * 255 * N * N / PSNR_1_1_4)
        print("[INFO] PSNR =", PSNR_1_1_4)
        print("[INFO] 1.2      2d DCT and IDCT")
        print("[INFO] 1.2.1    All DCT coefficients")
        mid = my_dct_2d(bitmap, N, 8, 1)
        fin = my_idct_2d(mid, N, 8, 1).astype(int)
        PSNR_1_2_1 = 0.0
        for x in range(N):
            for y in range(N):
                PSNR_1_2_1 += (bitmap[x][y] - fin[x][y]) ** 2
        PSNR_1_2_1 = 10 * log10(255 * 255 * N * N / PSNR_1_2_1)
        print("[INFO] PSNR =", PSNR_1_2_1)
        print("[INFO] 1.2.2    1/4 DCT coefficients")
        mid = my_dct_2d(bitmap, N, 8, 2)
        fin = my_idct_2d(mid, N, 8, 2).astype(int)
        PSNR_1_2_2 = 0.0
        for x in range(N):
            for y in range(N):
                PSNR_1_2_2 += (bitmap[x][y] - fin[x][y]) ** 2
        PSNR_1_2_2 = 10 * log10(255 * 255 * N * N / PSNR_1_2_2)
        print("[INFO] PSNR =", PSNR_1_2_2)
        print("[INFO] 1.2.3    1/16 DCT coefficients")
        mid = my_dct_2d(bitmap, N, 8, 4)
        fin = my_idct_2d(mid, N, 8, 4).astype(int)
        PSNR_1_2_3 = 0.0
        for x in range(N):
            for y in range(N):
                PSNR_1_2_3 += (bitmap[x][y] - fin[x][y]) ** 2
        PSNR_1_2_3 = 10 * log10(255 * 255 * N * N / PSNR_1_2_3)
        print("[INFO] PSNR =", PSNR_1_2_3)
        print("[INFO] 1.2.4    1/64 DCT coefficients")
        mid = my_dct_2d(bitmap, N, 8, 8)
        fin = my_idct_2d(mid, N, 8, 8).astype(int)
        PSNR_1_2_4 = 0.0
        for x in range(N):
            for y in range(N):
                PSNR_1_2_4 += (bitmap[x][y] - fin[x][y]) ** 2
        PSNR_1_2_4 = 10 * log10(255 * 255 * N * N / PSNR_1_2_4)
        print("[INFO] PSNR =", PSNR_1_2_4)
        print("[INFO] 2        Compare size of blocks in 2D-DCT trial")
        print("[INFO] 2.1      size = 2")
        mid = my_dct_2d(bitmap, N, 2, 1)
        fin = my_idct_2d(mid, N, 2, 1).astype(int)
        PSNR_2_1 = 0.0
        for x in range(N):
            for y in range(N):
                PSNR_2_1 += (bitmap[x][y] - fin[x][y]) ** 2
        PSNR_2_1 = 10 * log10(255 * 255 * N * N / PSNR_2_1)
        print("[INFO] PSNR =", PSNR_2_1)
        print("[INFO] 2.2      size = 4")
        mid = my_dct_2d(bitmap, N, 4, 1)
        fin = my_idct_2d(mid, N, 4, 1).astype(int)
        PSNR_2_2 = 0.0
        for x in range(N):
            for y in range(N):
                PSNR_2_2 += (bitmap[x][y] - fin[x][y]) ** 2
        PSNR_2_2 = 10 * log10(255 * 255 * N * N / PSNR_2_2)
        print("[INFO] PSNR =", PSNR_2_2)
        print("[INFO] 2.3      size = 8 (default in 1.2)")
        mid = my_dct_2d(bitmap, N, 8, 1)
        fin = my_idct_2d(mid, N, 8, 1).astype(int)
        PSNR_2_3 = 0.0
        for x in range(N):
            for y in range(N):
                PSNR_2_3 += (bitmap[x][y] - fin[x][y]) ** 2
        PSNR_2_3 = 10 * log10(255 * 255 * N * N / PSNR_2_3)
        print("[INFO] PSNR =", PSNR_2_3)
        print("[INFO] 2.4      size = 16")
        mid = my_dct_2d(bitmap, N, 16, 1)
        fin = my_idct_2d(mid, N, 16, 1).astype(int)
        PSNR_2_4 = 0.0
        for x in range(N):
            for y in range(N):
                PSNR_2_4 += (bitmap[x][y] - fin[x][y]) ** 2
        PSNR_2_4 = 10 * log10(255 * 255 * N * N / PSNR_2_4)
        print("[INFO] PSNR =", PSNR_2_4)
        print("[INFO] 2.5      size = 32")
        mid = my_dct_2d(bitmap, N, 32, 1)
        fin = my_idct_2d(mid, N, 32, 1).astype(int)
        PSNR_2_5 = 0.0
        for x in range(N):
            for y in range(N):
                PSNR_2_5 += (bitmap[x][y] - fin[x][y]) ** 2
        PSNR_2_5 = 10 * log10(255 * 255 * N * N / PSNR_2_5)
        print("[INFO] PSNR =", PSNR_2_5)
    # elif mode == 2:
    #     # TODO: Exp2: Why quantization is so important?
    #     pass
    else:
        print("[ERROR] mode %d not implemented yet!" % mode)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="A script to finish homework 4 of DIP."
        )
    parser.add_argument("-i", "--input", type=str,
                        default=None,
                        help="input file",
                        required=True
                        )
    parser.add_argument("-m", "--mode", type=int,
                        help="mode: 1, 2; see README.md",
                        required=True
                        )

    args = parser.parse_args()
    main(args.input, args.mode)
