from os import system
import random
import urllib.request

#Get a random word from an online wordlist
def getword():
	print("Fetching wordlist from http://www.mieliestronk.com/corncob_lowercase.txt...")
	url = 'http://www.mieliestronk.com/corncob_lowercase.txt'
	response = urllib.request.urlopen(url)
	data = response.read()
	wordList = data.decode('utf-8')
	wordFromList = wordList.split('\n')
	randomNumber = random.randint(0, len(wordFromList))
	word0 = wordFromList[randomNumber]
	word = word0.replace("\r", "")
	return word

#Hangman function
def hangMan():
	#initialise variables
	guesses = 0					
	word = getword()				
	word_list = list(word)	
	blanks = "_"*len(word)	
	blanks_list = list(blanks) 
	new_blanks_list = list(blanks)
	guess_list = []
	
	print ("Let's play hangman!")
	#this will give the player 10 incorrect guesses before the while loop breaks
	while guesses < 10:
		
		#This block will print some text and take input from the player
		print("Guesses left: " + str(10 - guesses))
		print ("" + ' '.join(blanks_list))
		print("\n")
		guess = str(input("> "))
		print("\n")
		guess = guess.lower()
		
		#make sure that the player inputs a singular letter
		if len(guess) > 1:
			print ("Stop cheating! Enter one letter at time.")
		elif guess == "":
			print ("Don't you want to play? Enter one letter at a time.")
		elif guess in guess_list:
			print ("You already guessed that letter! Here is what you've guessed:")
			print (' '.join(guess_list))
		#if the user inputs a single letter, find out if it is correct
		else:
			#check each letter individualy
			guess_list.append(guess)
			for i in range(len(word)):
				if guess == word[i]:
					new_blanks_list[i] = word_list[i]

			#If the letter is wrong, increase guesses and print text
			if new_blanks_list == blanks_list:
				guesses = guesses + 1
				if guesses < 9:
					print ("Your letter isn't here.")
					print ("Guess again.")

			#If the guess is correct run this
			elif word_list != blanks_list:
						
				blanks_list = new_blanks_list[:]
				
				#If the word is fully revealed, do this
				if word_list == blanks_list:
					print ("\nYOU WIN! Here is your prize:\n")
					again = input("Would you like to play again? (y/n): ")
					if again.lower() == "y":
						hangMan()
					elif again.lower() == "n":
						quit()
				#else if the word isn't, tell the player and let them input another
				else:
					print ("Great guess! Guess another!")
	#Tell the player the word and ask if they want to play again
	print("Damn, you lost. The word was: " + word)
	again = input("Would you like to play again? (y/n): ")
	if again.lower() == "n":
		quit()
	else:
		hangMan()

hangMan()




