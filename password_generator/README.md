Generate pseudo-randomic password according to requested length and complexity

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