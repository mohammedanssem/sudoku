import random
import string
import csv
#__________________4x4
def generate_4x4_game():

	#__generate random row / shuffle overwrites exsiting list
	first_row = [str(number) for number in range(1,5)]
	random.shuffle(first_row)

	#__generates secound row by slicing first row into two parts
	secound_row_p1 = first_row[:2]
	secound_row_p2 = first_row[2:]
	#__and revering the
	secound_row_p1 = list(reversed(secound_row_p1))
	secound_row_p2 = list(reversed(secound_row_p2))
	#__puzzel them togeter
	secound_row = secound_row_p2 + secound_row_p1

	#__generates third row
	third_row_p1 = list(reversed(secound_row[:2]))
	third_row_p2 = list(reversed(secound_row[2:]))
	third_row = third_row_p1 + third_row_p2

	#__generates forth_row
	forth_row_p1 = list(reversed(first_row[:2]))
	forth_row_p2 = list(reversed(first_row[2:]))
	forth_row = forth_row_p1 + forth_row_p2

	#__swap third and fourth row at random
	states = ["TRUE","FALSE"]
	random_state = random.choice(states)
	if random_state == "TRUE":
		row = forth_row
		forth_row = third_row
		third_row = row


	#___print rows
	print(first_row)
	print(secound_row)
	print(third_row)
	print(forth_row)

	#_____________________generate list for savefile

	start_game_savefile_lst = []
	#__creates a list with 4 x "TRUE" in it > to set all numbers in a row visible
	visibility = ["TRUE" for x in range(4)]
	#___create a upper case list containing all letters of the alphabet
	column_alphabet_lst = list(string.ascii_uppercase)
	#___slice alphabet list (letter amount == amount of rows)
	column_lst = column_alphabet_lst[:4]
	row_lst = [first_row,secound_row,third_row,forth_row]
	for index in range(0,4):
		new_row = [column_lst[index]] + (row_lst[index])
		start_game_savefile_lst.append(new_row)
		new_row = [column_lst[index] + "_v"] + (visibility)
		start_game_savefile_lst.append(new_row)

	print(start_game_savefile_lst)

	return start_game_savefile_lst

#_______________________________GENERATE difficulty
def add_difficulty(orginal_field,minimum = 6,maximum = 7,row_size = 4,false_count = 0):

	difficulty_field = orginal_field
	states = ["TRUE","FALSE"]

	#___get and return an random number beween 2 and row size (4,9,16) for random indexing
	def get_random_position(row_size):
		position = random.choice(range(2,(row_size +1)))
		return position
	#___base case 01 > if 6 FALSE are in the list, return it
	if false_count == minimum:
		return difficulty_field

	else:
		for row in orginal_field:
			#__get random index number
			position = get_random_position(row_size)
			#__if item on this posion is "TRUE"
			if row[position] == "TRUE":
				#__get random state (TRUE or FALSE)
				random_state = random.choice(states)
				if random_state == "FALSE":
					#__replace "TRUE" with "FALSE"
					row[position] = random_state
					#__raise false count
					false_count +=1
	#___base case 01 > if 7 FALSE are in the list, return it
	if (false_count < maximum):
		add_difficulty(difficulty_field,minimum,maximum,row_size,false_count)
	return difficulty_field


#_______________________________GENERATE start_game_savefile
def generate_start_game_file(game = None, difficulty = None):

	user_field_choise = str(game)
	user_difficulty_choise = str(difficulty)
	points = ""

		#___get start numbers from game functions
	if user_field_choise == "4x4":
		orginal_field = generate_4x4_game()
		#__add default points and difficulty
		if user_difficulty_choise == "novize":
			field = add_difficulty(orginal_field,6,7,4)
			points = "1111"
		elif user_difficulty_choise == "master":
			field = add_difficulty(orginal_field,8,9,4)
			points = "2222"
		elif user_difficulty_choise == "legend":
			field = add_difficulty(orginal_field,10,11,4)
			points = "3333"
		first_row = [user_field_choise] + [user_difficulty_choise] + [points]
		start_game_savefile_lst = [first_row] + (field)
		


	#___create start game file > reset button
	with open("set_start_game_savefile.csv", "w",newline='') as start_game_file:
		csv_writer = csv.writer(start_game_file)
		for item in start_game_savefile_lst:
			csv_writer.writerow(item)

		start_game_file.close()

	#___create game file where the progress of the user is saved > continue button
	with open("set_game_savefile.csv", "w",newline='') as save_game_file:
		csv_writer = csv.writer(save_game_file)
		for item in start_game_savefile_lst:
			csv_writer.writerow(item)

		save_game_file.close()



