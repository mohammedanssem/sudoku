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
ingame4_screen_bg_image = PhotoImage(file = "images/Ingame4_Screen.png")
ingame9_screen_bg_image = PhotoImage(file = "images/Ingame9_Screen.png")
ingame16_screen_bg_image = PhotoImage(file = "images/Ingame16_Screen.png")
achievement_screen_bg_image = PhotoImage(file = "images/Achievement_Screen.png")
highscore_screen_bg_image = PhotoImage(file = "images/Highscore_Screen.png")
achievement_screen_bg_image = PhotoImage(file = "images/Achievement_Screen.png")


def go_to_ingame_screen(background_image):
	pass

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



	#___By clicking the start button the last user input will besaved
	def overwrite_difficulty_in_file(default_4x4 = "active",default_9x9 = "inactive",default_16x16 = "inactive",novize = "novize_active",master = "master_locked",legend = "legend_locked",target = None):



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


		with open("set_difficulty.csv", "w",newline='') as difficulty_file:
			csv_writer = csv.writer(difficulty_file)
			for item in upadated_difficulty_lst:
				csv_writer.writerow(item)

			difficulty_file.close()

		load_last_play_default()

	def load_last_play_default():

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

		#________Get Achievements to set update difficulty
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

		#__set fiel size button
		if default_4x4 == "active":
			#___Define appearance of 4x button set to inactive and call difficulty csv overwrite function
			d_screen_4x4_button = Button(root,image = d_screen_4x4_button_active,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
			d_screen_4x4_button.place(relx=.33, rely= 0.2675, anchor="center")
			d_screen_4x4_button.config( image = d_screen_4x4_button_active)
			d_screen_4x4_button.image = d_screen_4x4_button_active
			#___Define appearance of 9x9 button set to inactive and call difficulty csv overwrite function
			d_screen_9x9_button = Button(root,image = d_screen_9x9_button_inactive,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
			d_screen_9x9_button.place(relx=.5, rely= 0.2675, anchor="center")
			d_screen_9x9_button.config( image = d_screen_9x9_button_inactive)
			d_screen_9x9_button.config( command = lambda:overwrite_difficulty_in_file("inactive","active","inactive"))
			d_screen_9x9_button.image = d_screen_9x9_button_inactive
			#___Define appearance of 16x16 button set to inactive and call difficulty csv overwrite function
			d_screen_16x16_button = Button(root,image = d_screen_16x16_button_inactive,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
			d_screen_16x16_button.place(relx=.665, rely= 0.2675, anchor="center")
			d_screen_16x16_button.config( image = d_screen_16x16_button_inactive)
			d_screen_16x16_button.config( command = lambda:overwrite_difficulty_in_file("inactive","inactive","active"))
			d_screen_16x16_button.image = d_screen_16x16_button_inactive


			#__set difficulty button
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
			#___Define appearance of 4x4 button set to inactive and call difficulty csv overwrite function
			d_screen_4x4_button = Button(root,image = d_screen_4x4_button_inactive,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
			d_screen_4x4_button.place(relx=.33, rely= 0.2675, anchor="center")
			d_screen_4x4_button.config( image = d_screen_4x4_button_inactive)
			d_screen_4x4_button.config( command = lambda:overwrite_difficulty_in_file("active","inactive","inactive"))
			d_screen_4x4_button.image = d_screen_4x4_button_inactive

			#___Define appearance of 9x9 button set to inactive and call difficulty csv overwrite function
			d_screen_9x9_button = Button(root,image = d_screen_9x9_button_active,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
			d_screen_9x9_button.place(relx=.5, rely= 0.2675, anchor="center")
			d_screen_9x9_button.config( image = d_screen_9x9_button_active)
			d_screen_9x9_button.image = d_screen_9x9_button_active


			#___Define appearance of 16x16 button set to inactive and call difficulty csv overwrite function
			d_screen_16x16_button = Button(root,image = d_screen_16x16_button_inactive,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
			d_screen_16x16_button.place(relx=.665, rely= 0.2675, anchor="center")
			d_screen_16x16_button.config( image = d_screen_16x16_button_inactive)
			d_screen_16x16_button.config( command = lambda:overwrite_difficulty_in_file("inactive","inactive","active"))
			d_screen_16x16_button.image = d_screen_16x16_button_inactive

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
			#___Define appearance of 4x4 button set to inactive and call difficulty csv overwrite function
			d_screen_4x4_button = Button(root,image = d_screen_4x4_button_inactive,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
			d_screen_4x4_button.place(relx=.33, rely= 0.2675, anchor="center")
			d_screen_4x4_button.config( image = d_screen_4x4_button_inactive)
			d_screen_4x4_button.config( command = lambda:overwrite_difficulty_in_file("active","inactive","inactive"))
			d_screen_4x4_button.image = d_screen_4x4_button_inactive

			#___Define appearance of 9x9 button set to inactive and call difficulty csv overwrite function
			d_screen_9x9_button = Button(root,image = d_screen_9x9_button_inactive,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
			d_screen_9x9_button.place(relx=.5, rely= 0.2675, anchor="center")
			d_screen_9x9_button.config( image = d_screen_9x9_button_inactive)
			d_screen_9x9_button.config( command = lambda:overwrite_difficulty_in_file("inactive","active","inactive"))
			d_screen_9x9_button.image = d_screen_9x9_button_inactive


			#___Define appearance of 16x16 button set to inactive and call difficulty csv overwrite function
			d_screen_16x16_button = Button(root,image = d_screen_16x16_button_active,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
			d_screen_16x16_button.place(relx=.665, rely= 0.2675, anchor="center")
			d_screen_16x16_button.config( image = d_screen_16x16_button_active)
			d_screen_16x16_button.image = d_screen_16x16_button_active


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

	back_to_main_from_difficulty_button_onClick = PhotoImage(file = "images/MainmenueButtons/DScreenToMainMenuExitButton_onClick.png")

	#___Define appearance of continue button
	back_to_main_from_difficulty_button = Label(root,image = back_to_main_from_difficulty_button_active,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
	back_to_main_from_difficulty_button.place(relx=.774, rely= 0.141, anchor="center")

	#___Start button mouse hover functions
	def set_back_to_main_from_difficulty_button_hover(event):
		back_to_main_from_difficulty_button.config( image = back_to_main_from_difficulty_button_onClick)
		back_to_main_from_difficulty_button.image = back_to_main_from_difficulty_button_onClick

	def set_back_to_main_from_difficulty_button_active(event):
		back_to_main_from_difficulty_button.config( image = back_to_main_from_difficulty_button_active)
		back_to_main_from_difficulty_button.image = back_to_main_from_difficulty_button_active

	#___Mouse Hover
	back_to_main_from_difficulty_button.bind("<Enter>", set_back_to_main_from_difficulty_button_hover)
	back_to_main_from_difficulty_button.bind("<Leave>", set_back_to_main_from_difficulty_button_active)
	back_to_main_from_difficulty_button_onclick_funktion = lambda x:load_main_menu(background_image)
	back_to_main_from_difficulty_button.bind("<Button-1>",back_to_main_from_difficulty_button_onclick_funktion)


	#____________Start Button
	start_game_button_active = PhotoImage(file = "images/MainmenueButtons/DScreen_StartButton_active.png")

	start_game_button_onClick = PhotoImage(file = "images/MainmenueButtons/DScreen_StartButton_onClick.png")

	#___Define appearance of continue button
	start_game_button = Label(root,image = start_game_button_active,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
	start_game_button.place(relx=.5, rely= 0.675, anchor="center")

	#___Start button mouse hover functions
	def set_start_game_button_hover(event):
		start_game_button.config( image = start_game_button_onClick)
		start_game_button.image = start_game_button_onClick

	def set_start_game_button_active(event):
		start_game_button.config( image = start_game_button_active)
		start_game_button.image = start_game_button_active

	#___Mouse Hover
	start_game_button.bind("<Enter>", set_start_game_button_hover)
	start_game_button.bind("<Leave>", set_start_game_button_active)
	start_game_button_onclick_funktion = lambda x:go_to_ingame_screen(background_image)
	start_game_button.bind("<Button-1>",start_game_button_onclick_funktion)
	
def exit_to_main_menu_from_highscore_sreen(background_image):
	background_image.pack()
	#__________________Exit Button

	back_to_main_from_highscore_button_active = PhotoImage(file = "images/MainmenueButtons/ScreenToMainMenuExitButton_active.png")

	back_to_main_from_highscore_button_onClick = PhotoImage(file = "images/MainmenueButtons/ScreenToMainMenuExitButton_onClick.png")

	#___Define appearance of continue button
	back_to_main_from_highscore_button = Label(root,image = back_to_main_from_highscore_button_active,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
	back_to_main_from_highscore_button.place(relx=.86, rely= 0.151, anchor="center")

	#___Start button mouse hover functions
	def set_back_to_main_from_highscore_button_hover(event):
		back_to_main_from_highscore_button.config( image = back_to_main_from_highscore_button_onClick)
		back_to_main_from_highscore_button.image = back_to_main_from_highscore_button_onClick

	def set_back_to_main_from_highscore_button_active(event):
		back_to_main_from_highscore_button.config( image = back_to_main_from_highscore_button_active)
		back_to_main_from_highscore_button.image = back_to_main_from_highscore_button_active

	#___Mouse Hover
	back_to_main_from_highscore_button.bind("<Enter>", set_back_to_main_from_highscore_button_hover)
	back_to_main_from_highscore_button.bind("<Leave>", set_back_to_main_from_highscore_button_active)
	back_to_main_from_highscore_button_onclick_funktion = lambda x:load_main_menu(background_image)
	back_to_main_from_highscore_button.bind("<Button-1>",back_to_main_from_highscore_button_onclick_funktion)

def go_to_highscore_screen(background_image):

	#_________________Replace background image
	background_image.pack_forget()
	background_image = Label(root,image = highscore_screen_bg_image)
	background_image.pack()
	#_________________Calling Exit Button
	exit_to_main_menu_from_highscore_sreen(background_image)


	# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!ADD Highscore

def go_to_achievements_screen(background_image):

	#_________________Replace background image
	background_image.pack_forget()
	background_image = Label(root,image = achievement_screen_bg_image)
	background_image.pack()

	#_________________Next Buttons Functions
	def go_to_achievment_page(position = None,page_number = 1):
		
		next_r_button_active = PhotoImage(file = "images/MainmenueButtons/NextButtonR_active.png")
		next_r_button_onClick = PhotoImage(file = "images/MainmenueButtons/NextButtonR_onClick.png")

		next_l_button_active = PhotoImage(file = "images/MainmenueButtons/NextButtonL_active.png")
		next_l_button_onClick = PhotoImage(file = "images/MainmenueButtons/NextButtonL_onClick.png")

		next_r_button = Label(root,image = next_r_button_active,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
		next_l_button = Label(root,image = next_l_button_active,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)

		#__Adchievment Labels
		#_4x4
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

		#_9x9
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

		#_16x16
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


		
		

		if position != None:
			position.place_forget()

		if page_number == 1:

			#_________________Achievements
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
			#___Define appearance of button
			next_r_button.place(relx=0.872, rely= 0.5, anchor="center")


			#___Start button mouse hover functions
			def set_next_r_button_hover(event):
				next_r_button.config( image = next_r_button_onClick)
				next_r_button.image = next_r_button_onClick

			def set_next_r_button_active(event):
				next_r_button.config( image = next_r_button_active)
				next_r_button.image = next_r_button_active

			#___Mouse Hover
			next_r_button.bind("<Enter>", set_next_r_button_hover)
			next_r_button.bind("<Leave>", set_next_r_button_active)
			next_r_button_onclick_function = lambda x:go_to_achievment_page(next_r_button,2)
			next_r_button.bind("<Button-1>",next_r_button_onclick_function)



		elif page_number == 2:

			#_________________Achievements
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
			#___Define appearance of button
			next_l_button.place(relx=0.123, rely= 0.5, anchor="center")



			#___Start button mouse hover functions
			def set_next_l_button_onclick(event):
				next_l_button.config( image = next_l_button_onClick)
				next_l_button.image = next_l_button_onClick

			def set_next_l_button_active(event):
				next_l_button.config( image = next_l_button_active)
				next_l_button.image = next_l_button_active

			#___Mouse Hover
			next_l_button.bind("<Enter>", set_next_l_button_onclick)
			next_l_button.bind("<Leave>", set_next_l_button_active)
			next_l_button_onclick_function = lambda x:go_to_achievment_page(next_r_button,1)
			next_l_button.bind("<Button-1>",next_l_button_onclick_function)

	#_________________Calling to switch pages and hide arrows		
	go_to_achievment_page()
	#_________________Calling Exit Button
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

	continue_button_onClick = PhotoImage(file = "images/MainmenueButtons/ContinueButton_onClick.png")

	#___Look for save file and return state
	def continue_button_state():
		# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!check if safe game is empty
		continue_button_state = continue_button_inactive
		return continue_button_state

	#___Define appearance of continue button
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
	#___Mouse Hover
	def continue_button_hover(continue_button):
		if continue_button  != None: 
			continue_button.bind("<Enter>", set_continue_button_onclick)
			continue_button.bind("<Leave>", set_continue_button_active)

	#___Countinue button mouse hover functions
	def set_continue_button_onclick(event):
		continue_button.config( image = continue_button_onClick)
		continue_button.config( command = lambda:continue_savegame(background_image))
		continue_button.image = continue_button_onClick

	def set_continue_button_active(event):
		continue_button.config( image = continue_button_active)
		continue_button.image = continue_button_active


	#__Function call
	continue_button = continue_button_appearance()
	continue_button_hover(continue_button)

	#__________________Start Button

	start_button_active = PhotoImage(file = "images/MainmenueButtons/StartButton_active.png")

	start_button_onClick = PhotoImage(file = "images/MainmenueButtons/StartButton_onClick.png")

	#___Define appearance of continue button
	start_button = Button(root,image = start_button_active,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
	start_button.place(relx=.5, rely= 0.345, anchor="center")

	#___Start button mouse hover functions
	def set_start_button_onclick(event):
		start_button.config( image = start_button_onClick)
		start_button.config( command = lambda:go_to_difficulty_screen(background_image))
		start_button.image = start_button_onClick

	def set_start_button_active(event):
		start_button.config( image = start_button_active)
		start_button.image = start_button_active

	#___Mouse Hover
	start_button.bind("<Enter>", set_start_button_onclick)
	start_button.bind("<Leave>", set_start_button_active)

	#___________________Highscore Button

	highscore_button_active = PhotoImage(file = "images/MainmenueButtons/HighscoreButton_active.png")

	highscore_button_onClick = PhotoImage(file = "images/MainmenueButtons/HighscoreButton_onClick.png")

	#___Define appearance of continue button
	highscore_button = Button(root,image = highscore_button_active,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
	highscore_button.place(relx=.5, rely= 0.445, anchor="center")

	#___Start button mouse hover functions
	def set_highscore_button_onclick(event):
		highscore_button.config( image = highscore_button_onClick)
		highscore_button.config( command = lambda:go_to_highscore_screen(background_image))
		highscore_button.image = highscore_button_onClick

	def set_highscore_button_active(event):
		highscore_button.config( image = highscore_button_active)
		highscore_button.image = highscore_button_active

	#___Mouse Hover
	highscore_button.bind("<Enter>", set_highscore_button_onclick)
	highscore_button.bind("<Leave>", set_highscore_button_active)

	#___________________Achievements Button

	achievements_button_active = PhotoImage(file = "images/MainmenueButtons/AchievementsButton_active.png")

	achievements_button_onClick = PhotoImage(file = "images/MainmenueButtons/AchievementsButton_onClick.png")

	#___Define appearance of continue button
	achievements_button = Button(root,image = achievements_button_active,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
	achievements_button.place(relx=.5, rely= 0.545, anchor="center")

	#___Start button mouse hover functions
	def set_achievements_button_onclick(event):
		achievements_button.config( image = achievements_button_onClick)
		achievements_button.config( command = lambda:go_to_achievements_screen(background_image))
		achievements_button.image = achievements_button_onClick

	def set_achievements_button_active(event):
		achievements_button.config( image = achievements_button_active)
		achievements_button.image = achievements_button_active

	#___Mouse Hover
	achievements_button.bind("<Enter>", set_achievements_button_onclick)
	achievements_button.bind("<Leave>", set_achievements_button_active)

	#___________________Exit Game Button

	exit_game_button_active = PhotoImage(file = "images/MainmenueButtons/ExitButton_active.png")

	exit_game_button_onClick = PhotoImage(file = "images/MainmenueButtons/ExitButton_onClick.png")

	#___Define appearance of continue button
	exit_game_button = Button(root,image = exit_game_button_active,highlightthickness = 0, bd = 0,relief = FLAT,justify = CENTER)
	exit_game_button.place(relx=.5, rely= 0.645, anchor="center")

	#___Start button mouse hover functions
	def set_exit_game_button_onclick(event):
		exit_game_button.config( image = exit_game_button_onClick)
		exit_game_button.config( command = exit_game)
		exit_game_button.image = exit_game_button_onClick

	def set_exit_game_button_active(event):
		exit_game_button.config( image = exit_game_button_active)
		exit_game_button.image = exit_game_button_active

	#___Mouse Hover
	exit_game_button.bind("<Enter>", set_exit_game_button_onclick)
	exit_game_button.bind("<Leave>", set_exit_game_button_active)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Final FUNCTION CALLS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

window(root)
load_main_menu()
root.mainloop()