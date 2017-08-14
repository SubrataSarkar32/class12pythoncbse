text='This is text.\nHow does this read?'
outfile=open('writethis.txt','w+')
outfile.write(text)
outfile.close()
infile=open('writethis.txt','r+')
print ord(infile.read(1))
print infile.read()
infile.close()
import sys

d='This is text to be written'
class StdinCatcher:
     def __init__(self):
         self.data = ''
     def write(self, stuff):
         self.data = self.data + stuff
     def read(self,stuff):
         return raw_input('Edit text: '+self.data)

sys.stdin=
ghi=readline.Readline()
ghi.insert_text(d)
po=k.readline()
print sys.__stdin__
sys.stdout.write(po)


