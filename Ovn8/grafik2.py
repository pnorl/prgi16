from tkinter import *

class Grafik:
	def __init__(self, root):
		self.frame = Frame(root)
		self.frame.pack()
		for i in range(20):
			knapp = Knapp(self.frame)

class Knapp(Button):
	def __init__(self, frame):
		self.frame = frame
		self.clicked = False

		Button.__init__(self, self.frame, bg="green", command=self.klick, width = 5, height = 5)
		self.pack()

	def klick(self):
		if (not self.clicked):
			self.configure(bg = "red")
		else:
			self.configure(bg = "green")
		self.clicked = not self.clicked

def main():
	root = Tk()
	Grafik(root)
	root.mainloop()

main()