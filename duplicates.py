def duplacates():
	words_list = []

	word = input("Enter a word (enter quit to quit): ")

	while word != "quit":
		if word not in words_list:
			words_list.append(word)
		word = input("Enter a word (enter quit to quit): ")
	
	if word == "quit":
		for word in words_list:
			print(word)


duplacates()