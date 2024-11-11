import re # used for validation,pattern matching and text processing
import json # a text file used to saved contact
import os 

#name of the file to save contacts

FILENAME ="ContactList.json"

#check email validity




def is_email_valid(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern,email) is not None

# loading the contacts into the file
def accept_contact():
    if os.path.exists(FILENAME):
       with open(FILENAME, "r") as file:
           return json.load(file)
    return[]

#taking the contacts and saving it in the file
def save_contacts(contact):
    with open(FILENAME, "w") as file:
        return json.dump(contact, file)

# add a menu so a user can choose from

    
# adding a new contact
def input_new_contact(contact):
    name = input(" Enter the contact name: ")
    phone_number = input(f" Enter the {name} phone number: ")
    while not phone_number.isdigit():
        print(" Phone number can only accept numbers")
        phone_number = input(f" Enter the {name} phone number number: ")
    
    email = input("Enter a valid email address: ")

    while not is_email_valid(email):
        print("Email is invalid. Use the right email format(example@yyyy.zzz)")
        email = input("Enter a valid email address: ")


    contact.append({"name":  name, "phone_number": phone_number, "email": email,})
    save_contacts(contact)
    print(f"The new contact information  has been added successfully" )

# viewing the contacts 

def view_contact(contact):
    if not contact:
        print(" No contacts available yet")
    else:
        for x, contact in enumerate(contact):
          print(f"{x + 1}. Name: {contact['name']}, Phone_Number: {contact['phone_number']}, Email: {contact['email']}")

# Updating a contact infomation
def update_contact(contact):
    view_contact(contact)
    index = int(input(" choose the number on the contact list you will like to update: "))-1
    if index < 0 or index >= len(contact):
        print(" the contact does not exist")
    
        return
    print(f" You're about to edit {index +1}'s contact information!!!")
    name = input(" Enter the updated contact name( leave it blanked if thesmae): ")
    phone_number= input(" Enter the updated contact phone number( leave it blanked if thesmae): ")
    email= input(" Enter the updated contact email( leave it blanked if thesmae): ")

    while  email and not is_email_valid(email):
        print("Email is invalid. Use the right email format(example@yyyy.zzz)")
        email = input("Enter a valid email address: ")
        
    if name:
        contact[index]["name"]= name
    if email:
        contact[index]["email"]= email
    if phone_number:
        contact[index]["phone_number"]= phone_number

    save_contacts(contact)
    print(" Contact Updated Successfully.")

def delete_contact(contact):
    view_contact(contact)
    index = int(input("Enter the contact number you will like to delete: "))-1

    if index <0 or index>= len(contact):
        print(" Contact number does not exist")
        return
    contact.pop(index)
    save_contacts(contact)
    print("Contact Has been deleted successfully")

#program Menu


def menu():
    contact = accept_contact()

    while True:
        print("*********************")
        print("------PHONEBOOK------")
        print("**********************")
        print("1. ADD CONTACT")
        print("2. VIEW CONTACT")
        print("3. UPDATE CONTACT")
        print("4. DELETE CONTACT")
        print("5. EXIT")
        
        choice = input(" Choose an option: ")
        
        if choice == "1":
            input_new_contact(contact)
        elif choice == "2":
            view_contact(contact)
        elif choice == "3":
            update_contact(contact)
        elif  choice == "4":
            delete_contact(contact)
        elif choice == "5":
            break
        else:
            print(" Inavlid Option. Try Again(1-5)")

if __name__ == "__main__":
    menu()



            






            
  