import sys

numbers = ['0','1','2','3','4','5','6','7','8','9']

def findPasswd(length,psswd):
    if length <= 0:
        print 'length <=0'
        return
    if length == 1:
        psswd[:] = numbers[:]
    else:
        findPasswd(length-1,psswd)
        for i in xrange(len(psswd)):
            last_c = psswd[i][-1]
            for x in numbers:
                if x > last_c:
                    psswd.append(psswd[i]+x)
        psswd[i] = psswd[i] + last_c

def foo(psswd):
    for x in numbers:
        psswd.append(x)

if __name__ == '__main__':
    length = int(sys.stdin.readline())
    psswd = []
    findPasswd(length,psswd)
    for x in psswd:
        print x
