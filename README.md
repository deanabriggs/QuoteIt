# Overview
This software was designed to test the usability and functionality of a NoSQL cloud database with Python to solve a real world problem. It includes working with Cloud Firestore collections, documents, subcollections, and a map within a subcollection. It includes Python functions, import features, and a menu design.

This project addresses the issue of sales reps needing to give quick estimates to customers during an on-site walk through. A sales rep could build a quote by responding to simple prompts. It allows the sales rep to create multiple quotes for the same customer. The program will calculate a quote based on the entries and store it for later reference or it can be accessed by administrative staff for other tasks such as drafting contracts, ordering products, etc. 

The user (sales rep) is presented with a menu of options and prompts in Python. Python functions calculate and format entered data for customers, equipments, and quotes. Then, Python provides a quote to the rep and transmits the data to the Cloud Firestore database so it can be search or retrieved for other purposes.

{Provide a link to your YouTube demonstration. It should be a 4-5 minute demo of the software running, a walkthrough of the code, and a view of the cloud database.}

[Software Demo Video](http://youtube.link.goes.here)

# Cloud Database
This software uses Googles Cloud Firestore database. This is a NoSQL database, meaning it does not follow the relational structure of traditional SQL database. Data is stored in documents within collections. Documents cannot store other documents, but they can be related to other collections.

The Firestore database I created is called "quote-install" and contains two top-level collections: one for customers and another for equipment. 
- The equipment collection has a document for each piece of equipment available for installation and includes a description, part number, time to install, cost, retail, etc. 
- Documents within the customers collection are unique for each customer. Each cusotmer document contains basic information like name, address, and email, as well as a sub-collection for their quotes. 
- The sub-collection of quotes stores totals for equipment cost, labor, profit, products with quantity selected, and the estimate (or retail price).

# Development Environment

* Google Firestore Database
* VS Code (version 1.93.1)
* Python (version 3.11.9)
* Library - firebase_admin (for credentials & firestore functions)

# Useful Websites
- [Firebase Tutorial](https://www.youtube.com/watch?v=QcsAb2RR52c&list=PLl-K7zZEsYLmOF_07IayrTntevxtbUxDL&t=1s)
- [Firebase Fudimentals](https://www.youtube.com/watch?v=p9pgI3Mg-So&t=13s)
- [Cloud Firestore](https://www.youtube.com/watch?v=v_hR4K4auoQ)
- [Setup Firebase Admin Python SDK](https://github.com/firebase/firebase-admin-python)
- [Firebase Cloud Firestore with Python](https://www.youtube.com/watch?v=N0j6Fe2vAK4)
- [Firestore Maps, Arrays, and Subcollections](https://www.youtube.com/watch?v=o7d5Zeic63s&t=10s)
- [Firestore How to Structure Data](https://www.youtube.com/watch?v=haMOUb3KVSo)

# Future Work
There are several ways this program could be improved. Here are some that I have in mind.

- Error handling for data entry
- Error handling for values not in the database
- Viewing, editing, and deleting quotes
- Instead of deleting equipment, change the status to inactive
- Use inactive equipment values to filter equipment views for active items only
- Search for customers with the same name before adding a new customer to minimize duplicates