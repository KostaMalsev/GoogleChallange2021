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
    if(isFib(M) and isFib(F) and F >1 and M >1):
        f = getFibIndex(M)
        n = getFibIndex(F)
        #print('fibs:',f,n,'MF',M,F)
        if(abs(f-n) ==1):
            #print('iS fib:',max(f,n))
            return max(f,n)
    return -1





def isFib(n):

    phi = 0.5 + 0.5 * math.sqrt(5.0)
    a = phi * n
    return n==0 or abs(round(a) - a) < 1.0 / n #n == 0 or abs(round(a) - a) < 1.0 / n




def recon(M,F):

    length = 0
    impossible = False
    found = False

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
                
                    #if(M > 1 and F >1):
                     #   n = checkFib(M,F)
                     #   if(not(n==-1)):
                     #       length =  length + n-3 #length
                     #       found = True
                        

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
    else: return ("%.0f" % (int(minLen//1)))
    #else: return ("%.0g" % (minLen))
