from tkinter import *
import sqlite3

#database connection
conn = sqlite3.connect("TeacherDB.db")
c = conn.cursor()

def showInfo():
	print("Name: "+str(nameVar.get()))
	print("Faculty Number: "+str(facultyVar.get()))
	#print("Year: "+str(yearVar.get()))
	#print("Division: "+str(divVar.get()))
	print("Email: "+str(emailVar.get()))
	#print("Parent Email: "+str(pemailVar.get()))
	print("Projector: "+str(projectorVar.get()))
	print("Preferences: "+str(preferencesVar.get()))

	c.execute("INSERT INTO TeacherInfo VALUES(:name, :faculty, :email, :projector, :preferences)", 
	{'name':nameVar.get(), 'faculty':int(facultyVar.get()), 'email':emailVar.get(), 'projector':int(projectorVar.get()), 'preferences':preferencesVar.get()})

	conn.commit()



root = Tk()
root.title("TeacherUI")
root.geometry("350x350")


#labels
headerText = Label(root, text = "Teacher Info", fg = "green", font = ('Arial', 18))
nameLabel = Label(root, text = "Name: ")
facultyLabel = Label(root, text = "GR Number: ")
yearLabel = Label(root, text = "Year: ")
#divLabel = Label(root, text = "Division: ")
emailLabel = Label(root, text = "Email ID: ")
#pemailLabel = Label(root, text = "Parent Email ID: ")
preferencesLabel = Label(root, text = "Schedule\nPreferences: ")

#variables
#yearChoices = {"FY" , "SY", "TY", "BTech"}
#yearVar = StringVar(root)
#yearVar.set("NULL")
nameVar = StringVar(root)
facultyVar = StringVar(root)
#divVar = StringVar(root)
emailVar = StringVar(root)
projectorVar = IntVar(root)
preferencesVar = StringVar(root)

#pemailVar = StringVar(root)

#entry elements
nameEntry = Entry(root, textvariable = nameVar)
facultyEntry = Entry(root, textvariable = facultyVar)
#yearMenu = OptionMenu(root, yearVar, *yearChoices)
#divEntry = Entry(root, textvariable = divVar)
emailEntry = Entry(root, textvariable = emailVar)
#pemailEntry = Entry(root, textvariable = pemailVar)
projectorCheckbox = Checkbutton(root, text = "Projector Required ", variable = projectorVar)
preferencesEntry = Entry(root, textvariable = preferencesVar, width = 20)
submitButton = Button(text = "Submit", fg = "Green", command = showInfo)
cancelButton = Button(text = "Cancel", fg = "Red", command = root.quit)


#placement

headerText.grid(row = 0, sticky = NW, column = 1, pady = 20)

nameLabel.grid(row = 1, pady = 10, padx = 10, sticky = E)
nameEntry.grid(row = 1, column = 1, pady = 10, padx = 10, sticky = E)

facultyLabel.grid(row = 2, pady = 10, padx = 10, sticky = E)
facultyEntry.grid(row = 2, column = 1, pady = 10, padx = 10, sticky = E)

#yearLabel.grid(row = 3)
#yearMenu.grid (row = 3, column = 1)

#divLabel.grid(row = 4)
#divEntry.grid (row = 4, column = 1)

emailLabel.grid(row = 5, pady = 10, padx = 10, sticky = E)
emailEntry.grid (row = 5, column = 1, pady = 10, padx = 10, sticky = E)

#pemailLabel.grid(row = 6)
#pemailEntry.grid (row = 6, column = 1)

projectorCheckbox.grid(row = 6, column = 1, sticky = W)

preferencesLabel.grid(row = 7, pady = 10, padx = 10, sticky = E)
preferencesEntry.grid(row = 7, column = 1, pady = 10, padx = 10, sticky = E, ipady = 10)

submitButton.grid(row = 8, column = 0, pady = 20, padx = 10)
cancelButton.grid(row = 8, column = 1, pady = 20, padx = 10)

root.mainloop()



