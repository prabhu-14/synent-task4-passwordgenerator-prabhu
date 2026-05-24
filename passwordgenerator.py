import random
import string

print("\nPASSWORD GENERATOR")


length = int(input("Enter password length: "))

if length < 8:
    print("Please keep a strong password with at least 8 characters.\n")
else:
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    numbers = string.digits
    special_characters = string.punctuation

    all_characters = (
        uppercase +
        lowercase +
        numbers +
        special_characters
    )

    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(numbers),
        random.choice(special_characters)
    ]

    for _ in range(length - 4):
        password.append(random.choice(all_characters))

    random.shuffle(password)

    final_password = "".join(password)

    print("Strong Random Password:", final_password,"\n")