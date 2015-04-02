#!/usr/bin/env python
from sklearn.neighbors import KNeighborsClassifier
import pickle

F_SIZE = 4
TRAIN_FILE = raw_input('please input file name\n')
ModelNumber = raw_input('please input Model number\n')

#data init
#for line in open('param.txt'):
#   attribute,value = line.strip().split('\t')
#   if attribute == 'feature_size':
#       F_SIZE = int(value)

#prepare to train
RawData = []
Class = []
DataFile = open(r"C:\Users\wilsonsws\Desktop\test\processeddata\%s.txt"%(TRAIN_FILE),"r")
tempData = [0]*F_SIZE
        
for line in DataFile:
    tempData = [0]*F_SIZE
    entry = line.strip()
    item = entry.split(' ')
    for i in range(0,4):
        tempData[i] = int(item[i],16)
    ClassName = item[-1]
    RawData.append(tempData)
    Class.append(int(ClassName))

print tempData
print RawData[1]
print Class[1]
print RawData[250]
print Class[250]
print RawData[600]
print Class[600]
DataFile.close()

#train model
neigh = KNeighborsClassifier(n_neighbors = 200,weights = 'uniform')
neigh.fit(RawData,Class)

#save model
fout = open(r"C:\Users\wilsonsws\Desktop\test\processeddata\YZQmodel%s.dat"%(str(ModelNumber)),"w")
pickle.dump(neigh,fout)
fout.close()

print 'finished'
