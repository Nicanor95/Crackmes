import sys
from functools import reduce

username = sys.argv[1]

# we sum the char value of each + 3, you can use:
#
# sum = 0
# for i,x in enumerate(username):
#     sum = sum + ord(x) + i + 4
#
# or this magic one liner:
sum1 = reduce(lambda x,y: x + y, map(lambda x: 4 + x[0] + ord(x[1]), enumerate(username)))

sum2 = ((len(username) >> 1)*3) + len(username)

print("{}-{}".format(sum2, sum1))