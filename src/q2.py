"""
Please implement this stub function to match the documentation.
Make sure to implement tests in the tests directory.
"""

import sys
sys.path.append('.')
from src.q1 import validate_password

def set_password() -> None:
    """
    1. Ask the user to input a password
    2. If it is not valid, print the 
       requirements which are not met and go back to step 1.
       (Keep repeating until password is valid)
    """
    print("Please create a strong password.")
    print("Requirements: at least 8 characters, 1 uppercase, 1 lowercase, 1 digit, 1 special character (!@#$%^&*)\n")
    
    while True:
        password = input("Enter your password: ")
        
        if validate_password(password):
            print("\nPassword set successfully!")
            break
        else:
            # validate_password() already printed what went wrong
            print("\nPlease try again with a stronger password.\n")
