import string
import random 


def generate_password(nchar: int, text=True, shuffle=True) -> str:

	password: str = ""

	for e in range(nchar):
		password = password +  str(random.randint(1,nchar))

	if text == True:
		chars: list = [] 
		for e in range(5):
			chars.append(random.choice(string.ascii_lowercase))
		password = password + "".join(chars)

	if shuffle == True:
		new_password: str = ""
		for x in range(len(password)):
			new_password += random.choice(password)
		password = new_password

	return password

password = generate_password(8,True,True)
print(password)

