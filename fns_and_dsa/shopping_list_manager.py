def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter the item to add: ")
            if item not in shopping_list:
                shopping_list.append(item)
            else:
                print(f"Item '{item}' is already on the list.")
                return shopping_list
            
        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print(f"Item '{item}' not found in the shopping list.")
                return shopping_list
            
        elif choice == '3':
            # Display the shopping list
            if not shopping_list:
                print("The shopping list is empty.")
            else:
                print("Current Shopping List:")
            for item in shopping_list:
                print(f"- {item}")
            
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
