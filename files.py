def filestrings(filename1,filename2,filename3,resultfile):
    lines1 = []
    summ1 = 0
    summ2 = 0
    summ3 = 0
    fileslist = [{'name': '1','count': 2,'lines':[]}, {'name':'2', 'count': 1,'lines':[]}, {'name': '3', 'count': 3,'lines':[]}]
    with open(filename1, 'rt', encoding='utf-8') as filefirst:
        for line in filefirst:
            fileslist[0]['lines'].append(line)
            summ1 += 1
        fileslist[0]['name'] = filename1
        fileslist[0]['count'] = str(summ1)
    with open(filename2, 'rt', encoding='utf-8') as filesecond:
        for line in filesecond:
            fileslist[1]['lines'].append(line)
            summ2 += 1
        fileslist[1]['name'] = filename2
        fileslist[1]['count'] = str(summ2)
    with open(filename3, 'rt', encoding='utf-8') as filethird:
        for line in filethird:
            fileslist[2]['lines'].append(line)
            summ3 += 1
        fileslist[2]['name'] = filename3
        fileslist[2]['count'] = str(summ3)  
    fileslist.sort(key = lambda x:x.get('count'))
    with open(resultfile, 'a', encoding='utf-8') as resultingfile:
            resultingfile.write(fileslist[0]['name'])
            resultingfile.write('\n')
            resultingfile.write(fileslist[0]['count'])
            resultingfile.write('\n')
            resultingfile.writelines(fileslist[0]['lines'])
            resultingfile.write('\n')
            resultingfile.write(fileslist[1]['name'])
            resultingfile.write('\n')
            resultingfile.write(fileslist[1]['count'])
            resultingfile.write('\n')
            resultingfile.writelines(fileslist[1]['lines'])
            resultingfile.write('\n')
            resultingfile.write(fileslist[2]['name'])
            resultingfile.write('\n')
            resultingfile.write(fileslist[2]['count'])
            resultingfile.write('\n')
            resultingfile.writelines(fileslist[2]['lines'])
filestrings('1.txt','2.txt','3.txt','result.txt')