#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from argparse import ArgumentParser


def parse():
    parser = ArgumentParser(
        description='Find all prime numbers up to given limit.')
    parser.add_argument('limit', type=int, nargs=1,
                        help='Argumet, must be an integer number.')
    args = parser.parse_args()
    return args


def main():
    """
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes"""
    args = parse()
    limit_number = args.limit[0]
    all_numbers_list = [x for x in range(2, limit_number + 1)]
    for number in all_numbers_list:
        for n in range(number * number, limit_number + 1, number):
            if n in all_numbers_list:
                all_numbers_list.remove(n)
    print('All prime numbers up to {}: {}'.format(
        limit_number, all_numbers_list))


if __name__ == '__main__':
    main()
