# ceasar.py
# This will shift the message by a given number, key, or decode the ciphertext


def main():
    # get whether the user wants to decode or encode a message.
    s = input("Encode or Decode: ")
    s = s.lower()
    # check if encode or decode
    # if encode, call encode()
    if s == "encode":
        encode()
    # if decode, call decode()
    if s == "decode":
        decode()


def encode():
    # Get a message from the user to encode
    # Get a key value from the user to encode the message
    message = input("Enter a string you wish to encode: ")
    key = int(input("Enter a key value: "))

    # shift the message over the value of the key chr(ord(message))
    cipher = ""
    cipher_text = ""
    for m in message:
        if m.isalpha():
            cipher = ord(m) + key
            if cipher > ord('z'):
                cipher = cipher - (ord('z') + 1 - ord('a'))
            cipher_text += chr(cipher)

    # when the cipher reaches z, it should loop around and start again at a.
    # i.e. 122 = z and 97 = a.

    # print encoded message
    print(cipher_text)


def decode():
    # get ciphertext from user
    cipher = input("Enter the string you wish to decode: ")
    key = int(input("Enter the key used to encode: "))

    # get key used to encode message

    message = ""
    plaintext = ""
    # undo ciphertext
    for c in cipher:
        if c.isalpha():
            message = ord(c) - key
            if message < ord('a'):
                message = message - (ord('a') + 1 - ord('z'))
            plaintext += chr(message)

    # print plaintext message
    print(plaintext)

main()
"""
if __name__ == "__main__":
    main()
"""