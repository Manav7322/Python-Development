import os
from datetime import datetime

file="sample_copy.txt"
ts=os.path.getmtime(file)

dt=datetime.fromtimestamp(ts)
print("Modified on:",dt.strftime("%Y-%m-%d %H:%M:%S"))