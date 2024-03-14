def password_checker():
    common_passwords = ['password', '123456', 'qwerty', 'abc123', 'letmein', 'monkey', 'football', 'iloveyou', 'admin']

    user_password = input("Enter your password: ")

    if user_password in common_passwords:
        print(f"Use a safer password {user_password} is compromised")
    else:
        print("Password is safe")

password_checker()
