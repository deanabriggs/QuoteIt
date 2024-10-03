# Connect to Cloud Database
import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Import functions from "equipment.py" & customers.py
from equipment import add_equipment, view_equipment, edit_equipment, delete_equipment
from customers import add_customer

# Menu Options for User Interface
def menu():
    choice = input("""
Select and Options:
  1. Add Equipment
  2. View Equipment
  3. Edit Equipment
  4. Delete Equipment                 
  5. Add a Customer                   
  6. Build a Quote
  7. Delete a Quote
  8. Exit
-> """)

    # Define Actions Based on User Selection
    if(choice == "1"):
        add_equipment(db)
        menu()
    elif(choice == "2"):
        view_equipment(db)
        menu()
    elif(choice == "3"):
        edit_equipment(db)
        menu()
    elif(choice == "4"):
        delete_equipment(db)
        menu()
    elif(choice == "5"):
        add_customer(db)
        menu()
    elif(choice == "8"):
        print("You have exited the program.\n")
        quit()
    else:
        print("Invalid choice. Try again.")
        menu()

if __name__ == "__main__":
    menu()