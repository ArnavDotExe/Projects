alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amt):
    cipher_text = ""
    for letter in plain_text:
        pos = alphabet.index(letter)
        new_pos = pos + shift_amt
        new_letter = alphabet[new_pos]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")


# encrypt(plain_text=text, shift_amt=shift)


def decrypt(cipher_text, shift_amt):
    decrypt_txt = ""
    for letter in cipher_text:
        pos = alphabet.index(letter)
        new_pos = pos - shift_amt
        new_letter = alphabet[new_pos]
        decrypt_txt += new_letter
    print(f"The decoded text is {decrypt_txt}")


# decrypt(cipher_text=text,shift_amt=shift)

if direction == "encode":
    encrypt(plain_text=text, shift_amt=shift)
elif direction == "decrypt":
    decrypt(cipher_text=text, shift_amt=shift)
