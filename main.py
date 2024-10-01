import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

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
   
    if(choice == "1"):
        add_equipment()

    if(choice == "2"):
        view_equipment()

    if(choice == "3"):
        edit_equipment()

    if(choice == "4"):
        delete_equipment()

    if(choice == "8"):
        quit()

def add_equipment():
    # Prompt the user for the new equip data
    equip_name = input("Short name for this equipment -> ").lower()
    description = input(f"{equip_name} description -> ").lower()
    cost = float(input("Our cost of the product -> ")) 
    print("---Leave the next items blank to accept DEFAULT values (shown in brackes)---")
    category = input("Type of equipment (camera) -> ").lower() or "camera"
    manufacture = input("Manufacture (HIK) -> ").upper() or "HIK"
    part_num = input("Part number (unk) -> ").upper() or "unk"
    labor_hours = float(input("Estimated tech hours to install (2) -> ") or 2)
    retail = float(input("Retail price to charge customer (calculated) -> ") or cost * 3)

    # Create a dictionary for the cloud document
    details = {
        "cost":cost, 
        "description": description, 
        "part_num": part_num, 
        "category": category, 
        "retail": retail, 
        "labor_hours": labor_hours, 
        "manufacture": manufacture,
        "active": True
    }

    # export the date to the firestore database - equipment collection
    db.collection("equipment").document(equip_name).set(details)
    input("The equipment has been added. Press enter to return to the main menu.")
    menu()

def view_equipment():
    print("\n** Available Equipment **")
    existing = db.collection('equipment').get()
    for doc in existing:
        print(f" - {doc.id}")

    equip_name = input('\nWhat item do you want to view -> ')
    result = db.collection("equipment").document(equip_name).get()

    if result.exists:
        print(result.to_dict())

    else:
        print("Sorry, that is not an existing option.")
    
    print()
    input("Press enter to return to the main menu.")
    menu()

def edit_equipment():
    # provide a list of existing equipment to update
    print("\n** Available Equipment **")
    existing = db.collection('equipment').get()
    for doc in existing:
        print(f" - {doc.id}")

    # prompt for a item to edit (check if it exists)
    equip_name = input('\nWhat item do you want to change/add -> ')
    result = db.collection("equipment").document(equip_name).get()
    if result.exists:
        print(result.to_dict())
        
        # prompt for a field parameter to be updated (check if it exists)
        param =input("\nWhat parameter do you want to change/add -> ")
        new_value = input("Change/add the value to -> ")

        if(param == "cost" or param == "retail" or param == "labor_hours"):
            new_value = float(new_value)
    
        db.collection("equipment").document(equip_name).update({param:new_value})
        input(f"The '{param}' has been updated. Press enter to return to the main menu.")        
    else:
        print("Sorry, that is not an existing option. Press enter to return to the main menu.")
    
    print()
    menu()

def delete_equipment():
    # provide a list of existing equipment to delete
    print("\n** Existing Equipment **")
    existing = db.collection('equipment').get()
    for doc in existing:
        print(f" - {doc.id}")

    # prompt for a item to delete (check if it exists)
    equip_name = input("\nWhat item do you want to delete -> ")
    result = db.collection("equipment").document(equip_name).get()
    if result.exists:
        print(result.to_dict())
        print()

        confirm = input("Are you sure you want to DELETE this equipment? If so, type 'DELETE' -> ")
        if(confirm == "DELETE"):
            db.collection("equipment").document(equip_name).delete()
            input(f"The '{equip_name}' has been deleted. Press enter to return to the main menu.")
        else:
            print("This action has been aborted. You have NOT deleted any equipment. Press enter to return to the main menu.")
    else:
        input("Sorry, that is not an existing option. Press enter to return to the main menu.")
    
    print()
    menu()

if __name__ == "__main__":
    menu()