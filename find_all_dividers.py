#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from argparse import ArgumentParser


def parse():
    parser = ArgumentParser(
        description='Finding all dividers.')
    parser.add_argument('number', type=int, nargs=1,
                        help='Argumet, must be an integer number.')
    args = parser.parse_args()
    return args


def main():
    args = parse()
    number = args.number[0]
    dividers = []
    half_number = number // 2
    for x in range(2, half_number + 1):
        if not number % x:
            dividers.append(x)
    print('For {} dividers are {}'.format(number, dividers))


if __name__ == '__main__':
    main()
