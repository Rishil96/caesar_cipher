# Project 6
# Caesar Cipher
from art import logo

# list of alphabets
alphabet = ['#', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# greet user
print(logo)


# encryption function
def encrypt(plain_text, shift_by):
    encoded_text = ""
    for letter in plain_text:
        if letter in alphabet:
            new_position = alphabet.index(letter) + shift_by
            if new_position > 26:
                new_position -= 26
            encoded_text += alphabet[new_position]
        else:
            encoded_text += letter
    return encoded_text


# decrypt function
def decrypt(plain_text, shift_by):
    decoded_text = ""
    for letter in plain_text:
        if letter in alphabet:
            new_position = alphabet.index(letter) - shift_by
            if new_position < 1:
                new_position += 26
            decoded_text += alphabet[new_position]
        else:
            decoded_text += letter
    return decoded_text


# Loop the code
while True:
    # get operation from user
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt.\n")

    # get text from user
    text = input("Type your message:\n").lower()

    # get shift number
    shift = int(input("Enter shift number: "))

    # encode/decode condition
    final_message = ""

    if direction == "encode":
        final_message = encrypt(text, shift)
    elif direction == "decode":
        final_message = decrypt(text, shift)
    else:
        print("Invalid operation. Try again.")

    if len(final_message) > 0:
        print(f"The {direction}d message is: {final_message}")

    go_again = input("Type 'yes' to go again otherwise type 'no'.")
    if go_again == 'yes':
        pass
    else:
        break
