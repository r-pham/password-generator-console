from string import ascii_lowercase, ascii_uppercase, punctuation, digits

def gen_pw(
	length: int, 
	use_capital: bool = True, 
	use_digits: bool = True, 
	use_symbols: bool = True
) -> str:
	password = ''
	choices = [ascii_lowercase]

	if use_capital:
		choices.append(ascii_uppercase)
	if use_digits:
		choices.append(punctuation)
	if use_symbols:
		choices.append(digits)
		
	for i in range(length):
		password += random.choice(random.choice(choices))
	return password