def converter():
	while True:
		input1 = input("Enter the starting units>:")
		input2 = input("Enter destination units>:")
		input3 = float(input("Enter your value without spacing>:"))
		k1 = 1000000
		if input1 == "m3" and input2 == "cm3":
			answer = float(k1*input3)
			print( 'Your answer is: {} m^3'.format(round(answer))) 
		elif input1 == "DONE":
			break