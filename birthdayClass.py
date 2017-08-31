# !/usr/bin/env python3

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
                            example: 26-August BOB,GARRY
                                     2-July DAN

    email_list.txt -- to store name and email related values
                            example: BOB bob@gmail.com
                                     GARRY garry@gmail.com

 In this program we will be working with Gmail host alone and dob in dd-mm pattern (example 26-03)
'''

import smtplib
import urllib
import sys

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Environment

class birthdayEmail():

    def add_user(self,name, email, dob):
        """This Function adds a member details to the list and updates the respective text files
            birthday_list.txt and email_list.txt

              Arguments:
              - `name`: Name of the member whose reference has to be added to the list
              - `email`: Email of the member whose reference has to be added to the list
              - `dob`: Date of birth of the member whose reference has to be added to the list
        """
        if len(name) > 0 and len(dob) > 0 and '@gmail.com' in email:
            dob_object = open('birthday_list.txt', 'a')
            email_object = open('email_list.txt', 'a')
            my_dob_string =  dob + "  " +name
            my_email_string = name + "  "+ email
            addLine = True # boolean value to keep track whether to add a line or append to existing line
            with open('birthday_list.txt', 'r') as file:
                # read a list of lines into data
                data = file.readlines()
                for index,i in enumerate(data):
                    # Check if date already exists if yes append to the line change addLine to False
                    if dob in i:
                        i = i.rstrip('\n') + "," +name + '\n'
                        data[index] = i
                        addLine = False

            # If date does not exist add a new line to the files with member data
            if addLine == True:
                dob_object.write(my_dob_string + '\n')
            else:
                with open('birthday_list.txt', 'w') as file:
                    file.writelines(data)
            email_object.write(my_email_string+'\n')
            print("{} was successfully added to the list".format(name))
        else:
            print("Error occurred while adding Member to the list. Please check the values entered")

    def delete_user(self,name):
        """This Function deletes a member from the list and updates the respective text files 

                  Arguments:
                  - `name`: Name of the member whose reference has to be deleted from the list
        """
        # To delete in birthday_list.txt
        if len(name) > 0 and name in open('birthday_list.txt').read():
            with open('birthday_list.txt', 'r') as file:
                # read a list of lines into data
                data = file.readlines()
                for index,i in enumerate(data):
                    if name in i and ',' in i:
                        i = i.replace(name, '').replace(' ,',' ').replace(',,',',').rstrip(',\n')
                        data[index] = i+'\n'
                    elif name in i and ',' not in i:
                        data[index] = ""

            with open('birthday_list.txt', 'w') as file:
                file.writelines(data)
            file.close()

            # To delete in email_list.txt
            with open('email_list.txt', 'r') as file:
                # read a list of lines into emailListData
                emailListData = file.readlines()
                for index, i in enumerate(emailListData):
                    if name in i:
                        emailListData[index] = ""
            with open('email_list.txt', 'w') as file:
                file.writelines(emailListData)
            file.close()
            print("{} has been successfully deleted from the list".format(name))
        else:
            print("Error occurred while deleting Member from the list. Please check the value provided.")

    def birthday_list(self):
        """This Function will create list of Members names who's birthday fall in the current day
            It reads birthday_list.txt files and derives the list

             Arguments:
             - It takes no arguments
             Returns:
             - List of member names
        """
        with open("birthday_list.txt") as f:
            self.birthdays = {}
            for line in f:
                line = line.rstrip('\n').split("  ")
                if not line:  # empty line?
                    continue
                self.birthdays[line[0]] = line[1].split(",")
        return self.birthdays

    def email_list(self):
        """This Function will create list of email addresses to which email has to be sent
            It reads email_list.txt files and derives the list
            
             Arguments:
             - It takes no arguments
             Returns:
             - List of emails
        """
        with open("email_list.txt") as fp:
            self.emails = {}
            for line in fp:
                (key, val) = line.rstrip('\n').split('  ')
                self.emails[key] = val
        return self.emails

    def send_email(self, fromAddress, toAddress, name):
        """Function to send emails to members on their birthday

          Arguments:
          - `fromAddress`: Email Id from which the email will be sent
          - `toAddress`: Member email ID
          - `name`: Name of the member
        """
        From = fromAddress
        To = toAddress

        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Birthday Wishes"
        msg['From'] = From
        msg['To'] = To

        html = urllib.urlopen("template.html").read()
        TEMPLATE = html
        try:
            part = MIMEText(Environment().from_string(TEMPLATE).render(name=name), 'html')

            msg.attach(part)

            mail = smtplib.SMTP('smtp.gmail.com', 25) # Next step would be using corporate smtp host address.

            mail.ehlo()

            mail.starttls()

            mail.login('kyashiri@gmail.com', 'Shiri1215')
            mail.sendmail(From, To, msg.as_string())
            print("Birthday wishes delivery to {} --success".format(To))
            mail.quit()
        except Exception, exc:
            sys.exit("mail failed --Please check the email ID provided; %s" % str(exc))  # give a error message