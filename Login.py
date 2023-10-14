def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Hardcoded username and password (for demonstration purposes)
    correct_username = "username"
    correct_password = "password"

    if username == correct_username and password == correct_password:
        print("Login successful!")
    else:
        print("Invalid username or password. Please try again.")

# Call the login function
login()
