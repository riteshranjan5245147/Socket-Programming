import matplotlib.pyplot as plt
import math
file = open('iris dataset.txt','r').read()
newdata=[]
lstx = []
lsty = []
irisdata = file.split()
for i in irisdata:
    irislist = i.split(',')
    if irislist[4] == 'Iris-setosa':
        irislist[4]='0'
    if irislist[4] == 'Iris-versicolor':
        irislist[4]='1'
    if irislist[4] == 'Iris-virginica':
        irislist[4]='2'
    newdata.append(irislist)

training = newdata[:20] + newdata[31:60] + newdata[71:140]
testing = newdata[21:30] + newdata[61:70] + newdata[141:149]
pc=0
per=0
D = []
for i in testing:
    sl=float(i[0])
    sw=float(i[1])
    pl=float(i[2])
    pw=float(i[3])
    for j in training:
        a = (float(j[0])-sl)**2
        b = (float(j[1])-sw)**2
        c = (float(j[2])-pl)**2
        d = (float(j[3])-pw)**2
        s = str(math.sqrt(a+b+c+d))
        D.append(j+[s])
    D=sorted(D,key = lambda l:l[5])
    k=10
    c1=0
    c2=0
    c3=0
    for m in range(0,k):
        if D[m][4]=='0':
            c1+=1
        elif D[m][4]=='1':
            c2+=1
        else:
            c3+=1
    if(c1>c2 and c1>c3):
        pc=0
    if(c2>c1 and c2>c3):
        pc=1
    if(c3>c1 and c3>c2):
        pc=2
    if i[4]==str(pc):
        per+=1
        lstx.append(i)
        lsty.append((per*100.0)/len(testing))
plt.plot(lstx,lsty)
plt.show()

acc=0
acc=per/float(len(testing))
acc=acc*100
print(acc)
