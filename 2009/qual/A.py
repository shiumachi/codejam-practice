#!/usr/bin/py

class AClass:
    def fileopen(self):
        self.dict = []
        L,D,N = raw_input().split(' ')
        L = int(L)
        D = int(D)
        N = int(N)
        for i in range(D):
            self.dict.append(raw_input())
        for i in range(N):
            count = self.process(raw_input())
            print "Case #" + repr(i+1) + ": " + repr(count)

    def process(self,line):
        chmap = [[0 for i in range(26)] for j in range(15)]
        l = len(line)
        stat = 0
        pos = 0
        for i in range(l):
            c = line[i]
            if(c == '('):
                stat = 1
            elif(c == ')'):
                stat = 0
                pos += 1
            else:
                if(stat == 1):
                    chmap[pos][ord(c)-ord('a')] = 1
                else:
                    chmap[pos][ord(c)-ord('a')] = 1
                    pos += 1
        count = 0
        for i in self.dict:
            flg = 1
            l = len(i)
            for j in range(l):
                if(chmap[j][ord(i[j])-ord('a')] == 0):
                    flg = 0
                    break
            if(flg == 1):
                count += 1
        return count
    
a = AClass()
a.fileopen()
