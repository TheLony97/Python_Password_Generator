import string
import random 


def generate_password(nchar: int) -> str:

	password: str = "" 
	for e in range(nchar):
		password = password +  str(random.randint(1,nchar))
	return password

password = generate_password(8)
print(password)