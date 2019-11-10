
import os
import shutil

DIR = '/home/arif/Downloads/'
DIR_PICS = '/home/arif/Downloads/Pics'
DIR_VIDS = '/home/arif/Downloads/Vids'
DIR_EXCELS = '/home/arif/Downloads/Excels'
DIR_SQLS = '/home/arif/Downloads/Sqls'
DIR_TXTS = '/home/arif/Downloads/Txts'

files_in_download_folders = os.listdir(DIR)

if not os.path.exists(DIR_PICS):
    os.makedirs(DIR_PICS)

if not os.path.exists(DIR_VIDS):
    os.makedirs(DIR_VIDS)
    
if not os.path.exists(DIR_EXCELS):
    os.makedirs(DIR_EXCELS)
    
if not os.path.exists(DIR_SQLS):
    os.makedirs(DIR_SQLS)

if not os.path.exists(DIR_TXTS):
    os.makedirs(DIR_TXTS)

for single_file in files_in_download_folders:
    file_path = DIR + single_file

    if os.path.isfile(file_path):
        print("Moving ", single_file)

        if single_file.endswith('.jpg') or \
                single_file.endswith('.JPG') or \
                single_file.endswith('.png') or \
                single_file.endswith('.jpeg'): 
            shutil.move(file_path, DIR_PICS)
        
        if single_file.endswith('.mkv'):
            shutil.move(file_path, DIR_VIDS)

        if single_file.endswith('.xlsx'):
            shutil.move(file_path, DIR_EXCELS)

        if single_file.endswith('.sql'):
            shutil.move(file_path, DIR_SQLS)
        
        if single_file.endswith('.txt'):
            shutil.move(file_path, DIR_TXTS)

        print("Moved ", single_file)
