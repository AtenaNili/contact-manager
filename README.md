# Phonebook Application (Python)

A simple phonebook application developed in Python using **Tkinter** for the graphical user interface and **SQLite** for data storage.

This project was implemented based on a **Python practical exam question**.

## Project Description
The application allows users to manage contacts by storing names and phone numbers in a local SQLite database.  
Users can add, view, search, edit, and delete contacts through a simple graphical interface.

## Features
- Add new contacts (name and phone number)
- Display all saved contacts
- Search contacts by name
- Edit existing contacts
- Delete selected contacts
- Data persistence using SQLite
- Graphical user interface built with Tkinter

## Technologies Used
- Python
- Tkinter (GUI)
- SQLite (Database)

## Database Structure
The application uses a SQLite database with a table named `contacts`:

- `id` (Primary Key)
- `name` (Contact name)
- `phone` (Phone number)

## User Interface
The graphical interface includes:
- Input fields for name and phone number
- Buttons for:
  - Add contact
  - Delete contact
  - Edit contact
  - Show all contacts
  - Search
- A listbox to display and select contacts

## How to Run
1. Make sure Python is installed on your system
2. Run the program using:

```bash
python contact.py

## Purpose
This project was created for:
- Practicing Python fundamentals
- Completing a Python practical exam
- Learning Tkinter and SQLite
- Building a beginner-friendly portfolio project on GitHub

## Author
- Atena Nili
