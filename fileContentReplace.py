lst=['file1.txt','file2.txt','file3.txt']
filepath='C:/Users/Jagadeesh/Desktop/python'

for i in lst:
  with open(filepath+"/"+i,'r') as filer:
    r=filer.read()
    r=r.replace("pattern","replacePattern")
    filer.close()
  with open(filepath+"/"+i,'w') as filew:
    filew.write(r)
    filew.close()
    
