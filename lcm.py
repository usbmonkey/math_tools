#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from argparse import ArgumentParser


def parse():
    parser = ArgumentParser(
        description='Computing the least common multiple for 2 numbers.')
    parser.add_argument('first', type=int, nargs=1,
                        help='First argumet, must be an integer number.')
    parser.add_argument('second', type=int, nargs=1,
                        help='Second argumet, must be an integer number.')
    args = parser.parse_args()
    return args


def lcm(num1, num2):
    """ Computing the least common multiple
    https://en.wikipedia.org/wiki/Least_common_multiple"""
    lcm_result = (num1 * num2) / gcd(num1, num2)
    return int(lcm_result)


def gcd(num1, num2):
    """Computing the greatest common divisor
    https://en.wikipedia.org/wiki/Greatest_common_divisor
    https://en.wikipedia.org/wiki/Euclidean_algorithm """
    while num2 > 0:
        num1, num2 = num2, num1 % num2
    return num1


def main():
    args = parse()
    number1 = args.first[0]
    number2 = args.second[0]
    lcm_result = lcm(number1, number2)
    print('LCM for {} & {} is {}'.format(number1, number2, lcm_result))


if __name__ == '__main__':
    main()
