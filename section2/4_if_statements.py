my_known_people = ["John", "Rolf", "Anne"]
user_name = input("Enter your name: ")
if user_name in my_known_people:
    print("Hello, I know you!")


if user_name in my_known_people:
    print(f"Hello {user_name}, I know you!")


if user_name in my_known_people:
    print("Hello {name}, I know you!".format(name=user_name))

"Hello {name}, I know you {}!".format("well", name=user_name)
'Hello John, I know you well!'

#### Exercise

def who_do_you_know():
    names = input("Enter the names of people you know, separated by commas: ")
    return names.split(",")

def ask_user():
    # Ask user for their name
    # See if their name is in list of people
    # Print something if it is

    user_name = input("Enter your name: ")
    if user_name in who_do_you_know():
        print(f"Hello {user_name}, I know you!")
