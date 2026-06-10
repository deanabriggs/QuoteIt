# QuoteIt — Python + Cloud Firestore

A command-line quoting tool that lets a sales rep build customer estimates on-site and store them in a NoSQL cloud database. Built to explore Cloud Firestore collections, documents, subcollections, and maps with Python.

## Overview

This project addresses a real-world problem: sales reps needing to give quick estimates to customers during an on-site walkthrough. By responding to simple prompts, a rep can build a quote — and create multiple quotes for the same customer. The program calculates the quote from the entries and stores it for later reference, where it can also be accessed by administrative staff for tasks like drafting contracts or ordering products.

The rep is presented with a menu of options in Python. Functions calculate and format the entered data for customers, equipment, and quotes, then transmit it to Cloud Firestore so it can be searched or retrieved for other purposes.

## Cloud Database

This software uses Google Cloud Firestore, a NoSQL database that stores data in documents within collections rather than in the relational structure of traditional SQL databases. Documents can't contain other documents, but they can be related to other collections.

The Firestore database (`quote-install`) has two top-level collections:

- **equipment** — one document per piece of installable equipment, including a description, part number, install time, cost, retail price, etc.
- **customers** — one document per customer with basic info (name, address, email) plus a **quotes** sub-collection. Each quote stores totals for equipment cost, labor, and profit, the products and quantities selected, and the estimated retail price.

## Development Environment

- Google Cloud Firestore
- VS Code (v1.93.1)
- Python (v3.11.9)
- `firebase_admin` library (for credentials & Firestore functions)

## Demo

<!-- TODO: add Software Demo Video link -->

## Useful Resources

- Firebase documentation & fundamentals
- Cloud Firestore
- Set up the Firebase Admin Python SDK
- Firestore maps, arrays, and subcollections
- Structuring data in Firestore

## Future Work

- Error handling for data entry and for values not in the database
- Viewing, editing, and deleting quotes
- Mark equipment inactive instead of deleting it, and filter views to active items only
- Search for existing customers by name before adding a new one to minimize duplicates
