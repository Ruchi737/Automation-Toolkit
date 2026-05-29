import os
import shutil

def organize_files(folder):
    all_files=os.listdir(folder)
    for item in all_files : 
        full_path=os.path.join(folder,item)
        if os.path.isdir(full_path):
            continue
        file_name,file_type= os.path.splitext(item)
        file_type = file_type.lower().replace(".","")
        if file_type =="":
            continue
        new_folder = file_type.upper()  +  "  Files"
        new_folder_path= os.path.join(folder, new_folder)
        if not os.path.exists( new_folder_path):
          os.mkdir(new_folder_path)
        
        shutil.move(full_path,os.path.join(new_folder_path,item))
    print("Files organized successfully!")