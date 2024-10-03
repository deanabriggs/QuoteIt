# Add Customer to Database (using document auto ID)
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

    # export the date to the firestore database - customers collection
    db.collection("customers").document().set(details)
    input("The customer has been added. Press enter to return to the main menu.")