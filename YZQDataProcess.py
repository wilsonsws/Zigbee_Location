FileName = raw_input()
#PointNumber = re.findall(r"[0-9]+",FileName)
#print PointNumber[0]
dataFile = open(r"C:\Users\wilsonsws\Desktop\test\%s.txt"%(FileName),"r")
outFile = open(r'C:\Users\wilsonsws\Desktop\test\processeddata\data%s.txt'%(FileName),'w')

itemSorted = ['0']*5
className = FileName[-1]

for line in dataFile:
    item = line.strip().split(' ')
    
    for i in range(0,4):
        if int(item[i*2],16) == 0:
            itemSorted[0] = item[i*2 + 1]
        elif int(item[i*2],16) == 1:
            itemSorted[1] = item[i*2 + 1]
        elif int(item[i*2],16) == 2:
            itemSorted[2] = item[i*2 + 1]
        else:
            itemSorted[3] = item[i*2 + 1]
    
    itemSorted[-1] = className
    
    for j in range(0,4):
        outFile.write(itemSorted[j])
        outFile.write(' ')
    outFile.write(itemSorted[4])
    outFile.write('\n')
    itemSorted[:] = ['0']*5

print 'process finished'
dataFile.close()
outFile.close()
print 'finished'
    

