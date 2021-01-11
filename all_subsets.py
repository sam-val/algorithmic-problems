from itertools import chain, combinations as com
from copy import deepcopy
import sys


def easy_way(s):
    rs_list = [com(s,n) for n in range(0, len(s)+1)]
    return chain.from_iterable(rs_list)

def manual_way(s):
    l = list(s)
    yield {}
    for i in range(len(l)):
        items_so_far = []
        for j in range(i, len(l)):
            pairs = [l[i],l[j]]
            if l[i] != l[j]:
                ## rs.append(deepcopy(pairs))
                yield deepcopy(pairs)
            items_so_far.append(l[j])
            if items_so_far != pairs:
                ## rs.append(deepcopy(items_so_far))
                yield deepcopy(items_so_far)


s =  []

for arg in range(1, len(sys.argv)):
    s.append(sys.argv[arg])

s = set(s)

if len(s) > 0:
    for i in easy_way(s):
        print(i)


