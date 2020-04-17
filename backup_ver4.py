import os 
import time
import zipfile



folderPath = 'C:\\My Documents'     #   Путь к папке, которую нужно архивировать
archievePath = 'D:\\Python\\backup\\test10.zip'


# create a ZipFile object
with zipfile.ZipFile(archievePath, 'w') as zipObj:
   # Iterate over all the files in directory
   for folderName, subfolders, filenames in os.walk(folderPath):
       for filename in filenames:
           #create complete filepath of file in directory
           filePath = os.path.join(folderName, filename)
           # Add file to zip
           zipObj.write(filePath)