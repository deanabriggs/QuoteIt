# Add Equipment to Database
def add_equipment(db):
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
        "cost": cost, 
        "description": description, 
        "part_num": part_num, 
        "category": category, 
        "retail": retail, 
        "labor_hours": labor_hours, 
        "manufacture": manufacture,
        "active": True
    }

    # export the data to the firestore database - equipment collection
    db.collection("equipment").document(equip_name).set(details)
    input("The equipment has been added. Press enter to return to the main menu.")

# Display Equipment Details from the Database
def view_equipment(db):
    print("\n** Available Equipment **")
    existing = db.collection('equipment').get()
    for doc in existing:
        print(f" - {doc.id}")

    view_detail = input("Do you want to view item details? (y/n) -> ") or "n"
    if view_detail.lower() == "y":
        equip_name = input('\nWhat item do you want to view -> ')
        result = db.collection("equipment").document(equip_name).get()

        # Handle an invalid entry
        if result.exists:
            print(result.to_dict())
        else:
            print("Sorry, that is not an existing option.")
    
        print()
        input("Press enter to return to the main menu.")

# Displays existing equipment and prompts for editing
def edit_equipment(db):
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

# Displays existing equipment and prompts for deleting
def delete_equipment(db):
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

        # Confirmaiton safe guard to ensure the delete is intentional
        confirm = input("Are you sure you want to DELETE this equipment? If so, type 'DELETE' -> ")
        if(confirm == "DELETE"):
            db.collection("equipment").document(equip_name).delete()
            input(f"The '{equip_name}' has been deleted. Press enter to return to the main menu.")
        else:
            print("This action has been aborted. You have NOT deleted any equipment. Press enter to return to the main menu.")
    else:
        input("Sorry, that is not an existing option. Press enter to return to the main menu.")
    
    print()