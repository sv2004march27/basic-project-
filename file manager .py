import os
def crete_file(filename):
    try:
        with open(filename,"x")as f:
            print(f"file name {filename}: created")
    except FileExistsError:
        print(f"file name {filename}: already exists")
    except Exception as error:
        print("an error occurred")
def view_all_files():
    files = os.listdir()
    if not files:
        print("no files found")
    else:
        print("files in directory")
        for file in files:
            print(file)
def delete_file(filename):
    try:
        os.remove(filename)
        print(f"file name {filename} deleted")
    except FileNotFoundError:
        print(f"file name {filename} does not exist")
    except Exception as error:
        print("an error occurred")
def read_file(filename):
    try:
        with open("sample.txt","r")as f:
            content = f.read()
            print(f"content of '{filename}':\n {content}")
    except FileNotFoundError:
        print(f"file name {filename} does not exist")
    except Exception as error:
        print("an error occurred")
def edit_file(filename):
    try:
        with open("sample.txt","w")as f:
            content = input("enter data to add =")
            f.write(content + "\n")
            print("content aded to {filename}succesfully")
    except FileNotFoundError:
        print(f"file name {filename} does not exist")
    except Exception as error:
        print("an error occurred")
def main():
    while True:
        print("FILE MANAGER")
        print("1. Create a new file")
        print("2. View all files")
        print("3. Delete a file")
        print("4. Edit a file")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            filename = input("Enter file name: ")
            crete_file(filename)
        elif choice == "2":
            view_all_files()
        elif choice == "3":
            filename = input("Enter file name: ")
            delete_file(filename)
        elif choice == "4":
            filename = input("Enter file name: ")
            edit_file(filename)
        elif choice == "5":
            print("Exit")
            break
        else:
            print("Invalid choice")
if __name__ == "__main__":
    main()


