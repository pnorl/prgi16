from tkinter import *

class Spel:
	def __init__(self, root):
		self.frame = Frame(root)
		self.frame.pack()
		self.knappar = []
		self.skapaKnappar()

	def skapaKnappar(self):
		for i in range(20):
			knapp = Knapp(self.frame, str(i))
			self.knappar.append(knapp)
		self.packaKnappar()

	def packaKnappar(self):
		for i in range(len(self.knappar)):
			if i<10:
				self.knappar[i].grid(row = i, column = 0)
			else:
				self.knappar[i].grid(row = i-10, column = 1)

class Knapp(Button):
	def __init__(self, frame, t):
		self.marked = False
		Button.__init__(self, frame, text = t, bg = "green", command=self.klickad, height=3, width=2)
		#self.pack()

	def klickad(self):
		if (not self.marked):
			self.configure(bg="red")
		else:
			self.configure(bg="green")
		self.marked = not self.marked

def main():
	root = Tk()
	spelet = Spel(root)
	root.mainloop()

main()