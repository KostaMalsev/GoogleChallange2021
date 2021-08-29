import math








def isDead(M,F):

    a = max(M,F)
    b = max(M,F) % min(M,F)
    length = 0

    #if it's plain simple multiple, its dead
    if(b == 0 and min(M,F)>1):
        #print('dead',M,F)
        return True
    
    while(b >1 and (a % b > 0)):

        #print(M,F,'b',b,'a','ceil:',math.ceil((M-F)/F)*F)

        a = min(M,F)
        
        if(M > F):
            M = M - math.ceil((M-F)/F)*F
            length = length + math.ceil((M-F)/F)*F
        else:
            F = F - math.ceil((F-M)/M)*M
            length = length + math.ceil((F-M)/M)*M
                
        b = max(M,F) % min(M,F)
        

        #print(M,F,'b',b,'a',a,'length:',length)
        

    if(b<=1):
        #print('false',M,F,'b=',b,'a=',a,'length:',length)
        return False
    else:
        #print(M,F)
        return True
        
    




def recon(M,F):

    length = 0
    impossible = False
    found = False

    
    i=0
    while( (not impossible) and (not found) ):
        
        i = i+1
        #if(i > 10**10):
            #print('Performance issues',M,F)
            #print('before: M=',M,'F=',F,'res=',res,length)
         #   impossible == True
        
        if(M ==1 or F ==1):
            if(not M == F):
                length = length + max(M,F)-1 
            found = True
        else:
            #print(M,F)       
            if (M < 1 or F < 1 ):#or isDead(M,F) or F==M
                impossible = True
            else:                

                if(M>F):
                    res = M - (M//F)*F
                    length = length + M//F
                    M = res                    
                else:
                    res = F - (F//M)*M
                    length = length + F//M
                    F = res

                #print(M,F,res)



    if(found):
        return length

    if(impossible):
        return -1

    



def solution(M,F):


    if(not M.isdigit() or not F.isdigit()):
        return "impossible"

    M = int(M)
    F = int(F)

    minLen = 0

    minLen = recon(M,F)

    #print(("%.0f" % minLen))

    if(minLen == -1):
        return "impossible"
    else: return ("%.0f" % (minLen))
    #else: return ("%.0g" % (minLen))

