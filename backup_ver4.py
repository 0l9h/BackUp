import os 
import time
import zipfile

current_time = time.strftime('%Y%m%d%H%M%S')    #   current time
print(current_time)

folderPath1 = 'C:\\My Documents'     #   Path to the folder, which you need to archive
folderPath2 = 'C:\\Code'

archivePath = 'D:\\Python\\backup\\'+current_time+'.zip'


def Parser(folderPath):
       # Iterate over all the files in directory 1
   for folderName, subfolders, filenames in os.walk(folderPath):
       for filename in filenames:
           #create complete filepath of file in directory
           filePath = os.path.join(folderName, filename)
           # Add file to zip
           zipObj.write(filePath)


# create a ZipFile object
with zipfile.ZipFile(archivePath, 'w') as zipObj:
    Parser(folderPath1)
    Parser(folderPath2)