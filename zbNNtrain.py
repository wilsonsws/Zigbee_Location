#!/usr/bin/env python
from sklearn.neighbors import KNeighborsClassifier
import pickle

F_SIZE = 9
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
for line in DataFile:
    try:
        entry,ClassName = line.strip().split('\t')
    except:
        continue
    x = [0]*(F_SIZE+1)
    item = entry.split(' ')
    #index,level = item[0].split(':')
    #x[int(index)] = int(level)*10
    for i in range(0,3):
        index,level = item[i].split(':')
        x[int(index)] = int(level)
    x[-1] = int(item[0].split(':')[0])*100
    RawData.append(x)
    Class.append(int(ClassName))
print x
DataFile.close()

#train model
neigh = KNeighborsClassifier(n_neighbors = 300,weights = 'distance')
neigh.fit(RawData,Class)

#save model
fout = open(r"C:\Users\wilsonsws\Desktop\test\processeddata\model%s.dat"%(str(ModelNumber)),"w")
pickle.dump(neigh,fout)
fout.close()

print 'finished'
