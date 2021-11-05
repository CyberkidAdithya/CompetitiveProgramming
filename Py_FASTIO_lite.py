#!/usr/bin/env python

'''
    Name : cyberkid05 | Country : India
    Language : Python3
    email : thehappymentorkid@gmail.com
'''

#INTRODUCTION
# '''           Meet my Codechef Doggie
#      |\_/|                  
#      | @ @   Woof! 
#      |   <>              _  
#      |  _/\------____ ((| |))
#      |               `--' |   
#  ____|_       ___|   |___.' 
# /_/_____/____/_______|
# I am here to guard this code, woof!
# '''

#--MODULES BEGINS--
import io, os, sys, time
import math, functools, collections
import bisect, heapq, numpy
from contextlib import contextmanager
#--MODULES ENDS--

#--SHORTHANDS BEGINS--
# input = raw_input
# input = sys.stdin.readline
# alphabets = "abcdefghijklmnopqrstuvwxyz"
# from statistics import mode
# from functools import reduce
# from bisect import bisect
# from collections import defaultdict
# from collections import Counter
# hp = defaultdict(lambda: 0)
# hp = collections.defaultdict(int, collections.Counter(arr))
# input = lambda: sys.stdin.readline().strip()
# imap = lambda: map(int,input().split())
# ilist = lambda: list(map(int, input().split()))
# sys.stdout.write(str(ans) + "\n")
# for line in sys.stdin
#--SHORTHANDS ENDS--


#----    CODE BEGINS    ----->
#--GLOBAL VALUES BEGINS--
class ConstantMod():
    def __init__(self, n = 10 ** 9 + 7):
        self.maxx = n
        self.minn = -(n)
@contextmanager
def simple_context_manager(obj):
    try:
        obj.maxx = INF
        obj.minn = -(INF)
        yield
    finally:
        obj.maxx = 10 ** 9 + 7
        obj.minn = -(10 ** 9 + 7)
StartTime = time.time()
# print("\nExecution Time: ",time.time()-StartTime)
input = lambda : sys.stdin.readline()
alp = "abcdefghijklmnopqrstuvwxyz"
modd = ConstantMod(10 ** 9 + 7)
INF = 10 ** 15     # Change as per need
#--GLOBAL VALUES ENDS--

#--FUNCTIONS BEGINS--
def solve():
    # YOUR CODE HERE
    # global modd
    # print(modd.maxx, modd.minn)
    print("Hello World")
    # pass

def main():
    tcs = 1
    # tcs = int(input())
    for tc in range(tcs):
        # with simple_context_manager(modd):    # temporary environment
        solve()

    # OUTPUT - GOOGLE KICKSTART
    # if solve():
    #     print('Case #{}: {}'.format(tc, "YES"))
    # else:
    #     print('Case #{}: {}'.format(tc, "NO"))
#--FUNCTIONS ENDS--

# # REGION FASTIO
# BUFSIZE = 8192

# class FastIO(IOBase):
#     newlines = 0
#     def __init__(self, file):
#         self._fd = file.fileno()
#         self.buffer = BytesIO()
#         self.writable = "x" in file.mode or "r" not in file.mode
#         self.write = self.buffer.write if self.writable else None
#     def read(self):
#         while True:
#             b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
#             if not b:
#                 break
#             ptr = self.buffer.tell()
#             self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
#         self.newlines = 0
#         return self.buffer.read()
#     def readline(self):
#         while self.newlines == 0:
#             b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
#             self.newlines = b.count(b"\n") + (not b)
#             ptr = self.buffer.tell()
#             self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
#         self.newlines -= 1
#         return self.buffer.readline()
#     def flush(self):
#         if self.writable:
#             os.write(self._fd, self.buffer.getvalue())
#             self.buffer.truncate(0), self.buffer.seek(0)

# class IOWrapper(IOBase):
#     def __init__(self, file):
#         self.buffer = FastIO(file)
#         self.flush = self.buffer.flush
#         self.writable = self.buffer.writable
#         self.write = lambda s: self.buffer.write(s.encode("ascii"))
#         self.read = lambda: self.buffer.read().decode("ascii")
#         self.readline = lambda: self.buffer.readline().decode("ascii")

# if sys.version_info[0] < 3:
#     sys.stdin, sys.stdout = FastIO(sys.stdin), FastIO(sys.stdout)
# else:
#     sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)

# input = lambda: sys.stdin.readline().rstrip("\r\n")
# # END REGION

if __name__ == "__main__":
    main()
#<-----    CODE ENDS    ----


'''

#----INPUT----

# INPUT DATA HERE

#----OUTPUT----

# OUTPUT DATA HERE

'''

''' SHORTER CODE | NOTES - comment this line to run the below code

# pass

# '''