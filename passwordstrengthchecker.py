import re

#conds to check for (min 8 chars, digits, chars{upper, lower}, special chars)
def check_password_strength(password):
    if len(password) < 8: 
        return "Weak: Password must be atleast of 8 characters"
    if not any (char.isdigit() for char in password):
        return "Weak: Password must contain a digit" #why use not,why not only if
    if not any (char.isupper() for char in password):
        return "Weak: Password must contain an upper character"
    if not any (char.islower() for char in password):
        return "Weak: Password must contain an lower character"
    if not re.search(r'[!@#$%^&*()-+]', password):
        return "Medium: Password must contain a special character"
    return "Strong: Your password is secured!"

def password_checker():
    print("Welcome to the Password Strength Checker!")

    while True:
        password = input("Enter your password (or type 'exit' to quit): ")

        if password.lower() == 'exit':
            print("Exiting the Password Strength Checker. Stay safe!")
            break

        result = check_password_strength(password)
        print(result)

#Run the password checker tool
if __name__ == "__main__":
    password_checker()