"""Banking system - version 4
Question 3: Overdraft users (when the account balance is negative)
"""


class User:
    def __init__(self, first_name, last_name, gender, street_address, city,
                 email, cc_number, cc_type, balance, account_no):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.street_address = street_address
        self.city = city
        self.email = email
        self.cc_number = cc_number
        self.cc_type = cc_type
        self.balance = float(balance)
        self.account_no = account_no
        user_list.append(self)

    def display_info(self):
        print(border)
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Gender:", self.gender)
        print("Street address:", self.street_address)
        print("City:", self.city)
        print("Email:", self.email)
        print("CC Number:", self.cc_number)
        print("CC Type:", self.cc_type)
        print("Balance:", self.balance)
        print("Account Number:", self.account_no)


def generate_users():
    import csv
    with open('bankUsers.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',', quotechar="'")
        for line in filereader:
            User(line[0], line[1], line[2], line[3], line[4], line[5], line[6],
                 line[7], float(line[8]), line[9])


def find_user():
    not_found = "True"
    find_first = input("Enter the first name of the user: ").title()
    find_last = input("Enter the last name of the user: ").title()
    for user in user_list:
        if user.first_name == find_first and user.last_name == find_last:
            not_found = "False"
            user.display_info()
            print(border)
    if not_found == "True":
        print("ERROR! User does not exist")


def overdrafts():
    names_list = []
    total_users = 0  # number of overdraft users
    total_amount = 0  # amount of overdraft by these users
    for user in user_list:
        if user.balance < 0:
            overdraft_user = user.first_name + " " + user.last_name
            names_list.append(overdraft_user)
            total_users += 1
            total_amount += user.balance
    print("All users with overdraft accounts:")
    for name in names_list:
        print(name)
    print(border)
    print(f"Total number of overdraft users: {total_users}")
    print(f"Total amount of overdraft: ${total_amount:.2f}")
    print(border)


def missing_emails():
    names_list = []
    total_users = 0  # number of users without emails on their account
    for user in user_list:
        if user.email == "":
            user.display_info()
    print("All users with missing emails:")


def bank_details():
    # TO COMPLETE

    True


def transfer():
    # TO COMPLETE

    True


# Main Routine
user_list = []
border = "-" * 30

user_choice = ""
print("Welcome!")

generate_users()
while user_choice != "Q":
    print()
    print("What function would you like to run?")
    print("Type 1 to find a user")
    print("Type 2 to print overdraft information")
    print("Type 3 to print users with missing emails")
    print("Type 4 to print bank details")
    print("Type 5 to transfer money")
    print("Type Q to quit")
    user_choice = input("Enter choice: ").upper()
    print()

    if user_choice == "1":
        find_user()
    elif user_choice == "2":
        overdrafts()
    elif user_choice == "3":
        missing_emails()
    elif user_choice == "4":
        bank_details()
    elif user_choice == "5":
        transfer()

