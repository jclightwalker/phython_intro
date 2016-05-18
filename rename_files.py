import os
def rename_files():
    #1 get files name from a given folder
    file_list = os.listdir(r"C:\Users\Juste Guipi\Desktop\prank")
    print(file_list)
    save_path = os.getcwd()
    print("Current working dirrectory is " + save_path)
    os.chdir(r"C:\Users\Juste Guipi\Desktop\prank")

#2 pour chaque fichier on le renome
    for file_name in file_list:
        print("Old name - "+ file_name)
        print("New name - "+ file_name.translate(None, "0123456789"))

        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(save_path)

    
rename_files()
