from tkinter import *
import sqlite3

#database connection
conn = sqlite3.connect("StudentDB")
c = conn.cursor()

def showInfo():
	print("Name: "+str(nameVar.get()))
	print("GR Number: "+str(grnVar.get()))
	print("Year: "+str(yearVar.get()))
	print("Division: "+str(divVar.get()))
	print("Email: "+str(emailVar.get()))
	print("Parent Email: "+str(pemailVar.get()))

	c.execute("INSERT INTO StudentInfo VALUES(:name, :grn, :year, :div, :email)", 
	{'name':nameVar.get(), 'grn':int(grnVar.get()), 'year':yearVar.get(), 'div':divVar.get(), 'email':emailVar.get()})

	conn.commit()



root = Tk()
root.title("StudentUI")
root.geometry("400x400")

#labels
headerText = Label(root, text = "Student Info", fg = "green", font = ('Arial', 18))
nameLabel = Label(root, text = "Name: ")
grnLabel = Label(root, text = "GR Number: ")
yearLabel = Label(root, text = "Year: ")
divLabel = Label(root, text = "Division: ")
emailLabel = Label(root, text = "Email ID: ")
pemailLabel = Label(root, text = "Parent Email ID: ")

#variables
yearChoices = {"FY" , "SY", "TY", "BTech"}
yearVar = StringVar(root)
yearVar.set("NULL")
nameVar = StringVar(root)
grnVar = StringVar(root)
divVar = StringVar(root)
emailVar = StringVar(root)
pemailVar = StringVar(root)

#entry elements
nameEntry = Entry(root, textvariable = nameVar)
grnEntry = Entry(root, textvariable = grnVar)
yearMenu = OptionMenu(root, yearVar, *yearChoices)
divEntry = Entry(root, textvariable = divVar)
emailEntry = Entry(root, textvariable = emailVar)
pemailEntry = Entry(root, textvariable = pemailVar)
submitButton = Button(text = "Submit", fg = "Green", command = showInfo)
cancelButton = Button(text = "Cancel", fg = "Red", command = root.quit)


#placement
headerText.grid(row = 0, column = 1, pady = 10, sticky = NW)

nameLabel.grid(row = 1, pady = 10, padx = 10, sticky = E)
nameEntry.grid(row = 1, pady = 10, padx = 10, sticky = E, column = 1)

grnLabel.grid(row = 2, pady = 10, padx = 10, sticky = E)
grnEntry.grid(row = 2, pady = 10, padx = 10, sticky = E, column = 1)

yearLabel.grid(row = 3, pady = 10, padx = 10, sticky = E)
yearMenu.grid (row = 3, pady = 10, padx = 10, sticky = E, column = 1)

divLabel.grid(row = 4, pady = 10, padx = 10, sticky = E)
divEntry.grid (row = 4, pady = 10, padx = 10, sticky = E, column = 1)

emailLabel.grid(row = 5, pady = 10, padx = 10, sticky = E)
emailEntry.grid (row = 5, pady = 10, padx = 10, sticky = E, column = 1)

pemailLabel.grid(row = 6, pady = 10, padx = 10, sticky = E)
pemailEntry.grid (row = 6, pady = 10, padx = 10, sticky = E, column = 1)

submitButton.grid(row = 8, pady = 20, padx = 10, sticky = E)
cancelButton.grid(row = 8, pady = 20, padx = 10, sticky = E, column = 1)

root.mainloop()



