import logging

logger = logging.getLogger(__name__)


def login():
    logger.info("Login")
    username = input("Enter your username: ")
    logger.debug("Username entered")
    password = input("Enter your password: ")
    logger.debug("Password entered")
    return username, password
    

def main():
    login()

if __name__ == "__main__":
    main()