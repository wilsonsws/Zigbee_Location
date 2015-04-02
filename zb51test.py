FILE_NAME = raw_input()
File = open("C:\\Users\\wilsonsws\\Desktop\\test\\processeddata\\%s.txt"%(FILE_NAME),"r")
LocationDict = {'1':'03',
                '2':'02',
                '3':'03',
                '4':'0100',
                '5':'03',
                '6':'06',
                '7':'07'}
RightDict = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0}
TotalDict = {'1':0,'2':0,'3':0,'4':1,'5':0,'6':0,'7':0}

for line in File:
    data,classes = line.strip().split('\t')
    if data.split(':')[0] == LocationDict[classes]:
        RightDict[classes] = RightDict[classes]+1
        TotalDict[classes] = TotalDict[classes]+1
    else:
        TotalDict[classes] = TotalDict[classes]+1

for i in range(1,8):
    print 'pointcard ' + str(i) + ' ' + 'accuracy: ' + str(float(RightDict[str(i)])/TotalDict[str(i)])
print 'successed'
File.close()
