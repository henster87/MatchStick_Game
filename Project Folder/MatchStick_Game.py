print("The point of this game is to not be the one to remove the last match!\nYou may remove a 1 to 3 matches each turn.\n\nGood luck!")
print("\n-------------------------\n")

while True:
	while True:
		try:
			matches = int(input("How many matches do you want to play with?: "))
			if matches >= 6:
				break
			else:
				print("Has to be bigger or equal to 6. ")
		except:
			print("Has to be a number! Try again. ")
		
	choice = ["1", "2", "3"]
	p= 1
	print("\nPlayer 1's turn: ")
	
	
	while matches > 0:
		
		player = None
		#print("p num:", p)
		if p % 2 == 0 and p > 1 and matches > 1:
			print("Player", ((p % 2)+2),"'s turn:")
		elif p % 2 != 0 and p > 1 and matches > 1:
			print("Player", ((p % 2)),"'s turn:")
		
		if matches == 1:
			matches = -1
			
		elif matches == 2:
			while True:
				player = input("Remove 1 or 2 matches? ")
				if player == choice[0] or player == choice[1]:
					break
			player = int(player)
			matches = matches - player
			if matches == 0 or matches == 2:
				print(matches, "matches left")
			else:
				print(matches, "match left")
			print()
			
		elif matches >= 3:
			while player not in choice:
				player = input("Remove 1, 2 or 3 matches? ")
			player = int(player)
			if player >= 1 and player <= 3:
				matches = matches - player
				if matches == 0 or matches > 1:
					print(matches, "matches left")
				else:
					print(matches, "match left")
			print()
			
		p +=1
		
	print("Game Over. Player " + str(((p % 2)+1)) + " lost! \n")
	print("\n-------------------------\n")
