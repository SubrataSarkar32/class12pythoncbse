f='sports.dat'
text=''''''
try:
    with io.open(f,'r',encoding='utf8') as opf:
                   text11 = opf.read()
    text1l=text11.split('\n')
    for i in range(len(textl)):
        if text1l[i].split('~')[1]=='Atheletics':
            text=text+text1l[i]+'\n'
    opf.close()
    print 'Text saved is: '
    print text
    f='Ateletics.dat'
    with io.open(f,'w',encoding='utf8') as sf:
                  sf.write(text)
                  sf.close()
    print 'File created and saved with name: ',f
except Exception as e:
    print 'Error!',e
