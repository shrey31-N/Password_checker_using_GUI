def password_checker(password):
    result = {}
    """this function checkes the password length"""
    if len(password) >= 7:
        result["length_of_password"] = True
    else:
        result["length_of_password"] = False

    num = False
    caps = False
    special = False
    for number in password:
        if number.isdigit():
            num = True

    for letter in password:
        if letter.isupper():
            caps = True
    for special_character in password:
        if special_character in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/\\`~":
            special = True

    result["has_special_character"] = special
    result["has_number"] = num
    result["has_capital_letter"] = caps

    if all(result.values()) == True:
        return "Strong"
    else:
        return "Week"
