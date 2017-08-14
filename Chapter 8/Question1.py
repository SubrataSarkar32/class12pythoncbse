f=raw_input('Enter valid file full pathname: ')
text=''''''
try:
    with io.open(f,'r',encoding='utf8') as opf:
                   text11 = opf.read()
    i=0
    while i<len(text11):
        if text11[i]==' ':
            for j in range(i,len(text)):
                if text11[j]!=' ':
                    break
            i=j
            text+=' '
        else:
            text+=text11[i]
            i+=1
    opf.close()
    print 'Text saved is: '
    print text
    f=f[:-4]+'-spaceremove.txt'
    with io.open(f,'w',encoding='utf8') as sf:
                  sf.write(text)
                  sf.close()
    print 'File removed of consecutive blank spaces and saved with name: ',f
except Exception as e:
    print 'Error!',e
