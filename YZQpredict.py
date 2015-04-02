#!/usr/bin/env python
from sklearn.neighbors import KNeighborsClassifier
import pickle

F_SIZE = 4
RealClass = []
PredictClass = []

FileName = raw_input('please input file name\n')
ModNumber = raw_input('please input Model number\n')

#predict
fin = open(r'C:\Users\wilsonsws\Desktop\test\processeddata\YZQmodel%s.dat'%(str(ModNumber)))
neigh = pickle.load(fin)
fin.close

DataFile = open(r"C:\Users\wilsonsws\Desktop\test\processeddata\%s.txt"%(FileName),"r")
tempData = [0]*F_SIZE

for line in DataFile:
    tempData = [0]*F_SIZE
    entry = line.strip()        
    item = entry.split(' ')
    for i in range(0,4):
        tempData[i] = int(item[i],16)
    ClassName = item[-1]

    cls = neigh.predict([tempData])  # what's this ?
    RealClass.append(ClassName)
    #RealClass.append(ClassName)
    PredictClass.append(cls[0])
print tempData
print cls[0]
DataFile.close()

ResultFile = open(r"C:\Users\wilsonsws\Desktop\test\processeddata\Model%sresult%s%s.txt"%(str(ModNumber),FileName[-3],FileName[-2]),"a")
for item in range(0,len(RealClass)):
    ResultFile.write(str(RealClass[item])+' '+str(PredictClass[item])+'\n')
ResultFile.close()
print 'finished'
     
