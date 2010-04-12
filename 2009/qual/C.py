
N = int(raw_input())

wel = 'welcome to code jam'
wellen = len(wel)
count = 0
cache = {}

def findtext(text,start,end,pos):
    global count,cache
    if (start,pos) in cache: return cache[(start,pos)]
    c = 0
    for i in xrange(start,end):
        if wel[pos] == text[i]:
            if pos+1 == wellen:
                c += 1
            else:
                c += findtext(text,i,end,pos+1)
    cache[(start,pos)] = c % 10000
    return c % 10000
    

for n in xrange(N):
    text = raw_input()
    count = 0
    cache = {}
    count = findtext(text,0,len(text),0)
    print "Case #%d: %04d" % ((n+1),int(count))
    
    
