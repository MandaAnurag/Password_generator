def password(): #creating a password generating function 

    """This is a password generator"""

    store = [] #It will contain passwords

    char_length = random.randrange(2,5)

    for i in range(char_length):# using string module to generate the password

        cap = random.choice(string.ascii_uppercase)

        store += cap

        small = random.choice(string.ascii_lowercase)

        store += small

        digit = random.choice(string.digits)

        store += digit

        punct = random.choice(string.punctuation)

        store += punct

    random.shuffle(store)# Shuffling it

    random.shuffle(store)# Shuffling it again 

    word = "".join(store) #Making the password a string

    return word
