#!/usr/bin/env python3

'''
 This is my Final Project
 This project includes a class file birthdayClass.py from which functions are called to perform necessary
 operations to run this script
    This program takes command line arguments
        # 'Add' --to add a member to the list.
        # 'Delete' --to delete a member from the existing list.
        # 'Run'  --to run the script with existing list and send email to members.
        # No command line arguments will simply run the script with existing list and send email to members.
 It includes two text file:
    birthday_list.txt -- to store dob and name related values
                            example: 26-07 BOB,GARRY
                                     2-04 DAN

    email_list.txt -- to store name and email related values
                            example: BOB bob@gmail.com
                                     GARRY garry@gmail.com

 In this program we will be working with Gmail host alone and dob in dd-mm pattern (example 26-03)
'''

from birthdayClass import birthdayEmail # importing birthdayEmail class from birthdayClass.py file.
import datetime
import sys

sendEmail = birthdayEmail() # Instantiate the class

# This is the main function which takes command line arguments

def main():
    """This is the main function which takes command line arguments and birthday.py script accordingly
        # 'Add' --to add a member to the list
        # 'Delete' --to delete a member from the existing list
        # 'Run'  --to run the script with existing list
        # No command line arguments will call the runScript function with existing list
    """

    # If command line argument is Run or No argv is provided call runScript function
    if len(sys.argv) < 2 or sys.argv[1] == 'Run':
        runScript()

    # If command line argument is Add call add function from sendEmail Class
    elif sys.argv[1] == 'Add':
        name = input("Enter the member name: ")  # Get the input
        email = input("Enter the member gmail ID: ")  # Get the input only Gmail host accepted
        dob = input("Enter the birthday dd-mm: ")  # Get the input in dd-mm format
        sendEmail.add_user(name, email, dob)

    # If command line argument is Delete call delete function from sendEmail Class
    elif sys.argv[1] == 'Delete':
        name = input("Enter the member name: ")  # Get the input
        sendEmail.delete_user(name)

def runScript():
    """This Function calls functions from sendEmail class to form the birthday list
            and email list of the members  send emails to members whose birthday fall on the current date
               it loops through the today_birthdays list and calls send_email function from sendEmail class
                  and by providing toAddress, fromAddress and name of the member to send birthday wishes to
                     individual members in the list.
    """
    now = datetime.datetime.now()
    currentDate = now.strftime("%d-%m") # Day and month as a zero-padded decimal number
    birthdays = sendEmail.birthday_list()
    toEmail = sendEmail.email_list()
    today_birthdays = birthdays.get(currentDate)

    if today_birthdays:

        for index, word in enumerate(today_birthdays):

            if word in toEmail:
                toEmailAddress = toEmail[word]
            sendEmail.send_email('kyashiri@gmail.com', toEmailAddress, word)
    else:
        print "No Birthday today"

if __name__ == '__main__':
    main()