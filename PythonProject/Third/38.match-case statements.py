# Match case statment (switch) : An alternative to using many 'elif' statments 
#                                Excute some code if a value matches a 'case' 
#                                Benefits: cleaner and syntax is more readable

def is_weekend(day):
    match day:
        case "Saturday" | "sunday":
            return True
        case "Monday" | "Tusday" |"Wednesday" | "Thursday" | "Friday":
            return False

print(is_weekend("Friday"))  