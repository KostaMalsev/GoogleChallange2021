import math


minLen = -1
Mtarget=-1
Ftarget=-1


def getRoute(M,F,length):

    global minLen
    global Mtarget
    global Ftarget

    if(M > Mtarget or F > Ftarget):
        return -1
    else:
        if(M == Mtarget and F == Ftarget):
            return length
        else:
            #initiate bomb replication:
            res1 = actM(M,F)
           	 print(res1) 

           

            #follow the paths, see where it gets us:
            len1 = getRoute(res1[0],res1[1],length+1)
            
            if(len1 == -1):
	            res2 = actF(M,F)
            	len2 = getRoute(res2[0],res2[1],length+1)
            else:
            	getMin(len1,len2)
            	return minLen
            	
            len2 = getRoute(res2[0],res2[1],length+1)


            #print(len1,len2)
            #if len2 > -1 and len1 > -1 : print('two choices:',len2,len1,res1,res2)

            #if len2 == -1 and len1 == -1 : return -1
            if(len2 == -1 and len1 == -1):
                #print('dead end',minLen)
                return minLen
                #len2 = getRoute(res2[0],res2[1],length+1)
                #len1 = getRoute(res1[0],res1[1],length+1)

            getMin(len1,len2)

            return minLen




def actM(M,F):
    return M,F+M

def actF(M,F):
    return M+F,F


def getMin(len1,len2):

    global minLen

    if(minLen > -1):

        if len1 == -1 and len2 > -1 and len2 < minLen : minLen = len2
        if len2 == -1 and len1 > -1 and len1 < minLen : minLen = len1
        if len2 > -1 and len1 > -1 and min(len1,len2) < minLen : minLen = math.min(len1,len2)

    else:

        if len1 == -1 and len2 > -1 : minLen = len2
        if len2 == -1 and len1 > -1 : minLen = len1
        if len2 > -1 and len1 > -1 : minLen = min(len1,len2)





def solution(M,F):

    global Mtarget
    global Ftarget
    global minLen

    minLen = -1

    Mtarget = int(M)
    Ftarget = int(F)


    if(Mtarget == 1 and Ftarget == 1):
        return str(0)

    if(Mtarget == 0 or Ftarget == 0):
        return str(0)


    shortPath = getRoute(1,1,0)

    #print(minLen)

    if(minLen == -1):
        return 'impossible'
    else: return str(minLen)

