"""This program will take user's password and check for Validaty"""

def password_validator(password):
	if (len(password) > 5 and len(password) < 15):
		
		lowercase = False
		uppercase = False
		num = False
		special = False
		for char in password:
			if (char.isdigit()):
				num = True
			if (char.lower()):
				lower_case = True
			if (char.upper()):
				upper_case = True
			if (not char.isalnum()):
				special = True
				
		return lower_case and upper_case and num and special
		
	else:
		return False




# user_password = "San$7849!"
user_password = input("Enter your password to check: ")
print(password_validator(user_password))