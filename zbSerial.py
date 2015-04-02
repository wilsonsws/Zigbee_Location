from sklearn.neighbors import KNeighborsClassifier
import pickle
import serial

F_SIZE = 9
FINGER = 6
CardID = []
PredictClass = []

serDataFile = open(r"C:\Users\wilsonsws\Desktop\test\realtime\serialtest.txt","w+")
serDataRecord = open(r'C:\Users\wilsonsws\Desktop\test\realtime\serialrecord.txt','a+')
middleDataFile = open(r"C:\Users\wilsonsws\Desktop\test\realtime\middletest.txt","a+")

CardDict = {'2C':'1',
            '3D':'2',
            '49':'3',
            '8B':'4',
            '9B':'5',
            '9D':'6',
            'A4':'7'}
CardConvert = {'1':'2C',
               '2':'3D',
               '3':'49',
               '4':'8B',
               '5':'9B',
               '6':'9D',
               '7':'A4'}
PositionDict = { '01 01':'01',
                 '01 02':'02',
                 '01 03':'03',
                 '01 04':'04',
                 '02 01':'05',
                 '02 02':'06',
                 '02 03':'07',
                 '02 04':'08',
                 '00 00':'00'}
Filter = {'1':[0]*(FINGER+1),
          '2':[0]*(FINGER+1),
          '3':[0]*(FINGER+1),
          '4':[0]*(FINGER+1),
          '5':[0]*(FINGER+1),
          '6':[0]*(FINGER+1),
          '7':[0]*(FINGER+1)}

fin = open(r'C:\Users\wilsonsws\Desktop\test\processeddata\Model3.dat')
neigh = pickle.load(fin)
fin.close

ser = serial.Serial()
ser.baudrate = 19200
ser.port = 20
ser.open()
count = 0

while True:
    try:
        for i in range(1,2):
            serLine = ser.read(16)
            for j in range(0,16):
                if ord(serLine[j]) < 16:
                    serDataFile.write('0')
                    serDataFile.write(hex(ord(serLine[j]))[2:].upper())
                else:
                    serDataFile.write(hex(ord(serLine[j]))[2:].upper())
                serDataFile.write(' ')
            serDataFile.write('\n')
        serDataFile.seek(0)
        
        for Node in serDataFile:

            serDataRecord.write(Node)
            serDataRecord.seek(0)

            NodeInfo = Node.strip().split(' ')
            #print NodeInfo[3]
            NodeLine = PositionDict[NodeInfo[5]+' '+NodeInfo[6]]+':'+str(int(NodeInfo[4],16))+' '+\
                       PositionDict[NodeInfo[10]+' '+NodeInfo[11]]+':'+str(int(NodeInfo[9],16))+' '+\
                       PositionDict[NodeInfo[13]+' '+NodeInfo[14]]+':'+str(int(NodeInfo[12],16))+'\t'+\
                       '%s'%(CardDict[NodeInfo[3]])+'\n'
            #middleDataFile.write(NodeLine)
        serDataFile.seek(0)
        #middleDataFile.seek(0)

        #for NodeLine in middleDataFile:
        entry,ClassName = NodeLine.strip().split('\t')
        data = [0]*(F_SIZE+1)           # Data_predict
        item = entry.split(' ')
        #index,level = item[0].split(':')
        #data[int(index)] = int(level)*10
        for i in range(0,3):
            index,level = item[i].split(':')
            data[int(index)] = int(level)
        data[-1] = int(item[0].split(':')[0])*100
        cls = neigh.predict([data])  # what's this ?
        CardID = int(ClassName)
        #CardID.append(ClassName)
        #PredictClass.append(cls[0])
        PredictClass = cls[0]

        print CardConvert[str(CardID)] + ' ' + str(PredictClass)
        middleDataFile.write(CardConvert[str(CardID)] + ' ' + str(PredictClass) + '\n')
        Filter[str(CardID)][int(PredictClass)-1] = Filter[str(CardID)][int(PredictClass)-1] + 1
        Filter[str(CardID)][-1] = Filter[str(CardID)][-1] + 1
        if Filter[str(CardID)][-1] == 10:
            finalPredictNum = max(Filter[str(CardID)][:-1])
            if finalPredictNum >4:
                finalPredict = Filter[str(CardID)][:-1].index(finalPredictNum) + 1
            else:
                k = 1
                for elePredict in Filter[str(CardID)][:-1]:
                    finalPredict = finalPredict + int(elePredict)*k
                    k = k + 1
                finalPredict = int(round(finalPredict/10.0))
            Filter[str(CardID)][:] = [0]*(FINGER+1)
            resDataFile = open(r"C:\Users\wilsonsws\Desktop\test\realtime\serialresult.txt","w+")
            #for item in range(0,len(RealClass)):
            resDataFile.write(CardConvert[str(CardID)]+' '+str(finalPredict)+'\n')
            print 'Real output: ' + CardConvert[str(CardID)]+' '+str(finalPredict)
            resDataFile.close()
            finalPredict = 0

    except:
        break

      
resDataFile.close()    
ser.close()
serDataFile.close()
serDataRecord.write('\n')
serDataRecord.close()
middleDataFile.write('\n')
middleDataFile.close()
print 'exit success'
        
