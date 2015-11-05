import turtle 
import random 
import time
import string 

#s1="abcdgkadmasdfaskdjfhkjdsfgkdsf"
#s2="absgflkdjlfkgjlkjdflg"
#s3="absdfaakd"
letset=string.letters
strlen=1000
setlen=20
#get string set 
def randomstr(n):
    return [letset[random.randint(0,30)] for i in range(n)]

strsetA=[''.join(randomstr(strlen)) for i in range(setlen)]
strsetB=[''.join(randomstr(strlen)) for i in range(setlen)]

try:
    f=open('seq.txt','a')
    for i in range(setlen):
        f.write('A'+str(i+1)+':'+strsetA[i]+'\n'+'B'+str(i+1)+':'+strsetB[i]+'\n')
except:
    print('write file err')
f.close()
def lcs_dy(s1,s2):
    m=len(s1)
    n=len(s2)
    cost=[[0]*(n+1) for i in range(m+1)]
    b=[[0]*(n+1) for i in range (m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1]==s2[j-1]:
                #print(isinstance(cost[0][0],bool))
                cost[i][j]=cost[i-1][j-1]+1
                b[i][j]=2
            elif cost[i][j-1]>=cost[i-1][j]:
                cost[i][j]=cost[i][j-1]
                b[i][j]=1
            else:
                cost[i][j]=cost[i-1][j]
                b[i][j]=3
    def print_lcs(b,s1,s2):
        result=['0']*cost[m][n]
        l=-1
        i=len(b)-1
        j=len(b[0])-1
        while (i*j)>0:
            if b[i][j]==1:
               j=j-1
            elif b[i][j]==3:
                i=i-1
            else:
                result[l]=s1[i-1]
                l-=1
                i-=1
                j-=1
        return (result)
    return print_lcs(b,s1,s2)

#lcs_dy(s1,s2)

def lcs_it(s1,s2):
    print 
    m=len(s1)
    n=len(s2)
    if (m==0 or n==0):
        #print "m equal 0"
        return []
    elif s1[-1]==s2[-1]:
       # print type(lcs_it(s1[0:m-1],s2[0:n-1]).append(s1[-1])),type(s1[-1])
        subr=lcs_it(s1[0:m-1],s2[0:n-1])
        if isinstance(subr+[s1[-1]],list):
            return subr+[s1[-1]]
        else:
            print s1[-1],s2[-1]
            return [s1[-1]]
    else:
        lcs1=lcs_it(s1[0:m-1],s2)
        lcs2=lcs_it(s1,s2[0:n-1])
        #print type(lcs1),"type2",s1,s2
        #print type(lcs2),"type3",m,n,s1,s2
        if isinstance(lcs1,list):
            l1=len(lcs1)
        else:
            l1=0
        
        if isinstance(lcs2,list):
            l2=len(lcs2)
        else:
            l2=0
        if l1>l2:
            return lcs1
        else:
            return lcs2
def lcs3(s1,s2,s3):
    r1=lcs_dy(s1,s2)
    r2=''
    for  i in r1:
        r2+=i
    result=lcs_dy(r2,s3)
    return result

start_time=time.time()
lcsset=[lcs_dy(strsetA[i],strsetB[i]) for i in range(len(strsetA))]
end_time=time.time()
#lcs=lcs_it(s1,s2)
#print(lcs)
#it_lcsset=[lcs_it(strsetA[i],strsetB[i]) for i in range(len(strsetA))]
#endit_time=time.time()
dy_usetime=end_time-start_time
#it_usetime=endit_time-start_time
#print 'use time:'+str(dy_usetime)+'S'

#print(lcsset)

try:
    f=open('seq.txt','a')
    f.write('\t'*3+'&'*10+'dynamic result'+'&'*10+'use time'+str(dy_usetime)+'s\n')
#    f.write('\t'*4+'&'*10+'it result'+'&'*10+'use time'+str(it_usetime)+'\ts\n')
    for i in range(setlen):
        f.write('A'+str(i+1)+':'+strsetA[i]+'\n'+'B'+str(i+1)+':'+strsetB[i]+'\n'+'LCS'+str(i+1)+':'+''.join(lcsset[i])+'\n')
       # f.write(''.join(it_lcsset[i])+'\n')
except:
    print('write file err2')

f.close()
#lcs=lcs_dy(s1,s2)
#lcs2=lcs_it(s1,s2)
#lcs=lcs3(s1,s2,s3)
#print lcs2
        
