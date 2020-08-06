from tkinter import *
import csv


#>>>>>>>>> Creating the GUI >>>>>>>>>>>>>>>#

root = Tk()

def window(main):
	main.title("Sudoku")
	#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!___Disable Window Frame
	#main.overrideredirect(1)
	#___Application size
	width_of_window = 1024
	height_of_window = 1024

	#___Get user screen size
	user_window_width = main.winfo_screenwidth()/2
	user_window_height = main.winfo_screenheight()/2
	#___Get center position of the window
	x_center = int(user_window_width - (width_of_window / 2))
	y_center = int((user_window_height - (height_of_window / 2))/2)
	#___Placing the window in the center of the screen
	main.geometry("+{0}+{1}".format(x_center,y_center))
	root.resizable(0,0)
	root.attributes("-topmost", True)


#__________________Background Images
main_menu_bg_image = PhotoImage(file = "images/MainMenue_Screen.png")
difficulty_screen_bg_image = PhotoImage(file = "images/Difficulty_Screen.png")
achievement_screen_bg_image = PhotoImage(file = "images/Achievement_Screen.png")
highscore_screen_bg_image = PhotoImage(file = "images/Highscore_Screen.png")
achievement_screen_bg_image = PhotoImage(file = "images/Achievement_Screen.png")
ingame_4x4_screen_bg_image = PhotoImage(file = "images/Ingame4x4_Screen.png")
ingame_9x9_screen_bg_image = PhotoImage(file = "images/Ingame9x9_Screen.png")
ingame_16x16_screen_bg_image = PhotoImage(file = "images/Ingame16x16_Screen.png")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> INGAME BUTTON FUNCTIONS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
def show_info_screen():
	pass

def save_and_back_to_mainmenu(background_image,savefile):
	#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!save game
	load_main_menu(background_image)

def hint(hint_ingame_button,hint_ingame_button_image_onclick,hint_ingame_button_image_active,savefile):

	#__if user clicks on button, chance button image
	hint_ingame_button.config( image = hint_ingame_button_image_onclick)
	hint_ingame_button.image = hint_ingame_button_image_onclick

	#__check if all entert numbers are correct

	#__give hint if all numbers are correct

	#__set button back to active after hint is completet
	#hint_ingame_button.config( image = hint_ingame_button_image_active)
	#hint_ingame_button.image = hint_ingame_button_image_active

	update_points(100)

def check(check_ingame_button,check_ingame_button_image_onclick,check_ingame_button_image_active,savefile):

	#__if user clicks on button, chance button image
	check_ingame_button.config( image = check_ingame_button_image_onclick)
	check_ingame_button.image = check_ingame_button_image_onclick

	#__check if all entert numbers are correct

	#__set button back to active after check is completet
	#check_ingame_button.config( image = check_ingame_button_image_active)
	#check_ingame_button.image = check_ingame_button_image_active

	update_points(50)

def update_points(amount = 0):
	pass
	#__overwrite set_points.csv
	# score = points - amount

def reset(reset_ingame_button,reset_ingame_button_image_onclick,reset_ingame_button_image_active,background_image,start_game_savefile):

	#__if user clicks on button, chance button image
	reset_ingame_button.config( image = reset_ingame_button_image_onclick)
	reset_ingame_button.image = reset_ingame_button_image_onclick

	#___load game with start savefile
	#go_to_ingame_screen(background_image,start_game_savefile)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>        INGAME    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

def go_to_ingame_screen(background_image,savefile = None):

	#___if user wants to continue, check save file
	if savefile == None:
		#___check selcted user choises in set difficulty sheet
		with open("set_difficulty.csv", "r",newline='') as difficulty_file:
			csv_reader = csv.reader(difficulty_file)

			user_field_choise = ""
			user_difficulty_choise = ""

			for row in csv_reader:
				if row[0] == "default_4x4":
					if row[1] == "active":
						user_field_choise = "4x4"
						if row[2] == "novize_active":
							user_difficulty_choise = "novize"
						elif row[3] == "master_active":
							user_difficulty_choise = "master"
						else:
							user_difficulty_choise = "legend"
				elif row[0] == "default_9x9":
					if row[1] == "active":
						user_field_choise = "9x9"
						if row[2] == "novize_active":
							user_difficulty_choise = "novize"
						elif row[3] == "master_active":
							user_difficulty_choise = "master"
						else:
							user_difficulty_choise = "legend"
				elif row[0] == "default_16x16":
					if row[1] == "active":
						user_field_choise = "16x16"
						if row[2] == "novize_active":
							user_difficulty_choise = "novize"
						elif row[3] == "master_active":
							user_difficulty_choise = "master"
						else:
							user_difficulty_choise = "legend"
			difficulty_file.close()

		if user_field_choise == "4x4":
			background_image.pack_forget()
			background_image = Label(root,image = ingame_4x4_screen_bg_image)
			background_image.pack()
			#create save file
			#create start game savefile for reset
			start_game_savefile = None
			#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!___difficulty / save start numbers / game / points

		elif user_field_choise == "9x9":
			background_image.pack_forget()
			background_image = Label(root,image = ingame_9x9_screen_bg_image)
			background_image.pack()
			#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!___difficulty / save start numbers / game / points
			

		elif user_field_choise == "16x16":
			background_image.pack_forget()
			background_image = Label(root,image = ingame_16x16_screen_bg_image)
			background_image.pack()
			#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!___difficulty / save start numbers / game / poins

	#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!___save file
	else:
		pass

	#___________________________________INGAME Buttons_______________________________________________________________

	#___________________Info Button
	info_ingame_button_image_active = PhotoImage(file = "images/InGameButtons/InGame_InfoButton_active.png")
	info_ingame_button_image_onclick = PhotoImage(file = "images/InGameButtons/InGame_InfoButton_onClick.png")

	#___define appearance of button
	info_ingame_button = Label(root,image = info_ingame_button_image_active,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
	info_ingame_button.place(relx=.963, rely= 0.04, anchor="center")

	#___button mouse hover functions
	def set_info_ingame_button_hover(event):
		info_ingame_button.config( image = info_ingame_button_image_onclick)
		info_ingame_button.image = info_ingame_button_image_onclick

	def set_info_ingame_button_active(event):
		info_ingame_button.config( image = info_ingame_button_image_active)
		info_ingame_button.image = info_ingame_button_image_active

	#___mouse hover and function call
	info_ingame_button.bind("<Enter>", set_info_ingame_button_hover)
	info_ingame_button.bind("<Leave>", set_info_ingame_button_active)
	info_ingame_button_onclick_funktion = lambda x:show_info_screen()
	info_ingame_button.bind("<Button-1>",info_ingame_button_onclick_funktion)

	#___________________Exit Button
	exit_ingame_button_image_active = PhotoImage(file = "images/InGameButtons/InGame_ExitButton_active.png")
	exit_ingame_button_image_onclick = PhotoImage(file = "images/InGameButtons/InGame_ExitButton_onClick.png")

	#___define appearance of button
	exit_ingame_button = Label(root,image = exit_ingame_button_image_active,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
	exit_ingame_button.place(relx=.871, rely= 0.17, anchor="center")

	#___button mouse hover functions
	def set_exit_ingame_button_hover(event):
		exit_ingame_button.config( image = exit_ingame_button_image_onclick)
		exit_ingame_button.image = exit_ingame_button_image_onclick

	def set_exit_ingame_button_active(event):
		exit_ingame_button.config( image = exit_ingame_button_image_active)
		exit_ingame_button.image = exit_ingame_button_image_active

	#___mouse hover and function call
	exit_ingame_button.bind("<Enter>", set_exit_ingame_button_hover)
	exit_ingame_button.bind("<Leave>", set_exit_ingame_button_active)
	exit_ingame_button_onclick_funktion = lambda x:save_and_back_to_mainmenu(background_image,savefile)
	exit_ingame_button.bind("<Button-1>",exit_ingame_button_onclick_funktion)


	#___________________Hint Button
	hint_ingame_button_image_active = PhotoImage(file = "images/InGameButtons/InGame_HintButton_active.png")
	hint_ingame_button_image_onclick = PhotoImage(file = "images/InGameButtons/InGame_HintButton_onClick.png")

	#___define appearance of button
	hint_ingame_button = Label(root,image = hint_ingame_button_image_active,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
	hint_ingame_button.place(relx=.943, rely= 0.4195, anchor="center")
	hint_ingame_button.config( image = hint_ingame_button_image_active)
	hint_ingame_button.image = hint_ingame_button_image_active

	#___button mouse hover functions
	hint_ingame_button_onclick_funktion = lambda x:hint(hint_ingame_button,hint_ingame_button_image_onclick,hint_ingame_button_image_active,savefile)
	hint_ingame_button.bind("<Button-1>",hint_ingame_button_onclick_funktion)

	#___________________Check Button
	check_ingame_button_image_active = PhotoImage(file = "images/InGameButtons/InGame_CheckButton_active.png")
	check_ingame_button_image_onclick = PhotoImage(file = "images/InGameButtons/InGame_CheckButton_onClick.png")

	#___define appearance of button
	check_ingame_button = Label(root,image = check_ingame_button_image_active,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
	check_ingame_button.place(relx=.943, rely= 0.53, anchor="center")
	check_ingame_button.config( image = check_ingame_button_image_active)
	check_ingame_button.image = check_ingame_button_image_active

	#___button mouse hover functions
	check_ingame_button_onclick_funktion = lambda x:check(check_ingame_button,check_ingame_button_image_onclick,check_ingame_button_image_active,savefile)
	check_ingame_button.bind("<Button-1>",check_ingame_button_onclick_funktion)

	
	#___________________Reset Button
	reset_ingame_button_image_active = PhotoImage(file = "images/InGameButtons/InGame_ResetButton_active.png")
	reset_ingame_button_image_onclick = PhotoImage(file = "images/InGameButtons/InGame_ResetButton_onClick.png")

	#___define appearance of button
	reset_ingame_button = Label(root,image = reset_ingame_button_image_active,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
	reset_ingame_button.place(relx=.943, rely= 0.644, anchor="center")
	reset_ingame_button.config( image = reset_ingame_button_image_active)
	reset_ingame_button.image = reset_ingame_button_image_active

	#___button mouse hover functions
	reset_ingame_button_onclick_funktion = lambda x:reset(reset_ingame_button,reset_ingame_button_image_onclick,reset_ingame_button_image_active,background_image,start_game_savefile)
	reset_ingame_button.bind("<Button-1>",reset_ingame_button_onclick_funktion)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> MENU BUTTON FUNCTIONS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

def continue_savegame(background_image):
	pass
def go_to_difficulty_screen(background_image):

	#_________________Replace background image
	background_image.pack_forget()
	background_image = Label(root,image = difficulty_screen_bg_image)
	background_image.pack()
	
	#__________________Field Size Buttons
	d_screen_4x4_button_active = PhotoImage(file = "images/MainmenueButtons/DScreen_4x4Button_active.png")
	d_screen_4x4_button_inactive = PhotoImage(file = "images/MainmenueButtons/DScreen_4x4Button_inactive.png")

	d_screen_9x9_button_active = PhotoImage(file = "images/MainmenueButtons/DScreen_9x9Button_active.png")
	d_screen_9x9_button_inactive = PhotoImage(file = "images/MainmenueButtons/DScreen_9x9Button_inactive.png")

	d_screen_16x16_button_active = PhotoImage(file = "images/MainmenueButtons/DScreen_16x16NovizeButton_active.png")
	d_screen_16x16_button_inactive = PhotoImage(file = "images/MainmenueButtons/DScreen_16x16NovizeButton_inactive.png")

	#__________________Difficulty Buttons
	novize_button_active = PhotoImage(file = "images/MainmenueButtons/DScreen_NovizeButton_active.png")
	novize_button_inactive = PhotoImage(file = "images/MainmenueButtons/DScreen_NovizeButton_inactive.png")

	master_button_active = PhotoImage(file = "images/MainmenueButtons/DScreen_MasterButton_active.png")
	master_button_inactive = PhotoImage(file = "images/MainmenueButtons/DScreen_MasterButton_inactive.png")
	master_button_locked = PhotoImage(file = "images/MainmenueButtons/DScreen_MasterButton_locked.png")

	legend_button_active = PhotoImage(file = "images/MainmenueButtons/DScreen_LegendButton_active.png")
	legend_button_inactive = PhotoImage(file = "images/MainmenueButtons/DScreen_LegendButton_inactive.png")
	legend_button_locked = PhotoImage(file = "images/MainmenueButtons/DScreen_LegendButton_locked.png")



	#___saves the user input choise in set_difficulty.csv
	def overwrite_difficulty_in_file(default_4x4 = "active",default_9x9 = "inactive",default_16x16 = "inactive",novize = "novize_active",master = "master_locked",legend = "legend_locked",target = None):

		#___reads set_difficulty.csv to restore the last default and creates a copy with new user input in it 
		with open("set_difficulty.csv", "r",newline='') as difficulty_file:
			csv_reader = csv.reader(difficulty_file)

			possible_difficulties_4x4 = []
			possible_difficulties_9x9 = []
			possible_difficulties_16x16 = []

			for row in csv_reader:
				if row[0] == "default_4x4":
					current_difficulty = row[2:]
					for item in current_difficulty:
						possible_difficulties_4x4.append(item)
				elif row[0] == "default_9x9":
					current_difficulty = row[2:]
					for item in current_difficulty:
						possible_difficulties_9x9.append(item)
				elif row[0] == "default_16x16":
					current_difficulty = row[2:]
					for item in current_difficulty:
						possible_difficulties_16x16.append(item)

			difficulty_file.close()

		if target == "possible_difficulties_4x4":
		 	possible_difficulties_4x4 = []
		 	possible_difficulties_4x4 = [novize,master,legend]
		if target == "possible_difficulties_9x9":
		 	possible_difficulties_9x9 = []
		 	possible_difficulties_9x9 = [novize,master,legend]
		if target == "possible_difficulties_16x16":
		 	possible_difficulties_16x16 = []
		 	possible_difficulties_16x16 = [novize,master,legend]


		upadated_difficulty_lst = []
		upadated_4x4_difficulty_lst = []
		upadated_9x9_difficulty_lst = []
		upadated_16x16_difficulty_lst = []
		
		upadated_4x4_difficulty_lst.append("default_4x4")
		upadated_4x4_difficulty_lst.append(default_4x4)
		for item in possible_difficulties_4x4:
			upadated_4x4_difficulty_lst.append(str(item))

		upadated_9x9_difficulty_lst.append("default_9x9")
		upadated_9x9_difficulty_lst.append(default_9x9)
		for item in possible_difficulties_9x9:
			upadated_9x9_difficulty_lst.append(str(item))

		upadated_16x16_difficulty_lst.append("default_16x16")
		upadated_16x16_difficulty_lst.append(default_16x16)
		for item in possible_difficulties_16x16:
			upadated_16x16_difficulty_lst.append(str(item))


		upadated_difficulty_lst.append(upadated_4x4_difficulty_lst)
		upadated_difficulty_lst.append(upadated_9x9_difficulty_lst)
		upadated_difficulty_lst.append(upadated_16x16_difficulty_lst)

		#___overwrites set_difficulty.csv with new user input
		with open("set_difficulty.csv", "w",newline='') as difficulty_file:
			csv_writer = csv.writer(difficulty_file)
			for item in upadated_difficulty_lst:
				csv_writer.writerow(item)

			difficulty_file.close()
		#___Function Call: Load current set_difficulty.csv
		load_last_play_default()

	#___load current set_difficulty.csv
	def load_last_play_default():

		#___read set_difficulty.csv to get last user input on field size
		with open("set_difficulty.csv", "r",newline='') as difficulty_file:
			csv_reader = csv.reader(difficulty_file)

			last_safed_field_state_lst = []
			possible_difficulties_4x4 = []
			possible_difficulties_9x9 = []
			possible_difficulties_16x16 = []

			for row in csv_reader:
				last_safed_field_state_lst.append(row[1])
				if row[0] == "default_4x4":
					current_difficulty = row[2:]
					for item in current_difficulty:
						possible_difficulties_4x4.append(item)
				elif row[0] == "default_9x9":
					current_difficulty = row[2:]
					for item in current_difficulty:
						possible_difficulties_9x9.append(item)
				elif row[0] == "default_16x16":
					current_difficulty = row[2:]
					for item in current_difficulty:
						possible_difficulties_16x16.append(item)


			default_4x4 = str(last_safed_field_state_lst[0])
			default_9x9 = str(last_safed_field_state_lst[1])
			default_16x16 = str(last_safed_field_state_lst[2])

			difficulty_file.close()

		#___read set_achievements.csv to lock or unlock difficulty level
		with open("set_achievements.csv", "r",newline='') as achievement_file:
			csv_reader = csv.reader(achievement_file)


			for row in csv_reader:
				if row[0] == "4x4Novize":
					if row[1] == "FALSE":
						possible_difficulties_4x4[1] = "master_locked"
				if row[0] == "4x4Master":
					if row[1] == "FALSE":
						possible_difficulties_4x4[2] = "legend_locked"
				if row[0] == "9x9Novize":
					if row[1] == "FALSE":
						possible_difficulties_9x9[1] = "master_locked"
				if row[0] == "9x9Master":
					if row[1] == "FALSE":
						possible_difficulties_9x9[2] = "legend_locked"
				if row[0] == "16x16Novize":
					if row[1] == "FALSE":
						possible_difficulties_16x16[1] = "master_locked"
				if row[0] == "16x16Master":
					if row[1] == "FALSE":
						possible_difficulties_16x16[2] = "legend_locked"

			achievement_file.close()

		#__define field size button
		if default_4x4 == "active":
			#___define appearance of 4x4 button 
			d_screen_4x4_button = Button(root,image = d_screen_4x4_button_active,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
			d_screen_4x4_button.place(relx=.33, rely= 0.2675, anchor="center")
			d_screen_4x4_button.config( image = d_screen_4x4_button_active)
			d_screen_4x4_button.image = d_screen_4x4_button_active
			#___define appearance of 9x9 button set to active and call difficulty csv overwrite function
			d_screen_9x9_button = Button(root,image = d_screen_9x9_button_inactive,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
			d_screen_9x9_button.place(relx=.5, rely= 0.2675, anchor="center")
			d_screen_9x9_button.config( image = d_screen_9x9_button_inactive)
			d_screen_9x9_button.config( command = lambda:overwrite_difficulty_in_file("inactive","active","inactive"))
			d_screen_9x9_button.image = d_screen_9x9_button_inactive
			#___define appearance of 16x16 button set to active and call difficulty csv overwrite function
			d_screen_16x16_button = Button(root,image = d_screen_16x16_button_inactive,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
			d_screen_16x16_button.place(relx=.665, rely= 0.2675, anchor="center")
			d_screen_16x16_button.config( image = d_screen_16x16_button_inactive)
			d_screen_16x16_button.config( command = lambda:overwrite_difficulty_in_file("inactive","inactive","active"))
			d_screen_16x16_button.image = d_screen_16x16_button_inactive


			#___define appearance of difficulty button set to locked / inactive / active and call difficulty csv overwrite function
			if possible_difficulties_4x4[0] == "novize_active":
				d_screen_novize_button = Button(root,image = novize_button_active,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
				d_screen_novize_button.place(relx=.33, rely= 0.435, anchor="center")
				d_screen_novize_button.config( image = novize_button_active)
				d_screen_novize_button.image = novize_button_active
				if possible_difficulties_4x4[1] == "master_inactive":
					d_screen_master_button = Button(root,image = master_button_inactive,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
					d_screen_master_button.place(relx=.5, rely= 0.45, anchor="center")
					d_screen_master_button.config( image = master_button_inactive)
					if possible_difficulties_4x4[2] == "legend_inactive":
						d_screen_master_button.config( command = lambda:overwrite_difficulty_in_file("active","inactive","inactive","novize_inactive","master_active","legend_inactive","possible_difficulties_4x4"))
						d_screen_master_button.image = master_button_inactive
					else:
						d_screen_master_button.config( command = lambda:overwrite_difficulty_in_file("active","inactive","inactive","novize_inactive","master_active","legend_locked","possible_difficulties_4x4"))
						d_screen_master_button.image = master_button_inactive
				elif possible_difficulties_4x4[1] == "master_locked":
						d_screen_master_button = Button(root,image = master_button_locked,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
						d_screen_master_button.place(relx=.5, rely= 0.45, anchor="center")
						d_screen_master_button.config( image = master_button_locked)
						d_screen_master_button.image = master_button_locked
				if possible_difficulties_4x4[2] == "legend_inactive":
					d_screen_legend_button = Button(root,image = legend_button_inactive,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
					d_screen_legend_button.place(relx=.665, rely= 0.45, anchor="center")
					d_screen_legend_button.config( image = legend_button_inactive)
					d_screen_legend_button.config( command = lambda:overwrite_difficulty_in_file("active","inactive","inactive","novize_inactive","master_inactive","legend_active","possible_difficulties_4x4"))
					d_screen_legend_button.image = legend_button_inactive
				elif possible_difficulties_4x4[2] == "legend_locked":
					d_screen_legend_button = Button(root,image = legend_button_locked,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
					d_screen_legend_button.place(relx=.665, rely= 0.45, anchor="center")
					d_screen_legend_button.config( image = legend_button_locked)
					d_screen_legend_button.image = legend_button_locked

			if possible_difficulties_4x4[1] == "master_active":
				d_screen_master_button = Button(root,image = master_button_active,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
				d_screen_master_button.place(relx=.5, rely= 0.45, anchor="center")
				d_screen_master_button.config( image = master_button_active)
				d_screen_master_button.image = master_button_active
				if possible_difficulties_4x4[0] == "novize_inactive":
					d_screen_novize_button = Button(root,image = novize_button_inactive,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
					d_screen_novize_button.place(relx=.33, rely= 0.435, anchor="center")
					if possible_difficulties_4x4[2] == "legend_inactive":
						d_screen_novize_button.config( command = lambda:overwrite_difficulty_in_file("active","inactive","inactive","novize_active","master_inactive","legend_inactive","possible_difficulties_4x4"))
						d_screen_novize_button.config( image = novize_button_inactive)
						d_screen_novize_button.image = novize_button_inactive
					else:
						d_screen_novize_button.config( command = lambda:overwrite_difficulty_in_file("active","inactive","inactive","novize_active","master_inactive","legend_locked","possible_difficulties_4x4"))
						d_screen_novize_button.config( image = novize_button_inactive)
						d_screen_novize_button.image = novize_button_inactive

				if possible_difficulties_4x4[2] == "inactive":
						d_screen_legend_button = Button(root,image = legend_button_inactive,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
						d_screen_legend_button.place(relx=.665, rely= 0.45, anchor="center")
						d_screen_legend_button.config( image = legend_button_inactive)
						d_screen_legend_button.config( command = lambda:overwrite_difficulty_in_file("active","inactive","inactive","novize_inactive","master_inactive","legend_active","possible_difficulties_4x4"))
						d_screen_legend_button.image = legend_button_inactive
				elif possible_difficulties_4x4[2] == "legend_locked":
						d_screen_legend_button = Button(root,image = legend_button_locked,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
						d_screen_legend_button.place(relx=.665, rely= 0.45, anchor="center")
						d_screen_legend_button.config( image = legend_button_locked)
						d_screen_legend_button.image = legend_button_locked

			if possible_difficulties_4x4[2] == "legend_active":
				d_screen_legend_button = Button(root,image = legend_button_active,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
				d_screen_legend_button.place(relx=.665, rely= 0.45, anchor="center")
				d_screen_legend_button.config( image = legend_button_active)
				d_screen_legend_button.image = legend_button_active
				if possible_difficulties_4x4[0] == "novize_inactive":
					d_screen_novize_button = Button(root,image = novize_button_inactive,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
					d_screen_novize_button.place(relx=.33, rely= 0.435, anchor="center")
					d_screen_novize_button.config( command = lambda:overwrite_difficulty_in_file("active","inactive","inactive","novize_active","master_inactive","legend_inactive","possible_difficulties_4x4"))
					d_screen_novize_button.config( image = novize_button_inactive)
					d_screen_novize_button.image = novize_button_inactive
				elif possible_difficulties_4x4[1] == "master_inactive":
					d_screen_master_button = Button(root,image = master_button_inactive,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
					d_screen_master_button.place(relx=.5, rely= 0.45, anchor="center")
					d_screen_master_button.config( command = lambda:overwrite_difficulty_in_file("active","inactive","inactive","novize_inactive","master_active","legend_inactive","possible_difficulties_4x4"))
					d_screen_master_button.config( image = master_button_inactive)
					d_screen_master_button.image = master_button_inactive

		if default_9x9 == "active":
			#___define appearance of 4x4 button set to active and call difficulty csv overwrite function
			d_screen_4x4_button = Button(root,image = d_screen_4x4_button_inactive,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
			d_screen_4x4_button.place(relx=.33, rely= 0.2675, anchor="center")
			d_screen_4x4_button.config( image = d_screen_4x4_button_inactive)
			d_screen_4x4_button.config( command = lambda:overwrite_difficulty_in_file("active","inactive","inactive"))
			d_screen_4x4_button.image = d_screen_4x4_button_inactive
			#___define appearance of 9x9 button 
			d_screen_9x9_button = Button(root,image = d_screen_9x9_button_active,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
			d_screen_9x9_button.place(relx=.5, rely= 0.2675, anchor="center")
			d_screen_9x9_button.config( image = d_screen_9x9_button_active)
			d_screen_9x9_button.image = d_screen_9x9_button_active
			#___define appearance of 16x16 button set to active and call difficulty csv overwrite function
			d_screen_16x16_button = Button(root,image = d_screen_16x16_button_inactive,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
			d_screen_16x16_button.place(relx=.665, rely= 0.2675, anchor="center")
			d_screen_16x16_button.config( image = d_screen_16x16_button_inactive)
			d_screen_16x16_button.config( command = lambda:overwrite_difficulty_in_file("inactive","inactive","active"))
			d_screen_16x16_button.image = d_screen_16x16_button_inactive

			#___define appearance of difficulty button set to locked / inactive / active and call difficulty csv overwrite function
			if possible_difficulties_9x9[0] == "novize_active":
				d_screen_novize_button = Button(root,image = novize_button_active,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
				d_screen_novize_button.place(relx=.33, rely= 0.435, anchor="center")
				d_screen_novize_button.config( image = novize_button_active)
				d_screen_novize_button.image = novize_button_active
				if possible_difficulties_9x9[1] == "master_inactive":
					d_screen_master_button = Button(root,image = master_button_inactive,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
					d_screen_master_button.place(relx=.5, rely= 0.45, anchor="center")
					d_screen_master_button.config( image = master_button_inactive)
					if possible_difficulties_9x9[2] == "legend_inactive":
						d_screen_master_button.config( command = lambda:overwrite_difficulty_in_file("inactive","active","inactive","novize_inactive","master_active","legend_inactive","possible_difficulties_9x9"))
						d_screen_master_button.image = master_button_inactive
					else:
						d_screen_master_button.config( command = lambda:overwrite_difficulty_in_file("inactive","active","inactive","novize_inactive","master_active","legend_locked","possible_difficulties_9x9"))
						d_screen_master_button.image = master_button_inactive
				elif possible_difficulties_9x9[1] == "master_locked":
						d_screen_master_button = Button(root,image = master_button_locked,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
						d_screen_master_button.place(relx=.5, rely= 0.45, anchor="center")
						d_screen_master_button.config( image = master_button_locked)
						d_screen_master_button.image = master_button_locked
				if possible_difficulties_9x9[2] == "legend_inactive":
					d_screen_legend_button = Button(root,image = legend_button_inactive,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
					d_screen_legend_button.place(relx=.665, rely= 0.45, anchor="center")
					d_screen_legend_button.config( image = legend_button_inactive)
					d_screen_legend_button.config( command = lambda:overwrite_difficulty_in_file("inactive","active","inactive","novize_inactive","master_inactive","legend_active","possible_difficulties_9x9"))
					d_screen_legend_button.image = legend_button_inactive
				elif possible_difficulties_9x9[2] == "legend_locked":
					d_screen_legend_button = Button(root,image = legend_button_locked,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
					d_screen_legend_button.place(relx=.665, rely= 0.45, anchor="center")
					d_screen_legend_button.config( image = legend_button_locked)
					d_screen_legend_button.image = legend_button_locked

			if possible_difficulties_9x9[1] == "master_active":
				d_screen_master_button = Button(root,image = master_button_active,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
				d_screen_master_button.place(relx=.5, rely= 0.45, anchor="center")
				d_screen_master_button.config( image = master_button_active)
				d_screen_master_button.image = master_button_active
				if possible_difficulties_9x9[0] == "novize_inactive":
					d_screen_novize_button = Button(root,image = novize_button_inactive,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
					d_screen_novize_button.place(relx=.33, rely= 0.435, anchor="center")
					if possible_difficulties_9x9[2] == "legend_inactive":
						d_screen_novize_button.config( command = lambda:overwrite_difficulty_in_file("inactive","active","inactive","novize_active","master_inactive","legend_inactive","possible_difficulties_9x9"))
						d_screen_novize_button.config( image = novize_button_inactive)
						d_screen_novize_button.image = novize_button_inactive
					else:
						d_screen_novize_button.config( command = lambda:overwrite_difficulty_in_file("inactive","active","inactive","novize_active","master_inactive","legend_locked","possible_difficulties_9x9"))
						d_screen_novize_button.config( image = novize_button_inactive)
						d_screen_novize_button.image = novize_button_inactive

				if possible_difficulties_9x9[2] == "inactive":
						d_screen_legend_button = Button(root,image = legend_button_inactive,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
						d_screen_legend_button.place(relx=.665, rely= 0.45, anchor="center")
						d_screen_legend_button.config( image = legend_button_inactive)
						d_screen_legend_button.config( command = lambda:overwrite_difficulty_in_file("active","inactive","inactive","novize_inactive","master_inactive","legend_active","possible_difficulties_4x4"))
						d_screen_legend_button.image = legend_button_inactive
				elif possible_difficulties_9x9[2] == "legend_locked":
						d_screen_legend_button = Button(root,image = legend_button_locked,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
						d_screen_legend_button.place(relx=.665, rely= 0.45, anchor="center")
						d_screen_legend_button.config( image = legend_button_locked)
						d_screen_legend_button.image = legend_button_locked

			if possible_difficulties_9x9[2] == "legend_active":
				d_screen_legend_button = Button(root,image = legend_button_active,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
				d_screen_legend_button.place(relx=.665, rely= 0.45, anchor="center")
				d_screen_legend_button.config( image = legend_button_active)
				d_screen_legend_button.image = legend_button_active
				if possible_difficulties_9x9[0] == "novize_inactive":
					d_screen_novize_button = Button(root,image = novize_button_inactive,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
					d_screen_novize_button.place(relx=.33, rely= 0.435, anchor="center")
					d_screen_novize_button.config( command = lambda:overwrite_difficulty_in_file("inactive","active","inactive","novize_active","master_inactive","legend_inactive","possible_difficulties_9x9"))
					d_screen_novize_button.config( image = novize_button_inactive)
					d_screen_novize_button.image = novize_button_inactive
				elif possible_difficulties_9x9[1] == "master_inactive":
					d_screen_master_button = Button(root,image = master_button_inactive,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
					d_screen_master_button.place(relx=.5, rely= 0.45, anchor="center")
					d_screen_master_button.config( command = lambda:overwrite_difficulty_in_file("inactive","active","inactive","novize_inactive","master_active","legend_inactive","possible_difficulties_9x9"))
					d_screen_master_button.config( image = master_button_inactive)
					d_screen_master_button.image = master_button_inactive

		if default_16x16 == "active":
			#___define appearance of 4x4 button set to active and call difficulty csv overwrite function
			d_screen_4x4_button = Button(root,image = d_screen_4x4_button_inactive,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
			d_screen_4x4_button.place(relx=.33, rely= 0.2675, anchor="center")
			d_screen_4x4_button.config( image = d_screen_4x4_button_inactive)
			d_screen_4x4_button.config( command = lambda:overwrite_difficulty_in_file("active","inactive","inactive"))
			d_screen_4x4_button.image = d_screen_4x4_button_inactive
			#___define appearance of 9x9 button set to active and call difficulty csv overwrite function
			d_screen_9x9_button = Button(root,image = d_screen_9x9_button_inactive,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
			d_screen_9x9_button.place(relx=.5, rely= 0.2675, anchor="center")
			d_screen_9x9_button.config( image = d_screen_9x9_button_inactive)
			d_screen_9x9_button.config( command = lambda:overwrite_difficulty_in_file("inactive","active","inactive"))
			d_screen_9x9_button.image = d_screen_9x9_button_inactive
			#___Define appearance of 16x16 button
			d_screen_16x16_button = Button(root,image = d_screen_16x16_button_active,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
			d_screen_16x16_button.place(relx=.665, rely= 0.2675, anchor="center")
			d_screen_16x16_button.config( image = d_screen_16x16_button_active)
			d_screen_16x16_button.image = d_screen_16x16_button_active

			#___define appearance of difficulty button set to locked / inactive / active and call difficulty csv overwrite function
			if possible_difficulties_16x16[0] == "novize_active":
				d_screen_novize_button = Button(root,image = novize_button_active,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
				d_screen_novize_button.place(relx=.33, rely= 0.435, anchor="center")
				d_screen_novize_button.config( image = novize_button_active)
				d_screen_novize_button.image = novize_button_active
				if possible_difficulties_16x16[1] == "master_inactive":
					d_screen_master_button = Button(root,image = master_button_inactive,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
					d_screen_master_button.place(relx=.5, rely= 0.45, anchor="center")
					d_screen_master_button.config( image = master_button_inactive)
					if possible_difficulties_16x16[2] == "legend_inactive":
						d_screen_master_button.config( command = lambda:overwrite_difficulty_in_file("inactive","inactive","active","novize_inactive","master_active","legend_inactive","possible_difficulties_16x16"))
						d_screen_master_button.image = master_button_inactive
					else:
						d_screen_master_button.config( command = lambda:overwrite_difficulty_in_file("inactive","inactive","active","novize_inactive","master_active","legend_locked","possible_difficulties_16x16"))
						d_screen_master_button.image = master_button_inactive
				elif possible_difficulties_16x16[1] == "master_locked":
						d_screen_master_button = Button(root,image = master_button_locked,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
						d_screen_master_button.place(relx=.5, rely= 0.45, anchor="center")
						d_screen_master_button.config( image = master_button_locked)
						d_screen_master_button.image = master_button_locked
				if possible_difficulties_16x16[2] == "legend_inactive":
					d_screen_legend_button = Button(root,image = legend_button_inactive,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
					d_screen_legend_button.place(relx=.665, rely= 0.45, anchor="center")
					d_screen_legend_button.config( image = legend_button_inactive)
					d_screen_legend_button.config( command = lambda:overwrite_difficulty_in_file("inactive","inactive","active","novize_inactive","master_inactive","legend_active","possible_difficulties_16x16"))
					d_screen_legend_button.image = legend_button_inactive
				elif possible_difficulties_16x16[2] == "legend_locked":
					d_screen_legend_button = Button(root,image = legend_button_locked,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
					d_screen_legend_button.place(relx=.665, rely= 0.45, anchor="center")
					d_screen_legend_button.config( image = legend_button_locked)
					d_screen_legend_button.image = legend_button_locked

			if possible_difficulties_16x16[1] == "master_active":
				d_screen_master_button = Button(root,image = master_button_active,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
				d_screen_master_button.place(relx=.5, rely= 0.45, anchor="center")
				d_screen_master_button.config( image = master_button_active)
				d_screen_master_button.image = master_button_active
				if possible_difficulties_16x16[0] == "novize_inactive":
					d_screen_novize_button = Button(root,image = novize_button_inactive,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
					d_screen_novize_button.place(relx=.33, rely= 0.435, anchor="center")
					if possible_difficulties_16x16[2] == "legend_inactive":
						d_screen_novize_button.config( command = lambda:overwrite_difficulty_in_file("inactive","inactive","active","novize_active","master_inactive","legend_inactive","possible_difficulties_16x16"))
						d_screen_novize_button.config( image = novize_button_inactive)
						d_screen_novize_button.image = novize_button_inactive
					else:
						d_screen_novize_button.config( command = lambda:overwrite_difficulty_in_file("inactive","inactive","active","novize_active","master_inactive","legend_locked","possible_difficulties_16x16"))
						d_screen_novize_button.config( image = novize_button_inactive)
						d_screen_novize_button.image = novize_button_inactive

				if possible_difficulties_16x16[2] == "inactive":
						d_screen_legend_button = Button(root,image = legend_button_inactive,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
						d_screen_legend_button.place(relx=.665, rely= 0.45, anchor="center")
						d_screen_legend_button.config( image = legend_button_inactive)
						d_screen_legend_button.config( command = lambda:overwrite_difficulty_in_file("inactive","inactive","active","novize_inactive","master_inactive","legend_active","possible_difficulties_16x16"))
						d_screen_legend_button.image = legend_button_inactive
				elif possible_difficulties_16x16[2] == "legend_locked":
						d_screen_legend_button = Button(root,image = legend_button_locked,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
						d_screen_legend_button.place(relx=.665, rely= 0.45, anchor="center")
						d_screen_legend_button.config( image = legend_button_locked)
						d_screen_legend_button.image = legend_button_locked

			if possible_difficulties_16x16[2] == "legend_active":
				d_screen_legend_button = Button(root,image = legend_button_active,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
				d_screen_legend_button.place(relx=.665, rely= 0.45, anchor="center")
				d_screen_legend_button.config( image = legend_button_active)
				d_screen_legend_button.image = legend_button_active
				if possible_difficulties_16x16[0] == "novize_inactive":
					d_screen_novize_button = Button(root,image = novize_button_inactive,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
					d_screen_novize_button.place(relx=.33, rely= 0.435, anchor="center")
					d_screen_novize_button.config( command = lambda:overwrite_difficulty_in_file("inactive","inactive","active","novize_active","master_inactive","legend_inactive","possible_difficulties_16x16"))
					d_screen_novize_button.config( image = novize_button_inactive)
					d_screen_novize_button.image = novize_button_inactive
				elif possible_difficulties_16x16[1] == "master_inactive":
					d_screen_master_button = Button(root,image = master_button_inactive,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
					d_screen_master_button.place(relx=.5, rely= 0.45, anchor="center")
					d_screen_master_button.config( command = lambda:overwrite_difficulty_in_file("inactive","inactive","active","novize_inactive","master_active","legend_inactive","possible_difficulties_16x16"))
					d_screen_master_button.config( image = master_button_inactive)
					d_screen_master_button.image = master_button_inactive

	load_last_play_default()

	#____________Exit Button
	back_to_main_from_difficulty_button_active = PhotoImage(file = "images/MainmenueButtons/DScreenToMainMenuExitButton_active.png")
	back_to_main_from_difficulty_button_onclick = PhotoImage(file = "images/MainmenueButtons/DScreenToMainMenuExitButton_onClick.png")

	#___define appearance of button
	back_to_main_from_difficulty_button = Label(root,image = back_to_main_from_difficulty_button_active,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
	back_to_main_from_difficulty_button.place(relx=.774, rely= 0.141, anchor="center")

	#___button mouse hover functions
	def set_back_to_main_from_difficulty_button_hover(event):
		back_to_main_from_difficulty_button.config( image = back_to_main_from_difficulty_button_onclick)
		back_to_main_from_difficulty_button.image = back_to_main_from_difficulty_button_onclick

	def set_back_to_main_from_difficulty_button_active(event):
		back_to_main_from_difficulty_button.config( image = back_to_main_from_difficulty_button_active)
		back_to_main_from_difficulty_button.image = back_to_main_from_difficulty_button_active

	#___mouse hover and click label
	back_to_main_from_difficulty_button.bind("<Enter>", set_back_to_main_from_difficulty_button_hover)
	back_to_main_from_difficulty_button.bind("<Leave>", set_back_to_main_from_difficulty_button_active)
	back_to_main_from_difficulty_button_onclick_funktion = lambda x:load_main_menu(background_image)
	back_to_main_from_difficulty_button.bind("<Button-1>",back_to_main_from_difficulty_button_onclick_funktion)


	#____________Start Button
	start_game_button_active = PhotoImage(file = "images/MainmenueButtons/DScreen_StartButton_active.png")
	start_game_button_onclick = PhotoImage(file = "images/MainmenueButtons/DScreen_StartButton_onClick.png")

	#___define appearance of button
	start_game_button = Label(root,image = start_game_button_active,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
	start_game_button.place(relx=.5, rely= 0.675, anchor="center")

	#___button mouse hover functions
	def set_start_game_button_hover(event):
		start_game_button.config( image = start_game_button_onclick)
		start_game_button.image = start_game_button_onclick

	def set_start_game_button_active(event):
		start_game_button.config( image = start_game_button_active)
		start_game_button.image = start_game_button_active

	#___mouse hover and click label
	start_game_button.bind("<Enter>", set_start_game_button_hover)
	start_game_button.bind("<Leave>", set_start_game_button_active)
	start_game_button_onclick_funktion = lambda x:go_to_ingame_screen(background_image,savefile = None)
	start_game_button.bind("<Button-1>",start_game_button_onclick_funktion)
	
def exit_to_main_menu_from_highscore_sreen(background_image):
	background_image.pack()

	#__________________Exit Button

	back_to_main_from_highscore_button_active = PhotoImage(file = "images/MainmenueButtons/ScreenToMainMenuExitButton_active.png")

	back_to_main_from_highscore_button_onclick = PhotoImage(file = "images/MainmenueButtons/ScreenToMainMenuExitButton_onClick.png")

	#___define appearance of button
	back_to_main_from_highscore_button = Label(root,image = back_to_main_from_highscore_button_active,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
	back_to_main_from_highscore_button.place(relx=.86, rely= 0.151, anchor="center")

	#___button mouse hover functions
	def set_back_to_main_from_highscore_button_hover(event):
		back_to_main_from_highscore_button.config( image = back_to_main_from_highscore_button_onCcick)
		back_to_main_from_highscore_button.image = back_to_main_from_highscore_button_onclick

	def set_back_to_main_from_highscore_button_active(event):
		back_to_main_from_highscore_button.config( image = back_to_main_from_highscore_button_active)
		back_to_main_from_highscore_button.image = back_to_main_from_highscore_button_active

	#___mouse hover
	back_to_main_from_highscore_button.bind("<Enter>", set_back_to_main_from_highscore_button_hover)
	back_to_main_from_highscore_button.bind("<Leave>", set_back_to_main_from_highscore_button_active)
	back_to_main_from_highscore_button_onclick_funktion = lambda x:load_main_menu(background_image)
	back_to_main_from_highscore_button.bind("<Button-1>",back_to_main_from_highscore_button_onclick_funktion)

def go_to_highscore_screen(background_image):

	#_________________Replace background image
	background_image.pack_forget()
	background_image = Label(root,image = highscore_screen_bg_image)
	background_image.pack()
	#_________________Function Call: Exit to Main Menu
	exit_to_main_menu_from_highscore_sreen(background_image)


	# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ADD Highscore

def go_to_achievements_screen(background_image):

	#_________________Replace Background Image
	background_image.pack_forget()
	background_image = Label(root,image = achievement_screen_bg_image)
	background_image.pack()

	#_________________Next Buttons Functions
	def go_to_achievment_page(position = None,page_number = 1):

		#__Next Buttons
		next_r_button_active = PhotoImage(file = "images/MainmenueButtons/NextButtonR_active.png")
		next_r_button_onclick = PhotoImage(file = "images/MainmenueButtons/NextButtonR_onClick.png")

		next_l_button_active = PhotoImage(file = "images/MainmenueButtons/NextButtonL_active.png")
		next_l_button_onclick = PhotoImage(file = "images/MainmenueButtons/NextButtonL_onClick.png")

		next_r_button = Label(root,image = next_r_button_active,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
		next_l_button = Label(root,image = next_l_button_active,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)

		#__Adchievment Labels 4x4
		novize_4x4_image_locked = PhotoImage(file = "images/MainmenueButtons/AScreen_4x4Novize_locked.png")
		novize_4x4_image_active = PhotoImage(file = "images/MainmenueButtons/AScreen_4x4Novize_active.png")

		master_4x4_image_locked = PhotoImage(file = "images/MainmenueButtons/AScreen_4x4Master_locked.png")
		master_4x4_image_active = PhotoImage(file = "images/MainmenueButtons/AScreen_4x4Master_active.png")

		legend_4x4_image_locked = PhotoImage(file = "images/MainmenueButtons/AScreen_4x4Legend_locked.png")
		legend_4x4_image_active = PhotoImage(file = "images/MainmenueButtons/AScreen_4x4Legend_active.png")

		hints_4x4_image_locked = PhotoImage(file = "images/MainmenueButtons/AScreen_4x4Hints_locked.png")
		hints_4x4_image_active = PhotoImage(file = "images/MainmenueButtons/AScreen_4x4Hints_active.png")

		checks_4x4_image_locked = PhotoImage(file = "images/MainmenueButtons/AScreen_4x4Checks_locked.png")
		checks_4x4_image_active = PhotoImage(file = "images/MainmenueButtons/AScreen_4x4Checks_active.png")

		points_4x4_image_locked = PhotoImage(file = "images/MainmenueButtons/AScreen_4x4Points_locked.png")
		points_4x4_image_active = PhotoImage(file = "images/MainmenueButtons/AScreen_4x4Points_active.png")

		#__Adchievment Labels 9x9
		novize_9x9_image_locked = PhotoImage(file = "images/MainmenueButtons/AScreen_9x9Novize_locked.png")
		novize_9x9_image_active = PhotoImage(file = "images/MainmenueButtons/AScreen_9x9Novize_active.png")

		master_9x9_image_locked = PhotoImage(file = "images/MainmenueButtons/AScreen_9x9Master_locked.png")
		master_9x9_image_active = PhotoImage(file = "images/MainmenueButtons/AScreen_9x9Master_active.png")

		legend_9x9_image_locked = PhotoImage(file = "images/MainmenueButtons/AScreen_9x9Legend_locked.png")
		legend_9x9_image_active = PhotoImage(file = "images/MainmenueButtons/AScreen_9x9Legend_active.png")

		hints_9x9_image_locked = PhotoImage(file = "images/MainmenueButtons/AScreen_9x9Hints_locked.png")
		hints_9x9_image_active = PhotoImage(file = "images/MainmenueButtons/AScreen_9x9Hints_active.png")

		checks_9x9_image_locked = PhotoImage(file = "images/MainmenueButtons/AScreen_9x9Checks_locked.png")
		checks_9x9_image_active = PhotoImage(file = "images/MainmenueButtons/AScreen_9x9Checks_active.png")

		points_9x9_image_locked = PhotoImage(file = "images/MainmenueButtons/AScreen_9x9Points_locked.png")
		points_9x9_image_active = PhotoImage(file = "images/MainmenueButtons/AScreen_9x9Points_active.png")

		#__Adchievment Labels 16x16
		novize_16x16_image_locked = PhotoImage(file = "images/MainmenueButtons/AScreen_16x16Novize_locked.png")
		novize_16x16_image_active = PhotoImage(file = "images/MainmenueButtons/AScreen_16x16Novize_active.png")

		master_16x16_image_locked = PhotoImage(file = "images/MainmenueButtons/AScreen_16x16Master_locked.png")
		master_16x16_image_active = PhotoImage(file = "images/MainmenueButtons/AScreen_16x16Master_active.png")

		legend_16x16_image_locked = PhotoImage(file = "images/MainmenueButtons/AScreen_16x16Legend_locked.png")
		legend_16x16_image_active = PhotoImage(file = "images/MainmenueButtons/AScreen_16x16Legend_active.png")

		hints_16x16_image_locked = PhotoImage(file = "images/MainmenueButtons/AScreen_16x16Hints_locked.png")
		hints_16x16_image_active = PhotoImage(file = "images/MainmenueButtons/AScreen_16x16Hints_active.png")

		checks_16x16_image_locked = PhotoImage(file = "images/MainmenueButtons/AScreen_16x16Checks_locked.png")
		checks_16x16_image_active = PhotoImage(file = "images/MainmenueButtons/AScreen_16x16Checks_active.png")

		points_16x16_image_locked = PhotoImage(file = "images/MainmenueButtons/AScreen_16x16Points_locked.png")
		points_16x16_image_active = PhotoImage(file = "images/MainmenueButtons/AScreen_16x16Points_active.png")

		
		#___hide arrow
		if position != None:
			position.place_forget()

		#___define apperance of first page
		if page_number == 1:

			#___checking if user has unlocked achievement
			with open("set_achievements.csv", "r",newline='') as achievement_file:
				csv_reader = csv.reader(achievement_file)	

				for column in csv_reader:
					if column[0] == "4x4Novize":
						novize_4x4_achievement = Label(root,image = novize_4x4_image_locked,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
						if column[1] == "FALSE":
							novize_4x4_achievement.config( image = novize_4x4_image_locked)
							novize_4x4_achievement.place(relx=0.276, rely= 0.296, anchor="center")
							novize_4x4_achievement.image = novize_4x4_image_locked
						else:
							novize_4x4_achievement.config( image = novize_4x4_image_active)
							novize_4x4_achievement.place(relx=0.276, rely= 0.296, anchor="center")
							novize_4x4_achievement.image = novize_4x4_image_active
					elif column[0] == "4x4Master":
						master_4x4_achievement = Label(root,image = master_4x4_image_locked,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
						if column[1] == "FALSE":
							master_4x4_achievement.config( image = master_4x4_image_locked)
							master_4x4_achievement.place(relx=0.5, rely= 0.296, anchor="center")
							master_4x4_achievement.image = master_4x4_image_locked
						else:
							master_4x4_achievement.config( image = master_4x4_image_active)
							master_4x4_achievement.place(relx=0.5, rely= 0.296, anchor="center")
							master_4x4_achievement.image = master_4x4_image_active
					elif column[0] == "4x4Legend":
						legend_4x4_achievement = Label(root,image = legend_4x4_image_locked,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
						if column[1] == "FALSE":
							legend_4x4_achievement.config( image = legend_4x4_image_locked)
							legend_4x4_achievement.place(relx=0.724, rely= 0.296, anchor="center")
							legend_4x4_achievement.image = legend_4x4_image_locked
						else:
							legend_4x4_achievement.config( image = legend_4x4_image_active)
							legend_4x4_achievement.place(relx=0.724, rely= 0.296, anchor="center")
							legend_4x4_achievement.image = legend_4x4_image_active
					elif column[0] == "4x4Hints":
						hints_4x4_achievement = Label(root,image = hints_4x4_image_locked,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
						if column[1] == "FALSE":
							hints_4x4_achievement.config( image = hints_4x4_image_locked)
							hints_4x4_achievement.place(relx=0.276, rely= 0.52, anchor="center")
							hints_4x4_achievement.image = hints_4x4_image_locked
						else:
							hints_4x4_achievement.config( image = hints_4x4_image_active)
							hints_4x4_achievement.place(relx=0.276, rely= 0.52, anchor="center")
							hints_4x4_achievement.image = hints_4x4_image_active
					elif column[0] == "4x4Checks":
						checks_4x4_achievement = Label(root,image = checks_4x4_image_locked,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
						if column[1] == "FALSE":
							checks_4x4_achievement.config( image = checks_4x4_image_locked)
							checks_4x4_achievement.place(relx=0.5, rely= 0.52, anchor="center")
							checks_4x4_achievement.image = checks_4x4_image_locked
						else:
							checks_4x4_achievement.config( image = checks_4x4_image_active)
							checks_4x4_achievement.place(relx=0.5, rely= 0.52, anchor="center")
							checks_4x4_achievement.image = checks_4x4_image_active
					elif column[0] == "4x4Points":
						points_4x4_achievement = Label(root,image = points_4x4_image_locked,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
						if column[1] == "FALSE":
							points_4x4_achievement.config( image = points_4x4_image_locked)
							points_4x4_achievement.place(relx=0.724, rely= 0.52, anchor="center")
							points_4x4_achievement.image = points_4x4_image_locked
						else:
							points_4x4_achievement.config( image = points_4x4_image_active)
							points_4x4_achievement.place(relx=0.724, rely= 0.52, anchor="center")
							points_4x4_achievement.image = points_4x4_image_active
					elif column[0] == "9x9Novize":
						novize_9x9_achievement = Label(root,image = novize_9x9_image_locked,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
						if column[1] == "FALSE":
							novize_9x9_achievement.config( image = novize_9x9_image_locked)
							novize_9x9_achievement.place(relx=0.276, rely= 0.756, anchor="center")
							novize_9x9_achievement.image = novize_9x9_image_locked
						else:
							novize_9x9_achievement.config( image = novize_9x9_image_active)
							novize_9x9_achievement.place(relx=0.276, rely= 0.756, anchor="center")
							novize_9x9_achievement.image = novize_9x9_image_active
					elif column[0] == "9x9Master":
						master_9x9_achievement = Label(root,image = master_9x9_image_locked,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
						if column[1] == "FALSE":
							master_9x9_achievement.config( image = master_9x9_image_locked)
							master_9x9_achievement.place(relx=0.5, rely= 0.756, anchor="center")
							master_9x9_achievement.image = master_9x9_image_locked
						else:
							master_9x9_achievement.config( image = master_9x9_image_active)
							master_9x9_achievement.place(relx=0.5, rely= 0.756, anchor="center")
							master_9x9_achievement.image = master_9x9_image_active
					elif column[0] == "9x9Legend":
						legend_9x9_achievement = Label(root,image = legend_9x9_image_locked,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
						if column[1] == "FALSE":
							legend_9x9_achievement.config( image = legend_9x9_image_locked)
							legend_9x9_achievement.place(relx=0.724, rely= 0.756, anchor="center")
							legend_9x9_achievement.image = legend_9x9_image_locked
						else:
							legend_9x9_achievement.config( image = legend_9x9_image_active)
							legend_9x9_achievement.place(relx=0.724, rely= 0.756, anchor="center")
							legend_9x9_achievement.image = legend_9x9_image_active
			achievement_file.close()



			#_________________Next Page Button

			#___define position of button
			next_r_button.place(relx=0.872, rely= 0.5, anchor="center")

			#___button mouse hover functions
			def set_next_r_button_hover(event):
				next_r_button.config( image = next_r_button_onclick)
				next_r_button.image = next_r_button_onclick

			def set_next_r_button_active(event):
				next_r_button.config( image = next_r_button_active)
				next_r_button.image = next_r_button_active

			#___mouse hover
			next_r_button.bind("<Enter>", set_next_r_button_hover)
			next_r_button.bind("<Leave>", set_next_r_button_active)
			next_r_button_onclick_function = lambda x:go_to_achievment_page(next_r_button,2)
			next_r_button.bind("<Button-1>",next_r_button_onclick_function)

		#___define apperance of first page
		elif page_number == 2:

			#___checking if user has unlocked achievement
			with open("set_achievements.csv", "r",newline='') as achievement_file:
				csv_reader = csv.reader(achievement_file)	

				for column in csv_reader:
					if column[0] == "9x9Hints":
						hints_9x9_achievement = Label(root,image = hints_9x9_image_locked,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
						if column[1] == "FALSE":
							hints_9x9_achievement.config( image = hints_9x9_image_locked)
							hints_9x9_achievement.place(relx=0.276, rely= 0.296, anchor="center")
							hints_9x9_achievement.image = hints_9x9_image_locked
						else:
							hints_9x9_achievement.config( image = hints_9x9_image_active)
							hints_9x9_achievement.place(relx=0.276, rely= 0.296, anchor="center")
							hints_9x9_achievement.image = hints_9x9_image_active
					elif column[0] == "9x9Checks":
						checks_9x9_achievement = Label(root,image = checks_9x9_image_locked,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
						if column[1] == "FALSE":
							checks_9x9_achievement.config( image = checks_9x9_image_locked)
							checks_9x9_achievement.place(relx=0.5, rely= 0.296, anchor="center")
							checks_9x9_achievement.image = checks_9x9_image_locked
						else:
							checks_9x9_achievement.config( image = checks_9x9_image_active)
							checks_9x9_achievement.place(relx=0.5, rely= 0.296, anchor="center")
							checks_9x9_achievement.image = checks_9x9_image_active
					elif column[0] == "9x9Points":
						points_9x9_achievement = Label(root,image = points_9x9_image_locked,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
						if column[1] == "FALSE":
							points_9x9_achievement.config( image = points_9x9_image_locked)
							points_9x9_achievement.place(relx=0.724, rely= 0.296, anchor="center")
							points_9x9_achievement.image = points_9x9_image_locked
						else:
							points_9x9_achievement.config( image = points_9x9_image_active)
							points_9x9_achievement.place(relx=0.724, rely= 0.296, anchor="center")
							points_9x9_achievement.image = points_9x9_image_active
					elif column[0] == "16x16Novize":
						novize_16x16_achievement = Label(root,image = novize_16x16_image_locked,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
						if column[1] == "FALSE":
							novize_16x16_achievement.config( image = novize_16x16_image_locked)
							novize_16x16_achievement.place(relx=0.276, rely= 0.52, anchor="center")
							novize_16x16_achievement.image = novize_16x16_image_locked
						else:
							novize_16x16_achievement.config( image = novize_16x16_image_active)
							novize_16x16_achievement.place(relx=0.276, rely= 0.52, anchor="center")
							novize_16x16_achievement.image = novize_16x16_image_active
					elif column[0] == "16x16Master":
						master_16x16_achievement = Label(root,image = master_16x16_image_locked,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
						if column[1] == "FALSE":
							master_16x16_achievement.config( image = master_16x16_image_locked)
							master_16x16_achievement.place(relx=0.5, rely= 0.52, anchor="center")
							master_16x16_achievement.image = master_16x16_image_locked
						else:
							master_16x16_achievement.config( image = master_16x16_image_active)
							master_16x16_achievement.place(relx=0.5, rely= 0.52, anchor="center")
							master_16x16_achievement.image = master_16x16_image_active
					elif column[0] == "16x16Legend":
						legend_16x16_achievement = Label(root,image = legend_16x16_image_locked,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
						if column[1] == "FALSE":
							legend_16x16_achievement.config( image = legend_16x16_image_locked)
							legend_16x16_achievement.place(relx=0.724, rely= 0.52, anchor="center")
							legend_16x16_achievement.image = legend_16x16_image_locked
						else:
							legend_16x16_achievement.config( image = legend_16x16_image_active)
							legend_16x16_achievement.place(relx=0.724, rely= 0.52, anchor="center")
							legend_16x16_achievement.image = legend_16x16_image_active
					elif column[0] == "16x16Hints":
						hints_16x16_achievement = Label(root,image = hints_16x16_image_locked,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
						if column[1] == "FALSE":
							hints_16x16_achievement.config( image = hints_16x16_image_locked)
							hints_16x16_achievement.place(relx=0.276, rely= 0.756, anchor="center")
							hints_16x16_achievement.image = hints_16x16_image_locked
						else:
							hints_16x16_achievement.config( image = hints_16x16_image_active)
							hints_16x16_achievement.place(relx=0.276, rely= 0.756, anchor="center")
							hints_16x16_achievement.image = hints_16x16_image_active
					elif column[0] == "16x16Checks":
						checks_16x16_achievement = Label(root,image = checks_16x16_image_locked,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
						if column[1] == "FALSE":
							checks_16x16_achievement.config( image = checks_16x16_image_locked)
							checks_16x16_achievement.place(relx=0.5, rely= 0.756, anchor="center")
							checks_16x16_achievement.image = checks_16x16_image_locked
						else:
							checks_16x16_achievement.config( image = checks_16x16_image_active)
							checks_16x16_achievement.place(relx=0.5, rely= 0.756, anchor="center")
							checks_16x16_achievement.image = checks_16x16_image_active
					elif column[0] == "16x16Points":
						points_16x16_achievement = Label(root,image = points_16x16_image_locked,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
						if column[1] == "FALSE":
							points_16x16_achievement.config( image = points_16x16_image_locked)
							points_16x16_achievement.place(relx=0.724, rely= 0.756, anchor="center")
							points_16x16_achievement.image = points_16x16_image_locked
						else:
							points_16x16_achievement.config( image = points_16x16_image_active)
							points_16x16_achievement.place(relx=0.724, rely= 0.756, anchor="center")
							points_16x16_achievement.image = points_16x16_image_active
			achievement_file.close()

			#_________________Next Page Button

			#___define position of button
			next_l_button.place(relx=0.123, rely= 0.494, anchor="center")

			#___button mouse hover functions
			def set_next_l_button_onclick(event):
				next_l_button.config( image = next_l_button_onclick)
				next_l_button.image = next_l_button_onclick

			def set_next_l_button_active(event):
				next_l_button.config( image = next_l_button_active)
				next_l_button.image = next_l_button_active

			#___mouse hover
			next_l_button.bind("<Enter>", set_next_l_button_onclick)
			next_l_button.bind("<Leave>", set_next_l_button_active)
			next_l_button_onclick_function = lambda x:go_to_achievment_page(next_l_button,1)
			next_l_button.bind("<Button-1>",next_l_button_onclick_function)

	#_________________Function Call: Switch Page and Hide Arrow		
	go_to_achievment_page()
	#_________________Function Call: Exit to Main Menu	
	exit_to_main_menu_from_highscore_sreen(background_image)

def exit_game():
	root.quit()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> MAIN MENU >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

def load_main_menu(background_image = Label(root,image = main_menu_bg_image)):

	#__________________Background Image
	background_image.pack_forget()
	background_image = Label(root,image = main_menu_bg_image)
	background_image.pack()


	#___________________________________MainMenu Buttons_______________________________________________________________

	#___________________Continue Button

	continue_button_inactive = PhotoImage(file = "images/MainmenueButtons/ContinueButton_inactive.png")
	continue_button_active = PhotoImage(file = "images/MainmenueButtons/ContinueButton_active.png")
	continue_button_onclick = PhotoImage(file = "images/MainmenueButtons/ContinueButton_onClick.png")

	#___look for save file and return state
	def continue_button_state():
		# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!check if safe game is empty
		continue_button_state = continue_button_inactive
		return continue_button_state

	#___define appearance of button
	def continue_button_appearance():
		button_state = continue_button_state()
		if button_state != continue_button_inactive:
			continue_button = Button(root,image = continue_button_active,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
			continue_button.place(relx=.5, rely= 0.245, anchor="center")
			return continue_button
		else:
			continue_button = Button(root,image = continue_button_inactive,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
			continue_button.config( image = continue_button_inactive)
			continue_button.image = continue_button_inactive
			continue_button.place(relx=.5, rely= 0.245, anchor="center")

	#___mouse hover
	def continue_button_hover(continue_button):
		if continue_button  != None: 
			continue_button.bind("<Enter>", set_continue_button_onclick)
			continue_button.bind("<Leave>", set_continue_button_active)

	#___Countinue button mouse hover functions
	def set_continue_button_onclick(event):
		continue_button.config( image = continue_button_onclick)
		continue_button.config( command = lambda:continue_savegame(background_image))
		continue_button.image = continue_button_onclick

	def set_continue_button_active(event):
		continue_button.config( image = continue_button_active)
		continue_button.image = continue_button_active


	#__function call
	continue_button = continue_button_appearance()
	continue_button_hover(continue_button)

	#__________________Start Button

	start_button_active = PhotoImage(file = "images/MainmenueButtons/StartButton_active.png")
	start_button_onclick = PhotoImage(file = "images/MainmenueButtons/StartButton_onClick.png")

	#___define appearance of button
	start_button = Button(root,image = start_button_active,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
	start_button.place(relx=.5, rely= 0.345, anchor="center")

	#___button mouse hover functions
	def set_start_button_onclick(event):
		start_button.config( image = start_button_onclick)
		start_button.config( command = lambda:go_to_difficulty_screen(background_image))
		start_button.image = start_button_onclick

	def set_start_button_active(event):
		start_button.config( image = start_button_active)
		start_button.image = start_button_active

	#___mouse hover
	start_button.bind("<Enter>", set_start_button_onclick)
	start_button.bind("<Leave>", set_start_button_active)

	#___________________Highscore Button

	highscore_button_active = PhotoImage(file = "images/MainmenueButtons/HighscoreButton_active.png")
	highscore_button_onclick = PhotoImage(file = "images/MainmenueButtons/HighscoreButton_onClick.png")

	#___define appearance of button
	highscore_button = Button(root,image = highscore_button_active,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
	highscore_button.place(relx=.5, rely= 0.445, anchor="center")

	#___button mouse hover functions
	def set_highscore_button_onclick(event):
		highscore_button.config( image = highscore_button_onclick)
		highscore_button.config( command = lambda:go_to_highscore_screen(background_image))
		highscore_button.image = highscore_button_onclick

	def set_highscore_button_active(event):
		highscore_button.config( image = highscore_button_active)
		highscore_button.image = highscore_button_active

	#___mouse hover
	highscore_button.bind("<Enter>", set_highscore_button_onclick)
	highscore_button.bind("<Leave>", set_highscore_button_active)

	#___________________Achievements Button

	achievements_button_active = PhotoImage(file = "images/MainmenueButtons/AchievementsButton_active.png")
	achievements_button_onclick = PhotoImage(file = "images/MainmenueButtons/AchievementsButton_onClick.png")

	#___define appearance of button
	achievements_button = Button(root,image = achievements_button_active,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
	achievements_button.place(relx=.5, rely= 0.545, anchor="center")

	#___button mouse hover functions
	def set_achievements_button_onclick(event):
		achievements_button.config( image = achievements_button_onclick)
		achievements_button.config( command = lambda:go_to_achievements_screen(background_image))
		achievements_button.image = achievements_button_onclick

	def set_achievements_button_active(event):
		achievements_button.config( image = achievements_button_active)
		achievements_button.image = achievements_button_active

	#___mouse hover
	achievements_button.bind("<Enter>", set_achievements_button_onclick)
	achievements_button.bind("<Leave>", set_achievements_button_active)

	#___________________Exit Game Button

	exit_game_button_active = PhotoImage(file = "images/MainmenueButtons/ExitButton_active.png")
	exit_game_button_onclick = PhotoImage(file = "images/MainmenueButtons/ExitButton_onClick.png")

	#___define appearance of button
	exit_game_button = Button(root,image = exit_game_button_active,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
	exit_game_button.place(relx=.5, rely= 0.645, anchor="center")

	#___button mouse hover functions
	def set_exit_game_button_onclick(event):
		exit_game_button.config( image = exit_game_button_onclick)
		exit_game_button.config( command = exit_game)
		exit_game_button.image = exit_game_button_onclick

	def set_exit_game_button_active(event):
		exit_game_button.config( image = exit_game_button_active)
		exit_game_button.image = exit_game_button_active

	#___mouse hover
	exit_game_button.bind("<Enter>", set_exit_game_button_onclick)
	exit_game_button.bind("<Leave>", set_exit_game_button_active)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Final FUNCTION CALLS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

window(root)
load_main_menu()
root.mainloop()