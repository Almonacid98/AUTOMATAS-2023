def validate_string(str_in):
    str_long = 0
    long_output = False    
    val_alnum = any(x.isalnum() for x in str_in)
    val_alpha = any(x.isalpha() for x in str_in)
    val_upper = any(x.isupper() for x in str_in)
    val_low = any(x.islower() for x in str_in)
    val_digit = any(x.isdigit() for x in str_in)
    str_long = len(str_in)
    if str_long >= 8:
        long_output = True
    else:
        long_output = False
    print(val_alnum)
    print(val_alpha)
    print(val_upper)
    print(val_low)
    print(val_digit)
    print(long_output)
str_argument = input("Enter an argument: ")
validate_string(str_argument)