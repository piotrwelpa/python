import os

def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir(r"/home/piotr/Desktop/python/kurs/pliki/secretmessage")
    print(file_list)
    saved_path = os.getcwd()
    print("Current Working directory is: "+saved_path)
    os.chdir(r"/home/piotr/Desktop/python/kurs/pliki/secretmessage")
     #(2) for each file, rename filename
    
    for filename in file_list:
        print("Old name: "+filename)
        print("New name: "+filename.translate(None, "0123456789")+"\n")
        os.rename(filename, filename.translate(None, "0123456789"))
    os.chdir(saved_path)
   
rename_files()
