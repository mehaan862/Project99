import time
import os 
import shutil

days=30

path='C:\PythonProjects\Projects\deletefile.txt'
seconds=time.time()-(days*24*60*60)
existpath=os.path.exists(path)


if (existpath==True):
    os.remove(path)
    