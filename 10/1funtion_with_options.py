
f_name = input("What's your first name?")
l_name = input("What's your last name?")


def format_name(fname,lname):
    formal_name = str.title(fname)
    formal_surname = str.title(lname)
    return formal_name + ' ' + formal_surname


final_result = format_name(f_name,l_name)

print(final_result)