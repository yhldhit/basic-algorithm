import random
import turtle
import time
dataset=[]
for i in range(100):
    x=random.randint(-100,100)
    y=random.randint(-100,100)
    #print([x,y])
    dataset.append([x,y])


def distance(x,y):
    #print x,y
    d=0.0
    d=(x[0]-y[0])**2+(x[1]-y[1])**2
    d=d**0.5
    return d

def initCentiods(dataset,k):
    center=random.sample(dataset,k)
    return center
        

def drawpoint(point,color):
    p=turtle.getturtle()
    p.hideturtle()
    turtle.delay(1)
    for i in point:
        p.pu()
        p.color(color)
        p.goto(i)
        p.pd()
        p.dot()

def kmeans(dataset,k):
    numsample=len(dataset)
    center=initCentiods(dataset,k)
    maxd=10000.0
    color=['yellow','red','green','orange','purple','blue','pink','cyln']     

    
    assment=[[-1,maxd] for i in range(numsample)]
    changed=True
    while True==changed:
        changed=False

        for i in range(numsample):
            dtemp=[maxd]*k
            for j in range(k):
                #print i,j
                dtemp[j]=distance(dataset[i],center[j])
                dmin=min(dtemp)
                if dmin<assment[i][1]:
                    assment[i][1]=dmin
                    assment[i][0]=j
                    changed=True
    #cluster piont
        for i in range(k):
            sample=[]
            for j in range(numsample):
                if assment[j][0]==i:
                    sample.append(dataset[j])
            sums=list(zip(*sample))
            x=sum(sums[0])/(len(sample)*1.0)
            y=sum(sums[1])/(len(sample)*1.0)
            center[i]=[x,y]
            drawpoint(sample,color[i])
    drawpoint(center,'black')
    time.sleep(10)
    print "great! it works"
    return center


k=4
center=kmeans(dataset,k)
