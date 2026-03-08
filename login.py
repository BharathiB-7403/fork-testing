def login():
    print("Login")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    return username, password

def main():
    login()

if __name__ == "__main__":
    main()