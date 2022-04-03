import base64
from os import system


def encode_me(text):
    message_bytes = text.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message


def decode_me(base64_message):
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    return message

# hashed = encode_me("I am a password")
# print(hashed)
# decoded = decode_me(hashed)
# print(decoded)


while True:

    print("""
    type option the press enter
    d to Decode.
    e to Encode.
    x to exit.
    
""")

    inputOption = input("encode or decode?:: ")
    if inputOption in ['e', 'E']:
        inputString = input("String to be encoded:: ")
        encodedString = encode_me(inputString)
        system("cls")
        print(f"encoded string is: {encodedString}")
    
    elif inputOption in ['d',"D"]:
        inputStringD = input("String to be decoded:: ")
        encodedString = decode_me(inputStringD)
        system("cls")
        print(f"decoded string is: {encodedString}")

    elif inputOption in ['x', 'X', 'exit', 'ee']:
        break

    else:
        system("cls")
        print("Invalid option")

system("cls")
