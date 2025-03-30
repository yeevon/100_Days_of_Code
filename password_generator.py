import random

# Generates random upper / lower case letters
def get_letters(num_of_letters):
    letter_list = []

    while len(letter_list) < num_of_letters:
        rand_num = random.randint(0, 25)

        if random.random() < 0.5: # if number 0 - 0.4 Uppercase / 0.5 - 1.0 lowercase
            # Uppercase
            letter_list.append(chr(rand_num + 65))
        else:
            # Lowercase
            letter_list.append(chr(rand_num + 97))

    return letter_list

# Generate random symbols for password
def get_symbols(num):
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*",
               "(", ")", "[", "]", "}", "{", "<", ">",
               "?", "*", "-", "_"]

    return_sym = []

    while len(return_sym) < num:
        return_sym.append(random.choice(symbols))

    return return_sym


# Generate random numbers for password
def get_numbers(nums):
    num_list = []

    while len(num_list) < nums:
        num_list.append(str(random.randint(0, 9)))

    return num_list

print("Welcome to the pyPassword Generator!")

pw_list = get_letters(int(input("How many letters would you like in your password?\n")))
pw_list += get_symbols(int(input("How many symbols would you like?\n")))
pw_list += get_numbers(int(input("How many numbers would you like?\n")))

print(pw_list)
random.shuffle(pw_list) # Shuffle generated password
print(pw_list)
print("Your password is: " + "".join(pw_list))