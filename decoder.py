import morse_translator

message = '1110111000100010111010001011101000111010111011100000001110101110100010101010001011101000101000101010001110001110111000101110001010100000000111010100010111000111010100011101011101011101110'

def decoder(message):
	message_list = []
	space = 0
	message = list(message)
	char_fin = False
	char_stor = []
	for char in message:
		if char == '1':
			char_stor.append(char)
			if space == 2:
				message_list.append(' ')
			space = 0
		elif char == '0':
			if len(char_stor) == 0:
				space += 1
			else:
				char_stor.append(char)
				char_fin = True
		if space == 6:
			message_list.append(' / ')
			space = 0
		if char_fin:
			message_list.append(''.join(char_stor))
			char_fin = False
			char_stor = []
	for letter in range(len(message_list)):
		if message_list[letter] == '10':
			message_list[letter] = '.'
		elif message_list[letter] == '1110':
			message_list[letter] = '-'
	final_message = ''.join(message_list)
	return final_message


print(morse_translator.translator(decoder(message)))
