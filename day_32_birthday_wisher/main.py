##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
import pandas

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {
    (row["month"], row["day"]): row for (index, row) in data.iterrows()
}

# HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
import datetime as dt

today_day = dt.datetime.now().day
today_month = dt.datetime.now().month

with open("letter_templates/letter_2.txt", "r") as file:
    the_letter = file.read()

if (today_month, today_day) in birthdays_dict:
    print("You can send the email now.")
    name = birthdays_dict[(today_month, today_day)]["name"]
    the_letter = the_letter.replace("[NAME]", name)
    print(the_letter)
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
