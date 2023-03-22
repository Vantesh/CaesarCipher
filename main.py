from symbols import characters, logo
print(logo)
while True:
  direction= input("Type 'encode' to encrypt or 'decode' to decrypt:  ").lower()

  text=input("Type Your message:\n\n").lower()

  shift=int(input("Type the shift number:\n"))

  def encrypt(plain_text, shift_amount, direction):
    cipher_text=""
    if direction == 'decode':
      shift_amount*=-1
    for char in plain_text:
      if char in characters:
        position=characters.index(char)
        new_position=position+shift_amount
        new_char=characters[new_position]
        cipher_text+=new_char
      else:
        cipher_text+=char
    print(f"The {direction}d message is {cipher_text}\n")
  encrypt(plain_text=text , shift_amount=shift, direction=direction)
  retry = input("retry ? (y/n): ")
  
  if retry.lower() != "y":
    break