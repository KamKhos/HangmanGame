import os


first_game = "Yes"
mistakes = 0
list_of_spaces = []
list_of_spaces_and_letters = []

def word_space_string(word):
	emp_list = []
	for each_letter in word:
		emp_list.append("_")
	space_string = " ".join(emp_list)
	print(space_string)


def add_letter_to_list(word, space_list, letter_and_space_list, first_game, mistakes):		
	if first_game == "Yes":
		for x in word:
			space_list.append("_")
			letter_and_space_list.append("_")

	
	emp_list = []
	for each_letter in word:
		emp_list.append("_")
	show_letters_and_spaces = " ".join(emp_list)

	while mistakes < 6:
		letter = input("Player 2, enter a letter: ")
		
		i = 0
		while i < len(word):
			if letter == word[i]:
				letter_and_space_list[i] = letter
				show_letters_and_spaces = " ".join(letter_and_space_list)
				os.system("cls")
				draw_hangman(mistakes)
				print(show_letters_and_spaces)
			i = i + 1
		if letter_and_space_list == space_list:
			mistakes += 1
			os.system("cls")
			draw_hangman(mistakes)
			print(show_letters_and_spaces)
		else:
			space_list = letter_and_space_list[:]
		if "_" not in letter_and_space_list:
			print("You win") 
			break
		if mistakes == 6:
			print("Game over, you lose :(")
	
	
	
   
def draw_hangman(mistakes):
	if mistakes == 0:
		print("  ___")
		print("     |")
		print("     |")
		print("     |")
		print("     |")
		print("     |")
		print("     |")
	elif mistakes == 1:
		
		print("  ___")
		print("     |")
		print("  O  |")
		print("     |")
		print("     |")
		print("     |")
	elif mistakes == 2:
		
		print("  ___")
		print("     |")
		print("  O  |")
		print("  |  |")
		print("  |  |")
		print("     |")
	elif mistakes == 3:
		
		print("  ___")
		print("     |")
		print("  O  |")
		print("  |  |")
		print("  |  |")
		print("   \\ |")
		print("     |")
	elif mistakes == 4:
		
		print("  ___")
		print("     |")
		print("  O  |")
		print("  |  |")
		print("  |  |")
		print(" / \\ |")
		print("     |")
	elif mistakes == 5:
		
		print("  ___")
		print("     |")
		print("  O  |")
		print("  Y  |")
		print("  |  |")
		print(" / \\ |")
		print("     |")
	elif mistakes == 6:
		
		print("  ___")
		print("  |  |")
		print("  O  |")
		print("  Y  |")
		print("  |  |")
		print(" / \\ |")
		print("     |")



word = input("Player 1, pick the word: ")
os.system("cls")
draw_hangman(mistakes)
word_space_string(word)
add_letter_to_list(word, list_of_spaces, list_of_spaces_and_letters, first_game, mistakes)