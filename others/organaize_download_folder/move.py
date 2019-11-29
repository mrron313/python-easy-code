
import os
import shutil
import filetypecheck

SUB_DIR_LIST = { 
    'DIR_PICS': '/home/arif/Downloads/Pics', 
    'DIR_VIDS': '/home/arif/Downloads/Vids', 
    'DIR_MP3s': '/home/arif/Downloads/MP3s', 
    'DIR_EXCELS': '/home/arif/Downloads/Excels',  
    'DIR_SQLS': '/home/arif/Downloads/Sqls', 
    'DIR_TXTS': '/home/arif/Downloads/Txts' 
}

def move(single_file, file_path):
    if filetypecheck.isImage(single_file):
        if not os.path.exists(SUB_DIR_LIST['DIR_PICS']):
            os.makedirs(SUB_DIR_LIST['DIR_PICS'])
        shutil.move(file_path, SUB_DIR_LIST['DIR_PICS'])
    
    if filetypecheck.isMovie(single_file):
        if not os.path.exists(SUB_DIR_LIST['DIR_VIDS']):
            os.makedirs(SUB_DIR_LIST['DIR_VIDS'])
        shutil.move(file_path, SUB_DIR_LIST['DIR_VIDS'])

    if filetypecheck.isExcel(single_file):
        if not os.path.exists(SUB_DIR_LIST['DIR_EXCELS']):
            os.makedirs(SUB_DIR_LIST['DIR_EXCELS'])
        shutil.move(file_path, SUB_DIR_LIST['DIR_EXCELS'])

    if filetypecheck.isSql(single_file):
        if not os.path.exists(SUB_DIR_LIST['DIR_SQLS']):
            os.makedirs(SUB_DIR_LIST['DIR_SQLS'])
        shutil.move(file_path, SUB_DIR_LIST['DIR_SQLS'])
    
    if filetypecheck.isTxt(single_file):
        if not os.path.exists(SUB_DIR_LIST['DIR_TXTS']):
            os.makedirs(SUB_DIR_LIST['DIR_TXTS'])
        shutil.move(file_path, SUB_DIR_LIST['DIR_TXTS'])

    if filetypecheck.isMp3(single_file):
        if not os.path.exists(SUB_DIR_LIST['DIR_MP3s']):
            os.makedirs(SUB_DIR_LIST['DIR_MP3s'])
        shutil.move(file_path, SUB_DIR_LIST['DIR_MP3s'])