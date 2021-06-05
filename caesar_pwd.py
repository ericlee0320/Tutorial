alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
			'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 
			'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
			'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from caesar_art import logo			
print(logo)


# def encrypt(input_text=text,shft_amount=shift):
	# cipher_text=""
	# for letter in input_text:
		# position = alphabet.index(letter)
		# new_position = position + shft_amount
		# new_letter = alphabet[new_position]	
		# cipher_text += new_letter
	# print(f"The encode text is {cipher_text}")
		

# def decrypt(cipher_text=text,shft_amount=shift):
	# original_text=""
	# for letter in cipher_text:
		# position = alphabet.index(letter)
		# new_position = position - shft_amount
		# new_letter = alphabet[new_position]	
		# original_text += new_letter
	# print(f"The decode text is {original_text}")

	
def caesar(input_text,shift_amount,cipher_direction):

	ouput_text=""
	
	if cipher_direction == 'd' or cipher_direction == 'decode':	
		shift_amount *= -1
	# for letter in input_text:
		# position = alphabet.index(letter)		
		# new_position = position + shift_amount
		# new_letter = alphabet[new_position]	
		# ouput_text += new_letter
	# print(f"The end text is {ouput_text}")	
	
	for char in input_text:
		if char in alphabet:
			position = alphabet.index(char)		
			new_position = position + shift_amount
			new_letter = alphabet[new_position]		
			ouput_text += new_letter
		else:
			ouput_text += char
	print(f"The end text is {ouput_text}")	
	
is_exit = False
while not is_exit:
	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
	text = input("Type your message:\n").lower()
	shift = int(input("Type the shift number:\n"))
	shift = shift % 26
	caesar(input_text=text,shift_amount=shift,cipher_direction=direction)
	
	
	ask_user=input("Do you want to continue? (yes,no)").lower()
	if ask_user == "no" or ask_user == "n":
		print("Goodbye")
		is_exit = True
		
		


#encrypt(text,shift)
#decrypt(text,shift)