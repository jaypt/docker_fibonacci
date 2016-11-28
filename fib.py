#!/usr/bin/python2.7

import argparse

def fib(max):
    a, b, idx = 0, 1, 0
    while idx < max:
       yield a
       a, b, idx = b, a+b, idx+1

def main(max):
    print 'printing ', max, 'fib numbers'
    for val in fib(max):
        print val

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("-m", "--max", help="enter max number of fib numbers", default=10, type=int)
  args = parser.parse_args()
  main(args.max)
