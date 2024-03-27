alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def shift_text(user_text, user_shift):
    shifted_index = 0
    encrypted_text = ""
    for char in user_text:
        if char == " ":
            encrypted_text += " "
            continue
        char_index = alphabet.index(char)  # the index of the character in the alphabet array
        if direction == "encode":
            shifted_index = char_index + user_shift
        elif direction == "decode":
            shifted_index = char_index - user_shift
        if shifted_index > 26:
            shifted_index %= 26
        encrypted_text += alphabet[shifted_index]
    return encrypted_text


print(shift_text(text, shift))
