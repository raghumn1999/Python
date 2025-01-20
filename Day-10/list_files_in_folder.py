import os

def listing_files_in_folder(folder):
    try:
        files=os.listdir(folder)
        return files,'The list of files are'
    except FileNotFoundError:
        return None, "folder not found"
    except PermissionError:
        return None, "Permision error"

def main():
    folders=input("Enter the list of folders with space seperated: ").split()
    for folder in folders:
        fun_result,message=listing_files_in_folder(folder)
        if fun_result:
            print(f'{message} in {folder} {fun_result}')
        else:
            print(f'{message}')

if __name__=="__main__":
    main()

