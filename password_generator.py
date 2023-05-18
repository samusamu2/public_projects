import random
import string


# array of arrays of possible characters for password generation
characters = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]


def generate_passw(length: int, complexity: int):
    """Generate pseudo-randomic password according to requested length and complexity

    Parameters
    ----------
    length : int
        Length of the password
    complexity : int
        Represents the requested complexity of the password:
        | 1. only lower-case letters
        | 2. lower and upper-case letters
        | 3. letters and numbers
        | 4. letters, numbers and symbols

    Returns
    -------
    str
        The generated password
    """

    # picks the feasible characters according to requested complexity
    usable = ""
    for i in range(complexity):
        usable += characters[i]

    password = ""
    for i in range(length):
        password += random.choice(usable)

    return password


length = input("Insert password length: ")
while True:
    # checks that the input corresponds to an integer
    try:
        length = int(length)
        break
    except ValueError:
        length = input("Please insert a integer number: ")


print()
print("Choose the complexity you prefer \n1. Lower-case letters \n2. Lower and upper-case letters "
      "\n3. Letters and numbers \n4. Letters, numbers and symbols")
complexity = input("Write the number corresponding to the desired option: ")
while True:
    # checks that the input corresponds to an integer between 0 and 4
    try:
        complexity = int(complexity)
        if 1 <= complexity <= 4:
            break
        raise KeyError
    except (ValueError, KeyError):
        complexity = input("Please insert a integer number between 1 and 4: ")


res = generate_passw(length, complexity)
print()
print(f"Here's your password: {res}")
