from pathlib import Path
import datetime
p=Path("sample_copy.txt")
print(p.resolve())
print(p.parent)
print(p.stem)
print(p.suffix)

file = Path("sample_copy.txt")
print(file.stat().st_size, "bytes")
print(file.stat().st_mtime)
mtime=datetime.datetime.fromtimestamp(file.stat().st_mtime)
print(mtime)