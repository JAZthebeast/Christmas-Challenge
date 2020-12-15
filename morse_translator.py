message = '-- . .-. .-. -.-- / -.-. .... .-. .. ... - -- .- ... / -.. .- -.. -.-.--'

morse_chars = {
			
			'.-' : 'A',
			'-...' : 'B',
			'-.-.' : 'C',
			'-..' : 'D',
			'.' : 'E',
			'..-.' : 'F',
			'--.' : 'G',
			'....' : 'H',
			'..' : 'I',
			'.---' : 'J',
			'-.-' : 'K',
			'.-..' : 'L',
			'--' : 'M',
			'-.' : 'N',
			'---' : 'O',
			'.--.' : 'P',
			'--.-' : 'Q',
			'.-.' : 'R',
			'...' : 'S',
			'-' : 'T',
			'..-' : 'U',
			'...-' : 'V',
			'.--' : 'W',
			'-..-' : 'X',
			'-.--' : 'Y',
			'--..' : 'Z',
			'.----' : '1',
			'..---' : '2',
			'...--' : '3',
			'....-' : '4',
			'.....' : '5',
			'-....' : '6',
			'--...' : '7',
			'---..' : '8',
			'----.' : '9',
			'-----' : '0',
			'--..--' : ', ',
			'.-.-.-' : '.', 
			'..--..' : '?',
			'-.-.--' : '!',
			'-..-.' : '/',
			'-....-' : '-', 
			'-.--.' : '(',
			'-.--.-' : ')'
			}

def translator(message):
	message = list(message)
	message.append(' ')
	letter = []
	final_message = []

	for char in message:
		if char != ' ':
			letter.append(char)

		else:
			for char in morse_chars:
				if char == ''.join(letter):
					final_message.append(morse_chars[char])
					break
			letter = []

		if char == '/':
				final_message.append(' ')

	return ''.join(final_message)
