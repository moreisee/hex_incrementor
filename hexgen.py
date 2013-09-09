#!/usr/bin/env python


"""Hex number incrementor"""

import csv

HEX_PREFACE = '64BABD'


def increment_hex(hex_num, inc_num):

    hex_final_list = []

    try:
        hex_num = hex_num.replace(':', '')
    except:
        pass

    for n in range(int(inc_num)):
        hex_num = int(hex_num, 16) + 1
        hex_num = hex(hex_num)[2:].upper()
        #hex_final = ':'.join(a+b for a,b in zip(hex_num[::2], hex_num[1::2]))

        hex_final = HEX_PREFACE + hex_num

        hex_final_list.append(hex_final)

    write_csv(hex_final_list)


def write_csv(hex_final_list):
    with open('hex_output.csv', 'wb') as fp:
        csv_writer = csv.writer(fp, dialect = 'excel', delimiter = '\n')
        csv_writer.writerow(hex_final_list)


if __name__ == '__main__':
    hex_start = raw_input("Please enter the hex starting point: ")
    inc_num = raw_input("Please enter number of hex to create: ")
    increment_hex(hex_start, inc_num)
