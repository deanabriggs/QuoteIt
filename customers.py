from equipment import view_equipment

# Add Customer to Database (using document auto ID - unknown key) 
def add_customer(db):
    # Prompt the user for the new equip data
    name = input("Customer's first & last name -> ").title()
    street = input("Street address -> ")
    city = input("City -> ")
    state = input("State -> ")
    email = input("Email -> ")
    
    # Create a dictionary for the cloud document
    details = {
        "Name":name, 
        "Street":street,
        "City":city,
        "State":state,
        "email":email
    }

    # export the data to the firestore database - customers collection
    db.collection("customers").document().set(details)
    input("The customer has been added. Press enter to return to the main menu.")

#
def quote_customer(db):
    docs = db.collection("customers").get()
    customer = input("What customer do you want to quote? -> ").title()
    for doc in docs:
        if doc.to_dict()["Name"] == customer:                   # improvement needed: catch if the customer doesn't exist - possibly providing a list of names or formatting the text to lowercase
            key = doc.id
    customerId = db.collection("customers").document(key)
    add_quote_subcollection(db, customerId)
    

def add_quote_subcollection(db, customerId):
    customer = customerId.get().to_dict().get("Name")
    equip_list = {}         # store selected equip with quantity in a dictionary
    install_hours = 0
    labor_cost = 0
    equip_cost = 0
    profit = 0
    retail = 0

    # Show available equipment to add to quote
    view_equipment(db)
    
    response = input("\nWould you like to one of these items to the quote? (y/n) -> ").lower() or "y"
    
    while response == "y":
        equip = input("What item do you want to add to the quote? ").lower()   # improvement needed: catch if the entry doesn't exist. Also, provide option to add a new item using the add_equipment function
        quantity = int(input(f"How many '{equip}'? (1) -> ") or 1)
        response = input("Would you like to add another item? (y/n) -> ").lower() or "y"

        # set a variable to the equipment path
        equip_doc = db.collection("equipment").document(equip).get()

        # add the item to the equip_list
        equip_list[equip] = quantity
       
        # calculate total quote values
        equip_data = equip_doc.to_dict()
        install_hours += equip_data.get("labor_hours")
        equip_cost += equip_data.get("cost") * quantity
        retail += equip_data.get("retail") * quantity

        labor_cost = install_hours * 50                               # hard code labor hour cost at $50
        profit = retail - labor_cost - equip_cost

    title = input("Give your quote a title -> ").title()

    details = {
        "customer": customer,
        "equip cost": equip_cost,
        "equipment": equip_list,
        "install hours": install_hours,
        "labor cost": labor_cost,
        "profit": profit,
        "retail": retail
    }

    # export the data to the firestore database - quote subcollection
    customerId.collection("quotes").document(title).set(details)
    print(f"\n{title} = ${retail}\n")
    input("The quote has been saved. Press enter to return to the main menu.")