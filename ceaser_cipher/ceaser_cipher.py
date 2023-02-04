# import math

# def area(height, width):
#     area = (height * width) / 5
#     print(f"You will need {math.ceil(area)} cans of paint")


# area(height = 3, width = 9)

#! def is_prime(number):

#     is_prime = True

#     if (number < 2):
#         is_prime = False
#     else:
#         for x in range(2, number):
#             if number % x == 0:
#                 is_prime = False
#     if (is_prime):
#         print(f"{number} is prime number")
#     else:
#         print(f"{number} is not prime number")

# is_prime(number= 109)

from ceaser_cipher_logo import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text, shift):
    code = ""
    for char in text:

        if char in alphabet:
            char_position = alphabet.index(char)
            if direction == "encode":
                coded_position = shift + char_position
            else:
                coded_position = char_position - shift
            code += alphabet[coded_position]
        else:
            code += char
    print(f"This is the encoded text: {code}")

should_continue = True
while should_continue:
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift > len(alphabet):
        shift = shift % len(alphabet)

    caesar(text, shift)
    replay = input("Type 'yes' to continue or 'no' to stop")
    if replay == 'yes':
        should_continue = True
    else:
        should_continue = False
        print("Good-bye!!\nThanks for using our service")
    
