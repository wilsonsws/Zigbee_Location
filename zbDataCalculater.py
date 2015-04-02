fileName = raw_input()
file1 = open(r"C:\Users\wilsonsws\Desktop\test\processeddata\%s.txt"%(fileName),"r")

positionDict = { '1':[1,1],
                 '2':[2,1],
                 '3':[3,1],
                 '4':[4,1],
                 '5':[1,2],
                 '6':[2,2],
                 '7':[3,2],
                 '8':[4,2],
                 '9':[1,3],
                 '10':[2,3],
                 '11':[3,3],
                 '12':[4,3],
                 '13':[1,4],
                 '14':[2,4],
                 '15':[3,4],
                 '16':[4,4]}
PositionTrans = {'%s'%1:'p2C',
                 '%s'%2:'p3D',
                 '%s'%3:'p49',
                 '%s'%4:'p8B',
                 '%s'%5:'p9B',
                 '%s'%6:'p9D',
                 '%s'%7:'pA4'}
CountDict = {'1':[0]*16,
             '2':[0]*16,
             '3':[0]*16,
             '4':[0]*16,
             '5':[0]*16,
             '6':[0]*16,
             '7':[1]*16}

resultDict = {'1':[0,0],
              '2':[0,0],
              '3':[0,0],
              '4':[0,0],
              '5':[0,0],
              '6':[0,0],
              '7':[0,0]}

for line in file1:
    realN,predictN = line.strip().split()
    #if CountDict[realN][int(predictN)-1] == 0:
    #    CountDict[realN][int(predictN)-1] = CountDict[realN][int(predictN)-1] + 1
    CountDict[realN][int(predictN)-1] = CountDict[realN][int(predictN)-1] + 1

for i in range(1,8):
    resultX = 0
    resultY = 0
    countN = 0
    for j in range(1,17):
        if not CountDict[str(i)][j-1] == 0:
            #if CountDict[str(i)][j-1] > 50:
            #    resultX = positionDict[str(j)][0]*50.0 + resultX
            #    resultY = positionDict[str(j)][1]*50.0 + resultY
            #    countN = countN + 50.0
            #else:
            resultX = positionDict[str(j)][0]*(CountDict[str(i)][j-1]**(1.0/2)) + resultX
            resultY = positionDict[str(j)][1]*(CountDict[str(i)][j-1]**(1.0/2)) + resultY
            countN = countN + (CountDict[str(i)][j-1]**(1.0/2))
    resultDict[str(i)][0] = float(resultX)/countN
    resultDict[str(i)][1] = float(resultY)/countN

for k in range(1,8):
    print PositionTrans[str(k)] + ' ' + str(resultDict[str(k)])

file1.close()
print 'finished'
    
