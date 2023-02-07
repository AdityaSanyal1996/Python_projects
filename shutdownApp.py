from tkinter import *
import os

def check(fname): #Checking if the user still wants to perform the operation
	c = Tk() #Reassuring Box
	c.geometry("300x120")
	c.config(bg = "white")
	text = Label(c, text = "Are you sure you want to perform the operation?")
	text.place(x = 20, y = 10)
	if (fname == "restart"):
		yes = Button(c, text = "Yes", font = ("Courier New", 15, "bold"), 
			relief = RAISED, cursor = "arrow", command = lambda: yes_perform("r"))
		yes.place(x = 50, y = 40, height = 30, width = 50)
		no = Button(c, text = "No", font = ("Courier New", 15, "bold"),
			relief = RAISED, cursor = "arrow",command = No)
		no.place(x = 150, y = 40, height = 30, width = 50)	 
	elif (fname == "restart_time"):
		yes = Button(c, text = "Yes", font = ("Courier New", 15, "bold"), 
			relief = RAISED, cursor = "arrow", command = lambda: yes_perform("rt"))
		yes.place(x = 50, y = 40, height = 30, width = 50)
		no = Button(c, text = "No", font = ("Courier New", 15, "bold"),
			relief = RAISED, cursor = "arrow",command = No)
		no.place(x = 150, y = 40, height = 30, width = 50)
	elif (fname == "logout"):
		yes = Button(c, text = "Yes", font = ("Courier New", 15, "bold"), 
			relief = RAISED, cursor = "arrow", command = lambda: yes_perform("lgt"))
		yes.place(x = 50, y = 40, height = 30, width = 50)
		no = Button(c, text = "No", font = ("Courier New", 15, "bold"),
			relief = RAISED, cursor = "arrow",command = No)
		no.place(x = 150, y = 40, height = 30, width = 50)
	elif (fname == "shutdown"):
		yes = Button(c, text = "Yes", font = ("Courier New", 15, "bold"), 
			relief = RAISED, cursor = "arrow", command = lambda: yes_perform("sd"))
		yes.place(x = 50, y = 40, height = 30, width = 50)		
		no = Button(c, text = "No", font = ("Courier New", 15, "bold"),
			relief = RAISED, cursor = "arrow",command = No)
		no.place(x = 150, y = 40, height = 30, width = 50)
	
def yes_perform(name):
	if (name == "r"):
		os.system("shutdown /r /t 1")
	elif (name == "rt"):
		os.system("shutdown /r /t 20")
	elif (name == "lgt"):
		os.system("shutdown -l")
	elif (name == "sd"):
		os.system("shutdown /s /t 1")	


def No():
	quit()

def restart(): # function for restarting the computer
	check("restart")

def restart_time(): # function for restarting the computer after 20 secs of delay
	check("restart_time")
	
def logout(): # function for logging out of the computer
	check("logout") 

def shutdown(): # function for shutting down the computer
	check("shutdown")

st = Tk() #Storing the Tk class in st variable
st.title("ShutDown App")
st.geometry("500x400")
st.config(bg = "purple")

#Restart Button
r_button = Button(st, text = "Restart", font = ("Courier New",15, "bold"),
		relief = RAISED, cursor = "arrow", command = restart)
r_button.place(x = 150, y = 50, height = 50, width = 200)

#Restart Time
rt_button = Button(st, text = "Restart Time", font = ("Courier New", 15, "bold"),
		relief = RAISED, cursor = "arrow", command = restart_time)
rt_button.place(x = 150, y = 125, height = 50, width = 200)

#Logout button
lg_button = Button(st, text = "Logout", font = ("Courier New", 15, "bold"),
		relief = RAISED, cursor = "arrow", command = logout)
lg_button.place(x = 150, y = 200, height = 50, width = 200)

#ShutDown button
st_button = Button(st, text = "ShutDown", font = ("Courier New", 15, "bold"),
		relief = RAISED, cursor = "arrow", command = shutdown)
st_button.place(x = 150, y = 275, height = 50, width = 200)


st.mainloop() #This creates the GUI based on the blocks of code above