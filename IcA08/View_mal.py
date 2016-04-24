from Tkinter import *

master = Tk()

master.title("River Crossing")
w = Canvas(master, width=900, height=900)
w.pack()

w.create_rectangle(200, 900, 750, 0,  fill="blue")
w.create_rectangle(200, 900, 0, 0, fill="green")
w.create_rectangle(900, 0, 750, 800, fill="green")
w.create_rectangle(400, 300, 201, 200, fill="brown") # Boat on the right side.

w.create_oval(150, 180, 180, 200, fill="yellow") # Chicken on the right side.
w.create_oval(130, 180, 160, 170, fill="white") # Grain on the right side.
w.create_oval(350, 250, 205, 210, fill="black") # Man in the boat on the right side.
w.create_oval(100, 130, 180, 150, fill="orange") # Fox on the right side.


bottomFrame = Frame(master)
bottomFrame.pack(side=BOTTOM)

#eget området nederst i vinduet tilegnet interaktive knapper

helpFrame = Frame(master)
helpFrame.pack(side=RIGHT)


getIn = Button(bottomFrame, text="Get in boat", bg="white", fg="black")
getOut = Button(bottomFrame, text="Get out of boat", bg="white", fg="black")
putinC = Button(bottomFrame, text="Put chicken in boat", bg="white", fg="black")
putinF = Button(bottomFrame, text="Put fox in boat", bg="white", fg="black")
putinG = Button(bottomFrame, text="Put grain in boat", bg="white", fg="black")
takeOutC = Button(bottomFrame, text="Take chicken out of boat", bg="white", fg="black")
takeOutF = Button(bottomFrame, text="Take fox out of boat", bg="white", fg="black")
takeOutG = Button(bottomFrame, text="Take grain out of boat", bg="white", fg="black")
crossRiver = Button(bottomFrame, text="Cross River", bg="black", fg="white")

help = Button(helpFrame, text="Help", bg="white", fg="red")

getIn.grid(row=0)
getOut.grid(row=0, column=1)
putinC.grid(row=0, column=2)
putinF.grid(row=0, column=4)
putinG.grid(row=0, column=5)
takeOutC.grid(row=1)
takeOutF.grid(row=1, column=2)
takeOutG.grid(row=1, column=5)
crossRiver.grid(row=2, column=2)

help.pack()

#Plasserer knappene


mainloop()