import random
import string
import csv
#__________________4x4
def generate_4x4_game():

	#__generate random row / shuffle overwrites exsiting list
	first_row = [str(number) for number in range(1,5)]
	random.shuffle(first_row)

	#__generates random row by splitting the first up in two parts, randomize the parts, switch the parts
	secound_row_p1 = first_row[:2]
	secound_row_p2 = first_row[2:]
	random.shuffle(secound_row_p1)
	random.shuffle(secound_row_p2)
	secound_row = secound_row_p2 + secound_row_p1

	#__generates first column
	first_column_p1 = first_row[:1] + secound_row[:1]
	#__________________________from index 1 step 2
	first_column_p2 = first_row[1:2] + secound_row[1:2]
	random.shuffle(first_column_p1)
	random.shuffle(first_column_p2)

	#__other column lists for checks
	third_column = first_row[2:3] + secound_row[2:3]
	forth_column = first_row[3:] + secound_row[3:]


	#__generate third and forth row
	third_row = first_column_p2[:1] + first_column_p1[:1]
	forth_row = first_column_p2[1:2] + first_column_p1[1:2]
	print(third_row)
	print(forth_row)

	for number in forth_row:
		number = str(number)
		if (number not in third_column) and (number not in third_row):
			third_row.append(number)
	for number in third_row[:2]:
	 	number = str(number)
	 	if (number not in third_column) and (number not in forth_row):
	 		forth_row.append(number)
	for number in range(1,5):
		number = str(number)
		if number not in third_row:
			third_row.append(number)
		if number not in forth_row:
			forth_row.append(number)

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
	def get_random_position(row_size):
		position = random.choice(range(2,(row_size +1)))
		return position

	if false_count == minimum:
		return difficulty_field
	else:
		for row in orginal_field:
			position = get_random_position(row_size)
			if row[position] == "TRUE":
				random_state = random.choice(states)
				if random_state == "FALSE":
					row[position] = random_state
					false_count +=1
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



