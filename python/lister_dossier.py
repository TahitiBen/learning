from pathlib import Path

doss = Path("python")
for f in doss.iterdir():
    print (f.name, "->", f.suffix)