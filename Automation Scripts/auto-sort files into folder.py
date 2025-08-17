from pathlib import Path
import shutil

def organize_files(folder_path):
    folder=Path(folder_path)

    if not folder.exists():
        print(f"Error: {folder} does not exist.")
        return 
    if not folder.is_dir():
        print(f"Error: {folder} is not a directory.")
        return
    
    files=list(folder.iterdir())
    print(f"files in {folder}: {[f.name for f in files]}")

    moved_count=0
    for file in files:
        if file.is_file():
            ext=file.suffix.lower()
            if ext=="":
                ext="no_extension"
            else:
                ext=ext[1:]
                
            dest_folder=folder/f'{ext.upper()}Files'
            dest_folder.mkdir(exist_ok=True)

            dest_path=dest_folder/file.name
            shutil.move(str(file),str(dest_path))

            print(f"Moved: {file.name} -> {dest_folder}")
            moved_count += 1
    print(f"\n✅ Organized {moved_count} file(s) into extension-based folders.")


if __name__ == "__main__":
   organize_files("D:/Python/Python-Development/text_folder")