import math








def isDead(M,F):

    if(M > F):
        a = M
        b = M % F
    else:
        a = F
        b = F % M

    length = 0

    #if it's plain simple multiple, its dead
    #ntr = M > 1 and F > 1
    ntr = M > 1 and F > 1
    if(b == 0 and ntr):
        #print('dead',M,F)
        return True

    while(b >1 and (a % b > 0)):

        #print(M,F,'b',b,'a','ceil:',math.ceil((M-F)/F)*F)

        if(M > F):
            a = F
            M = M - (M//F)*F #math.ceil((M-F)/F)*F
            length = length + (M//F)
        else:
            a = M
            F = F - (F//M)*M
            length = length + (F//M)

        if(M > F):
            b = M % F
        else:
            b = F % M

        #print(M,F,'b',b,'a',a,'length:',length)

    if(b <= 1):
        #print('false',M,F,'b=',b,'a=',a,'length:',length)
        return False
    else:
        if( a % b == 0 ):
            #print(M,F)
            return True




def getFibIndex(fn):
    #print('Is Fib',fn)
    n = round(math.log(fn) *2.078087 + 1.672276)
    return n


def checkFib(M,F):
    #check if fibonachi
    if(isFib(M) and isFib(F)):
        f = getFibIndex(M)
        n = getFibIndex(F)
        if(abs(f-n) ==1):
            print('iS fib:',max(f,n))
            return max(f,n)
    return -1





def isFib(n):

    phi = 0.5 + 0.5 * math.sqrt(5.0)
    a = phi * n
    return n==0 or abs(round(a) - a) < 1.0 / n #n == 0 or abs(round(a) - a) < 1.0 / n


#fibonachi number of series starting from A,B >1
def isTrick(M,F):

    mx = max(M,F)
    mn = min(M,F)
    b = 34*min(M,F) - 21*max(M,F)
    a = (mx - 55*b)/34

    #if(b > 1):
    if(b > 0 and M>1 and F>1):
        if(a//1 == a and a > 1):#a is integer
            #print('found trick',a//1,b)
            #return True,a//1,b,9
            return True,round(a//1),b,9
    #else:
        #if(b == 1 and a==1):
            #is fibonachi
    return False,0,0,0




isFibb = False


def recon(M,F):

    length = 0
    impossible = False
    found = False
    global isFibb

    #i=0
    while( (not impossible) and (not found) ):

        #i = i+1
        #if(i > 10**10):
            #print('Performance issues',M,F)
            #print('before: M=',M,'F=',F,'res=',res,length)
         #   impossible == True

        if((M ==1 or F ==1) and (F>0 and M >0)  ):
            if(not M == F):
                if(M > F):
                    length = length + M - 1
                else:
                    length = length + F - 1
            else:
                length = length+1
            found = True
        else:

            #print(M,F)
            if ( (M < 1 or F < 1) ):#or isDead(M,F) or F==M
                impossible = True
            else:

                if(M > F):
                    res = M - (M//F)*F
                    length = length + M//F
                    M = res
                else:
                    res = F - (F//M)*M
                    length = length + F//M
                    F = res

                rs = isTrick(M,F)
                if( rs[0]):
                    M = rs[1]
                    F = rs[2]
                    length = length + rs[3]

                if(False and (M > 5 and F >5)):
                    n = checkFib(M,F)
                    if(not(n==-1)):
                        length =  length + n-2 #length
                        found = True


                #print(M,F,res)



    if(found):
        return length

    if(impossible):
        return -1





def solution(M,F):


    #if(not M.isdigit() or not F.isdigit()):
    #    return "impossible"

    M = int(M)
    F = int(F)

    if(M > 10**50 or F>10**50):
        return "impossible"

    if(M  < 1 or F < 1):
        return "impossible"

    if(M==1 and F ==1):
        return ("%.0f" % (0))

    if( (M//1) < M or (F//1) < F):
        return "impossible"


    minLen = 0

    minLen = recon(M,F)

    #print(("%.0f" % minLen))

    if(minLen == -1):
        return "impossible"
    #else: return ("%.0f" % (minLen))
    else: return ("%.0f" % (int(minLen)))
    #else: return ("%.0g" % (minLen))
