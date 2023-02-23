import os
import shutil
path = " " # Here your path must be located.
if os.path.exists(path):
    print(path, "exists.")
    if os.path.isfile(path):
        print(path,"contains a file.")
        confirm = input("Do you want to remove this path? Y/N: ").upper()
        if confirm == 'Y':
            os.remove(path)
            print(path,"has been removed")
        elif confirm == 'N':
            print("Operation declined.")
    elif os.path.isdir(path):
        print(path,"contains a directory.")
        try:
            confirm = input("Do you want to remove this path? Y/N: ").upper()
            if confirm == 'Y':
                shutil.rmtree(path)
                print(path,"has been removed")
            elif confirm == 'N':
                print("Operation declined.")
        except OSError as e:
            print("Directory isn't empty.")
    else:
        print(path,"isn't a file.")
else:
    print("Path doesn't exists.")