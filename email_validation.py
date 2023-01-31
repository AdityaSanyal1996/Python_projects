email = input("Enter your mail: ")
k, j, d = 0, 0, 0
if len(email) <= 30:        # adityasanyal1996@gmail.com
	if email[0].isalpha():
		if "@" in (email) and (email.count("@") == 1):
			if (email[-4] == ".") ^ (email[-3] == "."):
				for i in email:
					if i == i.isspace():
						k = 1
						break
					elif i.isalpha():
						if i == i.upper():
							j = 1
							break
						else:
							continue	
					elif i in ['0','1','2','3','4','5','6','7','8','9']:
						continue
					elif i == "_" or i == "." or i == "@":
						continue
					else:
						d = 1			
						print("wrong position 3")
						break	
				if (k == 1) or (j == 1) or (d == 1):
					print("Wrong Email 5")
				else:
					print("Email is accepted")				
			else:
				print("Wrong Email 4")
		else:
			print("Wrong Email 3")		
	else:
		print("Wrong Email 2")	
else:
	print("Wrong Email 1")


