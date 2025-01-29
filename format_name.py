def format_name():
    """
    take a first and last name, and format them
    """
    while True :
        f_name = input("What's your first name: ").strip()
        l_name = input("Type your last name: ").strip()
        if f_name == "" or l_name == "":
            print("You did not provide valid input")
            continue
        formated_f_name = f_name.title()
        formated_l_name = l_name.title()

        return f"{formated_f_name} {formated_l_name}"

print(format_name())

