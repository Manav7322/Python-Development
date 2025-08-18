from pathlib import Path
from Excel_logging import log_file_move 
import shutil
import json

def load_config(path="config.json"):
    with open(path, "r") as f:
        return json.load(f)




def organize_files(folder_path, config):
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
            category = None
            for cat, exts in config["extensions"].items():
                if ext in exts:
                    category=cat
                    break

            if not category:
                category="others"

                
            dest_folder=folder/f'{ext.upper()}{category}'
            dest_folder.mkdir(exist_ok=True)

            dest_path=dest_folder/file.name
            shutil.move(str(file),str(dest_path))
            log_file_move(file.name, str(dest_folder))
            print(f"Moved: {file.name} -> {dest_folder}")
            moved_count += 1
    print(f"\n✅ Organized {moved_count} file(s) into extension-based folders.")


if __name__ == "__main__":
   config=load_config("config.json")
   organize_files("D:/Python/Python-Development/text_folder",config)