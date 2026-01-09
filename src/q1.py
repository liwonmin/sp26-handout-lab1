"""
Please implement these stub functions to match the documentation.
Make sure to implement tests in the tests directory.
"""


def validate_password(password: str) -> bool:
    """Determines whether a password meets the requirements. If any requirements
    are not met, prints which requirements were not met.

    Requirements:
    1. Password must be at least 8 characters long
    2. Password must contain at least one uppercase letter
    3. Password must contain at least one lowercase letter
    4. Password must contain at least one digit
    5. Password must contain at least one special character (!@#$%^&*)

    
    Parameters
    ----------
    password : str
        The password to validate
    
    Returns
    -------
    bool
        True if the password is valid, and false otherwise
    """

    is_long_enough = len(password) >= 8
    has_uppercase = any(c.isupper() for c in password)
    has_lowercase = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in '!@#$%^&*' for c in password)
    
    # Print which requirements are not met
    if not is_long_enough:
        print("Password must be at least 8 characters long")
    if not has_uppercase:
        print("Password must contain at least one uppercase letter")
    if not has_lowercase:
        print("Password must contain at least one lowercase letter")
    if not has_digit:
        print("Password must contain at least one digit")
    if not has_special:
        print("Password must contain at least one special character (!@#$%^&*)")
    
    # Return True only if all requirements are met
    return is_long_enough and has_uppercase and has_lowercase and has_digit and has_special


    pass
