alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(user_text, user_shift):
    encrypted_text = ""
    for char in user_text:
        if char == " ":
            encrypted_text += " "
            continue
        char_index = alphabet.index(char)  # the index of the character in the alphabet array
        shifted_index = char_index + user_shift  # the new index after applying the cypher
        if shifted_index > 26:
            shifted_index = (char_index + user_shift) % 26
        encrypted_text += alphabet[shifted_index]
    return encrypted_text


def decrypt(user_text, user_shift):
    decrypted_text = ""
    for char in user_text:
        if char == " ":
            decrypted_text += " "
            continue
        char_index = alphabet.index(char)  # the index of the character in the alphabet array
        shifted_index = char_index - user_shift  # the new index after applying the cypher
        if shifted_index > 26:
            shifted_index = (char_index - user_shift) % 26
        decrypted_text += alphabet[shifted_index]
    return decrypted_text


if direction == "encode":
    encoded_text = (encrypt(text, shift))
    print(encoded_text)
else:
    decoded_text = decrypt(text, shift)
    print(decoded_text)
    # print(f"There's no {direction} function.")

# TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount
#  and print the encrypted text. e.g. plain_text = "hello" shift = 5 cipher_text = "mjqqt" print output: "The encoded
#  text is mjqqt"

##HINT: How do you get the index of an item in a list:
# https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

# TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
