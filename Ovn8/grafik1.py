from tkinter import *
def click():
	print("klickade på knappen.")

def main():

	root = Tk()

	f = Frame(root)
	f.pack()

	clicks = 0

	knapp = Button(f, text="Button", command= click)
	knapp.pack()

	ruta = Label(f, text="0 clicks")
	ruta.pack()

	root.mainloop()

main()