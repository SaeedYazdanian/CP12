# def numOfFactors(n):
#     cnt = 0
#     for i in range(1,n+1):
#         if n % i == 0:
#             cnt += 1
#     return cnt
#
# def isPrime(n):
#     cnt = 0
#     for i in range(2,n):
#         if n % i == 0:
#             return 1
#     return cnt
#
# for i in range(1000000,100000000000000000):
#     if isPrime(i) == 0:
#         print(i)

a = [int(x) for x in input().split()]

print(a)