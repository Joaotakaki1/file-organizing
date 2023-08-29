import os;
from pathlib import Path
import shutil
#change de directory
os.chdir("/Users/joaoyukiotakaki/Desktop")
#creates a folder for my videos, pdfs and images if not created yet
if not os.path.exists("videos"):
    Path("videos").mkdir(exist_ok=True)
if not os.path.exists("pdfs"):
    Path("pdfs").mkdir(exist_ok=True)
if not os.path.exists("images"):
    Path("images").mkdir(exist_ok=True)

#iterates all my files and verify the extension of them, to move the file to de right folder
for file in os.listdir():
    f = Path(file)
    ext = f.suffix
    if ext == ".pdf":
        shutil.move(file, "pdfs")
    elif ext == ".mov" or ext == ".mp4":
        shutil.move(file, "videos")
    elif ext == ".png" or ext == ".svg":
        shutil.move(file, "images")
    
