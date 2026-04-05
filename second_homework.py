#TASK1 - User logging
full_name = input("Enter your full name (first and last) separated by a space: ").strip()

if not full_name:
    print("Error: please enter a valid full name")
else:
    name_parts = full_name.split()

    if len(name_parts) >= 2:
        print(f"Initials: {name_parts[0][0]} {name_parts[1][0]}")
    else:
        print("Error: please enter a valid full name")

#TASK2 - Email masking
user_email = input("Enter your email: ").strip()

if not user_email:
    print("Error: please enter a valid email")
elif not user_email.endswith((".com", ".org")):
    print('Error: email must end with ".com" or ".org"!')
else:
    user_nickname, email_domain = user_email.split("@")
    if len(user_nickname) >= 2:
        masked_user_nickname = user_nickname[0] + "*" * (len(user_nickname) - 2) + user_nickname[-1]
        masked_user_email = masked_user_nickname + "@" + email_domain
        print(masked_user_email)
    else:
        print("Error: user's nickname part too short to mask")

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

#TASK4 - Tag analysis (set + union/intersection)
user1_tags = set()
user2_tags = set()

input1 = input("User 1 tags: ").strip()
input2 = input("User 2 tags: ").strip()

if not input1 or not input2:
    print("Error: please enter tags")
else:
    tags1 = [tag.strip() for tag in input1.split(",")]
    tags2 = [tag.strip() for tag in input2.split(",")]
    
    if len(tags1) != 3 or len(tags2) != 3:
        print("Error: please enter exactly 3 tags for each user")
    else:
        user1_tags.update(tags1)
        user2_tags.update(tags2)
        
        common_tags = user1_tags.intersection(user2_tags)
        all_unique_tags = user1_tags.union(user2_tags)
        
        print("Common:", common_tags)
        print("Unique:", all_unique_tags)

#TASK5 - Processing a string with numbers
user_input = input("Enter numbers separated by space: ").strip()

values = user_input.split()

if len(values) < 3:
    print("Error: please enter at least three numbers")
else:
    if values[0].isdigit() and values[1].isdigit() and values[2].isdigit():
        total = int(values[0]) + int(values[1]) + int(values[2])
        print("Sum of three numbers:", total)
    else:
        print("Error: one or more values are not numbers")