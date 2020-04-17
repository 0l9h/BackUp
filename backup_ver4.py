import os 
import time
import zipfile

current_time = time.strftime('%Y%m%d%H%M%S')    #   current time
print(current_time)

folderPath = 'C:\\My Documents'     #   Path to the folder, which you need to archive
archivePath = 'D:\\Python\\backup\\'+current_time+'.zip'


# create a ZipFile object
with zipfile.ZipFile(archivePath, 'w') as zipObj:
   # Iterate over all the files in directory
   for folderName, subfolders, filenames in os.walk(folderPath):
       for filename in filenames:
           #create complete filepath of file in directory
           filePath = os.path.join(folderName, filename)
           # Add file to zip
           zipObj.write(filePath)