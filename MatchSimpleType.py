some_var = "not a float"

match some_var:
    case float:  # Wrong! - matches any subject, because Python sees float as a variable
        print(f"'{some_var}' is float")

some_var = 3.14

match some_var:
    case float():  # Correct!
        print(f"{some_var} is float")

int_var: int = 1

match int_var:
    case int():
        print(f"{int_var} is int")