import os, argparse, math
from PIL import Image as image
import numpy as np


def main(ipt_pic, mode, param):
    pass

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
    parser.add_argument("-p", "--param", type=str,
                        help="addition param; see README.md",
                        required=True
                        )

    args = parser.parse_args()
    main(args.input, args.mode, args.param)
