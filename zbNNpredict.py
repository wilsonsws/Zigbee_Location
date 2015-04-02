#!/usr/bin/env python
from sklearn.neighbors import KNeighborsClassifier
import pickle

F_SIZE = 9
RealClass = []
PredictClass = []

FileName = raw_input('please input file name\n')
ModNumber = raw_input('please input Model number\n')

#predict
fin = open(r'C:\Users\wilsonsws\Desktop\test\processeddata\model%s.dat'%(str(ModNumber)))
neigh = pickle.load(fin)
fin.close

DataFile = open(r"C:\Users\wilsonsws\Desktop\test\processeddata\%s.txt"%(FileName),"r")
for line in DataFile:
    try:
        entry,ClassName = line.strip().split('\t')
    except:
        continue
    data = [0]*(F_SIZE+1)           # Data_predict
    item = entry.split(' ')
    #index,level = item[0].split(':')
    #data[int(index)] = int(level)*10
    for i in range(0,3):
        index,level = item[i].split(':')
        data[int(index)] = int(level)
    data[-1] = int(item[0].split(':')[0])*100
    cls = neigh.predict([data])  # what's this ?
    RealClass.append(int(ClassName))
    #RealClass.append(ClassName)
    PredictClass.append(cls[0])
print data
DataFile.close()

ResultFile = open(r"C:\Users\wilsonsws\Desktop\test\processeddata\Model%sresult%s.txt"%(str(ModNumber),FileName[-1]),"a")
for item in range(0,len(RealClass)):
    ResultFile.write(str(RealClass[item])+' '+str(PredictClass[item])+'\n')
ResultFile.close()
print 'finished'
     
