from db import add_record, view_records, search_records

while True:
    print("\n===== JsonMiniDB =====")
    print("1. Add Record")
    print("2. View Records")
    print("3. Search Records")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        age = input("Age: ")
        city = input("City: ")
        add_record(name, age, city)

    elif choice == "2":
        view_records()

    elif choice == "3":
        keyword = input("Search keyword: ")
        search_records(keyword)

    elif choice == "4":
        break

    else:
        print("Invalid choice")
