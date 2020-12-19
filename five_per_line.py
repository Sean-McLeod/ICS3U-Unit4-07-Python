#!/usr/bin/env python3

# Created by Sean McLeod
# Created on December 2020
# This program can print from 1000 to 2000 with five integers per line

def main():
    # this function can print from 1000 to 2000, five integers per line

    # process & output
    for counter in range(1000, 2001):
        if counter % 5 == 0:
            print("\n", end="")
            print(counter, end=" ")
        else:
            print(counter, end=" ")


if __name__ == "__main__":
    main()
