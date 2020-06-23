fileoj = open('06-21-2020.csv','r')
fileoj.readline()
datalist = fileoj.readlines()
fileoj.close()
conflist = []
#print(datalist)
for country in datalist:
    #print(country)
    templist = country.split(',')
    pname = templist[2]
    cname = templist[3]
    lat = templist[5]
    lon = templist[6]
    conf = templist[7]
    #print(pname + cname + lat + lon + conf)
    conflist.append({'pname':pname,'cname':cname,'lat':lat,'lon':lon,'conf':conf})
#print(conflist)
conflist.sort(key=lambda a: a['conf'], reverse=True)
fileout = open('test.js','w')
fileout.write('data='+ str(conflist))
fileout.close()