import random
import array
MAX_LEN = 12
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
					'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
					'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
					'z']

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
					'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
					'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
					'Z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
		'*', '(', ')', '<']
LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
digit = random.choice(DIGITS)
upper = random.choice(UPCASE_CHARACTERS)
lower = random.choice(LOCASE_CHARACTERS)
symbol = random.choice(SYMBOLS)
temp_pass = digit + upper + lower + symbol
for x in range(MAX_LEN - 4):
	temp_pass = temp_pass + random.choice(LIST)
	temp_pass_list = array.array('u', temp_pass)
	random.shuffle(temp_pass_list)
password = ""
for x in temp_pass_list:
		password = password + x
print("Your password is",password)
