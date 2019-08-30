#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from argparse import ArgumentParser


def parse():
    parser = ArgumentParser(
        description='Check number, prime or composite.')
    parser.add_argument('number', type=int, nargs=1,
                        help='Argumet, must be an integer number.')
    args = parser.parse_args()
    return args


def main():
    args = parse()
    number = args.number[0]
    half_exp_number = int(number ** 0.5)
    for x in range(2, half_exp_number + 1):
        if not number % x:
            print('{} is composite.'.format(number))
            return
    print('{} is prime.'.format(number))


if __name__ == '__main__':
    main()
