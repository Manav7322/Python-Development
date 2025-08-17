import os
import shutil
import glob
import sys

def move_txt_files(folder_path):
    if not os.path.exists(folder_path):
        print(f'Error: Path {folder_path} does not exist.')
        return
    if not os.path.isdir(folder_path):
        print(f'Error: Path {folder_path} is not a directory.')

    text_folder=os.path.join(folder_path,"TextFiles")
    os.makedirs(text_folder,exist_ok=True)

    files=os.listdir(folder_path)
    print(f"Files in {folder_path}: {files}")

    move_count=0
    for file_name in files:
        full_path=os.path.join(folder_path,file_name)

        if os.path.isdir(full_path):
            continue

        if file_name.lower().endswith(".txt"):
            dest_path=os.path.join(text_folder,file_name)
            shutil.move(full_path,dest_path)
            print(f"Moved: {file_name}->{dest_path}")
            move_count+=1
    print(f"\n Moved {move_count} text file(s) to '{text_folder}'.")
    
if __name__=="__main__":
    if(len(sys.argv)!=2):
        print("Usage:python file_handling_basics.py <folder_path>")
    else:
        move_txt_files(sys.argv[1])