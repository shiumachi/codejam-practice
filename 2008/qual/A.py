def readint(): return int(raw_input())

N = readint()

for n in xrange(N):
    S = readint()
    slist = [raw_input() for _ in xrange(S)]
    Q = readint()
    cur_s = slist[:]
    count = 0
    for q in xrange(Q):
        query = raw_input()
        try:
            cur_s.remove(query)
        except ValueError:
            pass
        if len(cur_s) == 0:
            cur_s = slist[:]
            cur_s.remove(query)
            count += 1
    print "Case #%d: %d" % (n+1, count)
            
        
