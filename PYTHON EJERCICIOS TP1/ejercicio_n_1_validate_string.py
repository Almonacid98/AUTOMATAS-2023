def validate_string(string):
    conditions = [
        any(char.isalnum() for char in string),
        any(char.isalpha() for char in string),
        any(char.isupper() for char in string),
        any(char.islower() for char in string),
        any(char.isdigit() for char in string),
        len(string) >= 8
    ]
    return print(conditions)

argument = input("Enter an argument: ")
validate_string(argument)