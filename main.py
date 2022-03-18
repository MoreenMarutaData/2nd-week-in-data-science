# Initial dictionary

contact_book = {'Moreen' : 'moreen@moringa.org',
        'Parul' : 'parul@moringa.org',

        'Thomas' : 'thomas@moringa.org',

        'Ashley' : 'ashley@moringa.org',

        'Kellen' : 'kellen@moringa.org',

        'June' : 'june@moringa.org',

        'Joseph' : 'joe@moringa.org',

        'Lillian' : 'lillian@moringa.org',

        'Arnold' : 'arnold@moringa.org'
}
print(contact_book)

# Delete a contact from the dictionary when the user specifies the its key
# Write a code for entering the key

krr = str (input(" Which contact did you want to delete? "))

if krr in contact_book:
  del contact_book[krr]
#print(contact_book)
else:
 print(" Please enter a valid contact.")

print(contact_book)

# Print out the first 2 contacts.

first_two = list(contact_book) [:2]
print(first_two)

len(contact_book)

# Display the total no. of contacts left in the dictionary.

print("There are", str(len(contact_book)), "contacts in the contact book. ")

print(contact_book)

# Add 2 new contacts in the dictionary.

new_contact_1 = str(input("Enter name of new contact 1: "))
email_contact_1 = new_contact_1.lower() + "@moringa.org"
print(email_contact_1)

new_contact_2 = str(input("Enter name of new contact 2: "))
email_contact_2 = (new_contact_2.lower() + "@moringa.org")
print(email_contact_2)

contact_book[new_contact_1] = email_contact_1
contact_book[new_contact_2] = email_contact_2
print(contact_book)

# Print out all the contacts.

print(contact_book)
