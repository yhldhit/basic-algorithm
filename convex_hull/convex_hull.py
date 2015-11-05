#-*- coding:utf-8 -*-
import turtle
import random 
import time
import copy
max_x=100
max_y=100
min_x=-100
min_y=-100
def randpoint(pointnum):
    point=[(random.randrange(min_x,max_x),random.randrange(min_y,max_y)) for i in range(pointnum)]
    return point

pointset=randpoint(100)
pointset=list(set(pointset))

p0=(0,10000)
for i in range(len(pointset)):
    if p0[1]>pointset[i][1]:
        p0=pointset[i]
#print 
#####################brute-force###############
#whether there is a point in triangle
def line(point1,point2):
    lineef=[0.0,0.0]
    detx,dety=float(point1[0]-point2[0]),float(point1[1]-point2[1])
    if (detx!=0):
        lineef[0]=dety/detx
        bias=point2[1]*point1[0]-point1[1]*point2[0]
        lineef[1]=bias/detx
    else:
        lineef[0]=10000 #x=a,a is a constant 
        lineef[1]=point1[0]
    #print (lineef,'\t',detx)
    return lineef

def part(lineef,a,b):
    if lineef[0]<10000:
        if (lineef[0]*a[0]+lineef[1]-a[1])*(lineef[0]*b[0]+lineef[1]-b[1])>0:
            return True
        else:
            return False
    elif (lineef[1]-a[0])*(lineef[1]-b[0])>0:
        return True
    else:
        return False

def isbelong(a,b,c,p):
    line1=line(a,b)
    line2=line(b,c)
    line3=line(a,c)
    if False==part(line1,c,p):
        return False
    elif False==part(line2,a,p):
        return False
    elif False==part(line3,b,p):
        return False
    return True

def brute_force(pointset):
    l=len(pointset)
    set1=pointset[:]
    #print set1
    for i1 in range(l):
        #print ('i1:',i1)
        for i2 in range(l):
            if i1==i2:
                pass
            else:
                #print ('i2:',i2)
                for i3 in range(l):
                    if i1==i3 or i2==i3:
                        pass
                    else:
                        #print ('i3',i3)
                        for i4 in range(l):
                            if i1==i4 or i2==i4 or i3==i4:
                                pass
                            else:
                                #print ('i4',i4)
                                a,b,c,p=pointset[i1],pointset[i2],pointset[i3],pointset[i4]
                                if isbelong(a,b,c,p):
                                    #print 'here'
                                    if p in set1:
                                        ind=set1.index(p)
                                        set1.pop(ind)
    print len(set1)
    return set1
##########################graham_scan##########
def compare(a,b):
   #print 'in compare p0:',p0

    if a[0]==p0[0] and a[1]==p0[1]:
        return -1

    if b[0]==p0[0] and b[1]==p0[1]:
        return 1

    if a[0]==p0[0]:
        if b[0]==p0[0]:
            if a[1]>b[1]:
                #print(1,a,b)
                return 1
            else:
                #print(2,a,b)
                return -1
        else:
            if b[0]>p0[0]:
                #print(3,a,b)
                return 1
            else:
                #print(4,a,b)
                return -1
    else:
        if p0[0]==b[0]:
            #print(3,a,b)
            if a[0]<p0[0]:
                return 1
            else:
                return -1
    
    detx,dety=(a[0]-p0[0])*1.0,(a[1]-p0[1])*1.0
    #cos1=(a[1]-p0[1])*1.0/(a[0]-p0[0])
    cos1=detx/(detx**2+dety**2)**0.5
    detx,dety=(b[0]-p0[0])*1.0,(b[1]-p0[1])*1.0
    cos2=detx/(detx**2+dety**2)**0.5
    if cos1<cos2:
        return 1
    elif cos1>cos2:
        return -1
    else:
        return 0

class Stack:
    head=-2
    headnext=-1
    lenth=0
    points=[]
    #construct function
    def __init__(self,point):
        self.points=point
        self.lenth=len(self.points)
    def head(self):
        return self.points[-1]
    def headnext(self):
        return self.points[-2]
    def isempty(self):
        if 0==self.lenth:
            return True
        else:
            return False

    def pop(self):
        if self.isempty():
            print "stack is empty"
        else:
            self.lenth-=1
            self.points.pop(self.lenth)
            return self.head()

    def push(self,point):
        self.points.append(point)
        self.lenth+=1
def isleftmove(x,y,z):
    a1,a2=((y[0]-x[0],y[1]-x[1]),(z[0]-y[0],z[1]-y[1]))
    if a1[0]*a2[1]-a1[1]*a2[0]<0:
        return False
    elif a1[0]*a2[1]-a1[1]*a2[0]==0 and a1[0]*a2[0]<0:
        return False
    return True

def graham_scan(pointset):
    sortedset=copy.deepcopy(pointset)
    sortedset.sort(compare)
    #if 20==len(sortedset):
    #    print sortedset
    s=Stack(sortedset[0:2])
    sortedset.pop(0)
    for point in sortedset:
        while False==isleftmove(s.headnext(),s.head(),point):
            s.pop()
            if 1>=s.lenth:
                #s.push(point)
                break
        s.push(point)

    return s.points

    #if head headnext piont notleftmove

def drawpoint(point,color):
    p=turtle.getturtle()
    p.hideturtle()
    p.speed(10)
    for i in point:
        p.up()
        p.color(color)
        p.goto(i)
        p.down()
        p.dot()
def drawline(lineset,color):
    p=turtle.getturtle()
    p.hideturtle()
    p.speed(10)
    p.up()
    p.goto(lineset[0])
    p.down()
    p.color(color)
    for point in lineset:
        p.goto(point)
    p.goto(lineset[0])

def compareX(point1,point2):
    if point1[0]>point2[0]:
        return 1
    elif point1[0]<point2[0]:
        return -1
    else:
        return 0
def divide(pointset):
    l=len(pointset)
    media=int(l/2)
    return (pointset[0:media],pointset[media:l])
    
#def conqure(pointset):
def con_merge(psetl,psetr,p):
    if len(p)>0:
        p0=p
        set1=copy.deepcopy(psetl)
        set2=copy.deepcopy(psetr)
        set1.sort(compare)
        set2.sort(compare)
        u=set2[0]
        v=set2[-1]
        ui=psetr.index(u)
        vi=psetr.index(v)
        if ui>vi:
            set22=copy.deepcopy(psetr[vi:ui]).reverse
            set22.sort(compare)
            set21=list(set(psetr)-set(set22))
            set21.sort(compare)
        else:
            set21=copy.deepcopy(psetr[ui:vi])
            set22=list(set(psetr)-set(set21))
            set22.sort(compare)
        settotal=set1+set21+set22
        settotal.sort(compare)
        settotal=list(set(settotal))
        result=graham_scan(settotal)
        return result
    else:
        eset=psetl+psetr
        eset=list(set(eset))
        eset.sort(compare)
        result=graham_scan(eset)
        return result
    

dset=copy.deepcopy(pointset)
dset.sort(compareX)
def divide_merge(pointset):
    if len(pointset)>3:
        ql,qr=divide(pointset)
        resultl=divide_merge(ql)
        resultr=divide_merge(qr)
        temp=(set(ql)-set(resultl))
        temp=list(temp)
        if len(temp)>0:
            q=temp[0]
        else:
            q=[]
        return con_merge(resultl,resultr,q)
    else:
        return pointset
time1=time.time()
convex1=brute_force(pointset)
time2=time.time()
convex2=graham_scan(pointset)
time3=time.time()
convex3=divide_merge(pointset)
time4=time.time()
convex1=list(set(convex1))
convex2=list(set(convex2))
convex3=list(set(convex3))
convex1.sort(compare)
convex2.sort(compare)
convex3.sort(compare)
brute_time=time2-time1
graham_time=time3-time2
divid_time=time4-time3
def show_result(convex,usetime,color,algorithm):
    drawpoint(pointset,'black')
    drawpoint(convex,color)
    drawline(convex,color)
    turtle.up()
    #turtle.pensize(400)
    turtle.goto(-60,min_y-30)
    turtle.down()
    turtle.write('%s,use time:%s'%(algorithm,str(usetime)))
    time.sleep(10)
    turtle.reset()
show_result(convex1,brute_time,'green','brute_force')
show_result(convex2,graham_time,'red','graham_scan')
show_result(convex3,divid_time,'blue','divide_conquer')


