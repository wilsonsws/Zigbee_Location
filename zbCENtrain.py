#!/usr/bin/env python
from sklearn.neighbors.nearest_centroid import NearestCentroid
import pickle

F_SIZE = 7
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
    for i in range(0,3):
        index,level = item[i].split(':')
        x[int(index)] = float(level)
    x[-1] = int(item[0].split(':')[0])*1000
    RawData.append(x)
    Class.append(int(ClassName))
DataFile.close()

#train model
neigh = NearestCentroid()
neigh.fit(RawData,Class)

#save model
fout = open(r"C:\Users\wilsonsws\Desktop\test\processeddata\modelc%s.dat"%(str(ModelNumber)),"w")
pickle.dump(neigh,fout)
fout.close()

print 'finished'
