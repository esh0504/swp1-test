import sys

a=int(input())

for i in range (a):
    b,c=map(int,sys.stdin.readline().split())
    d=b+c
    print(d)

