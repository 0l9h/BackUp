import os 
import time
import zipfile

current_time = time.strftime('%H%M%S')    #   current time
current_date = time.strftime('%Y%m%d')    #   current date

folderPath1 = 'C:\\My Documents'     #   Path to the folder, which you need to archive
folderPath2 = 'C:\\Code'

if not os.path.exists('D:\\Python\\backup'+os.sep+current_date):     #   if there isn't folder with current date name, create it
    os.mkdir('D:\\Python\\backup'+os.sep+current_date)
    print('Folder succesfully created')

archivePath = 'D:\\Python\\backup' + os.sep + current_date + os.sep + current_time+'.zip'   #   place archive with current time as name to this directory


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
    Parser(folderPath1)     #   Calling fucntion for different folders
    Parser(folderPath2)

print('Backup succesfully created in directory', archivePath)