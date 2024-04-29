import os

def listing_files_in_folder(folder):
    try:
        files=os.listdir(folder)
        return files, None
    except FileNotFoundError:
        return None, "folder not found"
    except PermissionError:
        return None, "Permision error"

def main():
    folders=input("Enter the list of folders with space seperated: ").split()
    for folder in folders:
        result,error_message=listing_files_in_folder(folder)
        if result:
            print(f"list of files in {folder} folder")
            for file in result:
                print(file)
        else:
            print(f"Error in {folder}: Error is {error_message}")

if __name__=="__main__":
    main()

