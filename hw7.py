#!/usr/bin/env python3

'''
 This is my Assignment-7 program
 This program will create a dictionary of names and usernames.
 User is given options menu to choose from.
 User can delete , add or lookup an entry.
 Added this comment from github.
'''

# import SortedDict
from sortedcontainers import SortedDict

# function to print options menu from which the user can choose from
def print_menu():
    print('1. Print Users')
    print('2. Add a User')
    print('3. Remove a User')
    print('4. Lookup a Phone Number')
    print('5. Quit')
    print()


# Create dictionary with key = Names, value = user_name
usernames = SortedDict()
usernames['Summer'] = 'summerela'
usernames['William'] = 'GoofyFish'
usernames['Steven'] = 'LoLCat'
usernames['Zara'] = 'zanyZara'
usernames['Renato'] = 'songDude'

# setup counter to store menu choice
menu_choice = 0

# display your menu
print_menu()

# as long as the menu choice isn't "quit" get user options
while menu_choice != 5:
    # get menu choice from user
    while True:

        # exception handling for user options
        try:
            menu_choice = int(input("Type in a number (1-5): "))
            break
        except ValueError:
            print("Please choose a number from the given menu")


    # view current entries
    if menu_choice == 1:

        # exception handling for printing values in the dictionary.
        if bool(usernames):
            print("Current Users:")
            for x, y in usernames.items():
                print("Name: {} \tUser Name: {} \n".format(x, y))
        else:
            print("There are no values in the List.")


    # add an entry
    elif menu_choice == 2:
        print("Add User")
        while True:
        # exception handling for adding an entry
            name = input("Name: ")
            if name not in usernames:
                username = input("User Name: ")
                usernames[name] = username
                print("Added {} to dictionary".format(name))
                break
            else:
                print("{} already exists in the dictionary choose a different name".format(name))


    # remove an entry
    elif menu_choice == 3:
        print("Remove User")

        while True:
        # exception handling for removing an entry
            name = input("Name: ")
            if name in usernames:
                del usernames[name]  # delete that entry
                print("Deleted {} from the dictionary".format(name))
                break
            else:
                print("{} does not exists in the dictionary choose a different name.".format(name))

    # view user name
    elif menu_choice == 4:

        print("Lookup User")
        while True:
            # exception handling for looking up an entry
            name = input("Name: ")
            if name in usernames:
                print("Username associated with {} is : {}".format(name,usernames[name]))  # print the username
                break
            else:
                print("No username associated with {} found in the list.".format(name))  # print username not found


    # is user enters something strange, show them the menu
    elif menu_choice != 5:
        print_menu()



