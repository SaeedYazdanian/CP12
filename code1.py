import sys
sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

for t in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    print(a.count(max(a)))

