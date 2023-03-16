alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction= input("Type 'encode' to encrypt or 'decode' to decrypt:  ").lower()

text=input("Type Your message:\n\n").lower()

shift=int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
  cipher_text=""
  for letter in plain_text:
    position=alphabet.index(letter)
    new_position=position+shift_amount
    new_letter=alphabet[new_position]
    cipher_text+=new_letter
  print(f"The encrypted message is {cipher_text}")



def decrypt(plain_text, shift_amount):
  cipher_text=""
  for letter in plain_text:
    position=alphabet.index(letter)
    new_position=position-shift_amount
    new_letter=alphabet[new_position]
    cipher_text+=new_letter
  print(f"The decrypted message is {cipher_text}")
  


if direction == 'encode':
  encrypt(plain_text=text , shift_amount=shift)
elif direction== 'decode':
  decrypt(plain_text=text , shift_amount=shift)

