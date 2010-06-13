import sys
import time
import psyco
psyco.full()
def dbg(a): sys.stderr.write(str(a) + "\n")
def readint(): return int(raw_input())
def readfloat(): return float(raw_input())
def readarray(f): return map(f,raw_input().split())
def alloc(size, default = 0): return [default] * size

t00 = time.clock()

def solve():
    return 0

for t in xrange(readint()):
    t0 = time.clock()
    dbg("Test #%d:" % (t+1))
    ans = solve()
    print "Case #%d: %d" % (t+1,ans)
    dbg("time %.2f sec" % (time.clock() - t0))

dbg("total time %.2f sec" % (time.clock() - t00))
