#TASK1 - User logging
full_name = input("Enter your full name (first and last) separated by a space: ")
separated_full_name = []

#Check for empty or whitespace-only
if not full_name.strip(): #strip removes extra spaces
    print("Error: please enter a valid full name")
else:
    separated_full_name = full_name.split() #split used for string separation
#print(separated_full_name)

if separated_full_name:
    if len(separated_full_name) >= 2:
        print(f"Initials: {separated_full_name[0][0]} {separated_full_name[1][0]} ")
    else:
        print("Error: please enter a valid full name")

#TASK2 - Email masking
user_email = input("Enter your email: ").strip()

if not user_email:
    print("Error: please enter a valid email")
else:
    if user_email[-3:] == "com" or user_email[-3:] == "org":
        user_nickname, email_domain = user_email.split("@")
        #print(user_nickname,email_domain)
        if len(user_nickname) >= 2:
            masked_user_nickname = user_nickname[0] + "*" * (len(user_nickname)-2) + user_nickname[-1]
            masked_user_email = masked_user_nickname + "@" + email_domain
            print(masked_user_email)
        else:
            print("Error: user's nickname part too short to mask")
    else:
        print('Error: email must end with "com" or "org"!')

#TASK3 - Adding a unique value
registered_values = [1, 2, 3, 4, 5]

unique_values = set(registered_values)

new_number = int(input("Which number would you like to add? "))
print("Current list:", registered_values)

if new_number in unique_values:
    print("This number already exists, the list remains unchanged:", registered_values)
else:
    registered_values.append(new_number)
    unique_values.add(new_number)
    print("The list has been updated:", registered_values)