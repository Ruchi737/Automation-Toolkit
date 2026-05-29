from organizer import organize_files
from renamer import rename_files
from scaperweb import scrape_website

while True:

    print("\n=== AUTOMATION TOOLKIT ===")
    print("1. Organize Files")
    print("2. Rename Files")
    print("3. Scrape Website")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        folder = input("Enter folder path: ")

        organize_files(folder)

    elif choice == "2":

        folder = input("Enter folder path: ")

        prefix = input("Enter new filename prefix: ")

        rename_files(folder, prefix)

    elif choice == "3":

        url = input("Enter website URL: ")

        scrape_website(url)

    elif choice == "4":

        print("Exiting toolkit...")

        break

    else:
        print("Invalid choice!")