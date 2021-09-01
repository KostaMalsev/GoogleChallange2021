import math



def recon(M,F):

    length = 0
    impossible = False
    found = False

    while( (not impossible) and (not found) ):

        if((M ==1 or F ==1) ):
        
            if(not M == F):
                if(M > F):
                    length = length + M - 1
                else:
                    length = length + F - 1
            else:
                length = length+1
            found = True

        else:

            if ( (M < 1 or F < 1) ):
                impossible = True
                break
            else:

                if(M > F):
                    res = M - ((M-F)//F+1)*F

                    if(M > 30):
                        M = res
                        length = length + ((M-F+1)//F)
                    else:
                        M = M - F
                        length = length+1

                else:
                    res = F - ((F-M+1)//M)*M
                    
                    if(F > 30):
                        F = res
                        length = length + ((F-M+1)//M)
                    else:
                        F = F - M
                        length = length+1

    if(found):
        return length

    if(impossible):
        return -1



def solution(M,F):


    M = int(M)
    F = int(F)

    if(M==1 and F ==1):
        return print(str(0))


    minLen = 0

    minLen = recon(M,F)

    if(minLen == -1):
        return "impossible"

    else: return (str(minLen))


#print(solution('99194853094755497','61305790721611591'))#fibonachi 83 and 84 elements order of 38
#print(solution('99194853094755497','6428163631445425602')) #with adding 3 times of the action

#print(solution('3928413764606871165730','6356306993006846248183')) #Fibonachi adding one itiration on F

#print(solution('139583862445','225851433717')) #wFibonachi adding one itiration on F
#print(solution(str(55835073295300465536628086585786672357234389  ),str(55835073295300465536628086585786672357234389+34507973060837282187130139035400899082304280  ))) #with adding 3 times of the action
#print(solution(str(5),str(5+3))) #with adding 3 times of the action

#print(solution(str(34*2+55*7),str(21*2+34*7)))
#print(solution(str(13),str(13+1*8))) #with adding 3 times of the action




if(True):

    print(solution('2','2'))
    print(solution('4','2'))
    print(solution('1','1'))
    print(solution('2','1'))
    print(solution('4','7'))
    print(solution('16','9'))
    print(solution('31','4'))
    print(solution('11','5'))
    print(solution('3','13'))
    print(solution('1','2'))

    print(solution('3','5')) #is true
    print(solution('10','13')) #is true


    #print(solution('1000000000000000000000000000000000000000000000000','25'))

    #print(solution('6','4'))
    print(solution(str(10**50-1),str(10**50-2)))
    #print(solution('bla','7'))
    #print(solution('10000000000000000000000000000000000000000000000011','100000000000000000000000000000000000000000000000008'))


    #i=10**50
    i= 10**50#10**48
    lastRes=-1
    while(i<10**50):
        ii=1
        while (ii<1000):
            if("impossible" == (solution(str(i),str(ii)))):
                M = i
                F = ii
                if(not isDead(M,F)):
                    print('intrs impossible:',i,ii)
            else:
                a=1
                #print((solution(str(i),str(ii))),i,ii)

            ii = ii + 1
        i = i + 1

