# unzip the zip file with python : 
import zipfile 
from zipfile import ZipFile 

with ZipFile ('CSS3-animation-main.zip', 'r') as unzip : 
    unzip.extractall()
    
print(unzip.namelist())
