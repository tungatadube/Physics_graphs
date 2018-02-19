def disemvowel(word):
	vowels = ["a", "e", "i", "o", "u"]
	new_word = ""
	for letter in word.lower():
		if letter not in vowels:
			new_word = new_word + letter
	
	return(new_word)
		
disemvowel("stringa")