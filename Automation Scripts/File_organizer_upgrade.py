import os
import shutil
from datetime import datetime
from pathlib import Path
from Excel_logging import log_file_move

def organise_by_date(folder):
    folder=Path(folder)
    for file in folder.iterdir():
        if file.is_file():
            ts=file.stat().st_mtime
            dt=datetime.fromtimestamp(ts)

            date_folder=folder/dt.strftime("%Y-%m")
            date_folder.mkdir(exist_ok=True)

            shutil.move(str(file),date_folder/file.name)
            log_file_move(file,date_folder)
            print(f"Moved {file.name} → {date_folder}")

organise_by_date("text_folder")