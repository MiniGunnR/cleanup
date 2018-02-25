import os
from os.path import isfile, join
from shutil import move

mypath = os.path.dirname(os.path.abspath(__file__))

def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f

onlyfiles = [f for f in listdir_nohidden(mypath) if isfile(join(mypath, f))]

for f in onlyfiles:
    if f != 'cleanup.py':
        name, ext = os.path.splitext(f)
        dir = "cleanup/%s" % ext[1:]
        if ext == '':
            dir = 'cleanup/others'
        if not os.path.exists(dir):
            os.makedirs(dir)
        move(f, dir)

print("All your file(s) have been moved inside a folder called 'cleanup'.")
