FileName = raw_input()
#PointNumber = re.findall(r"[0-9]+",FileName)
#print PointNumber[0]
File = open(r"C:\Users\wilsonsws\Desktop\test\%s.txt"%(FileName),"r")
NodeFile = File.read()
NodeContent = NodeFile.split("FA 3B 02")
print NodeContent[1]
print NodeContent[2]
print NodeContent[-1]
print len(NodeContent)
CardDict = {'2C':'%s'%(int(FileName[-1],16)*7-6),
            '3D':'%s'%(int(FileName[-1],16)*7-5),
            '49':'%s'%(int(FileName[-1],16)*7-4),
            '8B':'%s'%(int(FileName[-1],16)*7-3),
            '9B':'%s'%(int(FileName[-1],16)*7-2),
            '9D':'%s'%(int(FileName[-1],16)*7-1),
            'A4':'%s'%(int(FileName[-1],16)*7)}
#CardDict = {'2C':'5',
#            '3D':'6',
#            '49':'5',
#            '8B':'4',
#            '9B':'7',
#            '9D':'6',
#            'A4':'test'}
PositionDict = { '01 01':'01',
                 '01 02':'02',
                 '01 03':'03',
                 '01 04':'04',
                 '02 01':'05',
                 '02 02':'06',
                 '02 03':'07',
                 '02 04':'08',
                 '00 00':'00'}
result = ""
#Tresult = ""
for Node in NodeContent[1:]:
    NodeInfo = Node.strip().split()
    #if CardDict[NodeInfo[0]] == 'test':
    #    TestLine = PositionDict[NodeInfo[2]+' '+NodeInfo[3]]+":"+str(int(NodeInfo[1],16))+" "+\
    #               PositionDict[NodeInfo[7]+' '+NodeInfo[8]]+":"+str(int(NodeInfo[6],16))+" "+\
    #               PositionDict[NodeInfo[10]+' '+NodeInfo[11]]+":"+str(int(NodeInfo[9],16))+"\t"+\
    #               "%s"%(CardDict[NodeInfo[0]])+"\n"
    #    Tresult = Tresult + TestLine
    #    continue
    NodeLine = PositionDict[NodeInfo[2]+' '+NodeInfo[3]]+":"+str(int(NodeInfo[1],16))+" "+\
               PositionDict[NodeInfo[7]+' '+NodeInfo[8]]+":"+str(int(NodeInfo[6],16))+" "+\
               PositionDict[NodeInfo[10]+' '+NodeInfo[11]]+":"+str(int(NodeInfo[9],16))+"\t"+\
               "%s"%(CardDict[NodeInfo[0]])+"\n"
    result = result + NodeLine
File2 = open("C:\\Users\\wilsonsws\\Desktop\\test\\processeddata\\data%s.txt"%(FileName),"w")
#File3 = open("C:\\Users\\wilsonsws\\Desktop\\test\\processeddata\\dataTEST%s.txt"%(FileName),"w")
File2.write(result)
#File3.write(Tresult)
File2.close()
#File3.close()
File.close()
print NodeContent[300]

