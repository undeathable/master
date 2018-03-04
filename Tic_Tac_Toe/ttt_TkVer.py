# Tic Tac Toe Tkinter version:
from __future__ import division
from __future__ import print_function
from Tkinter import *
from ttk import *
import tkMessageBox

'''
	1(0, 0) 2(1, 0) 3(2, 0)
	4(0, 1) 5(1, 1) 6(2, 1)
	7(0, 2) 8(1, 2) 9(2, 2)
'''

def label(source, text, relx, rely):
	#storeObj = Button(source, text = text, command = command)
	storeObj = Label(source, textvariable = text, borderwidth = 10, relief = "ridge", anchor = 'center')
	#storeObj.pack(side = side, expand = YES, fill = BOTH)
	storeObj.place(relx = relx, rely = rely, relwidth = (1/3), relheight = (1/3))
	return storeObj

#def iFrame(source, side):
#	storeObj = Frame(source)
#	storeObj.pack(side = side, expand = YES, fill = BOTH)
#	return storeObj

def conver_num_to_rel(number):
	x = [0 if number % 3 == 1 else (1/3) if number % 3 == 2 else (2/3)]
	y = [0 if number in range(4) else (1/3) if number in range(4,7) else (2/3)]
	return x, y

class App(Frame): # the whole game screen is a big Frame

	def __init__(self, master = None):
		Frame.__init__(self, master)
		self.option_add('*Font', 'arial 30 bold')
		self.pack(expand = YES, fill = BOTH)
		self.master.title("Tic Tac Toe")

		self.display=[]
		self.dict = {} # this a dynamic way to store the labels created in the future

		for i in range(9):
			sv=StringVar()
			sv.set("")
			self.display.append(sv)		

		for AllBut in ("123","456","789"):
			#RowBut = iFrame(self, TOP)
			for OneBut in AllBut:
				#button(RowBut, display[int(OneBut) - 1].get(), LEFT, lambda e = int(OneBut): self.callback(e))
				x, y = conver_num_to_rel(int(OneBut))
				key = OneBut
				self.dict[key] = label(self, self.display[int(OneBut) - 1], x[0], y[0]) # Tkinter automatically adds an argument that has information about the event. 
				self.dict[key].bind('<Button-1>', lambda event, e = int(OneBut): self.callback(e))

	def callback(self, number):


		# first check whether this button is empty, if yes, change its text based on number of total empties, else don't change

		
		if self.display[number - 1].get() == "": # if this specific button is empty
			#print(number)
			list = [i.get() for i in self.display]
			#print(list)
			if list.count("") % 2 == 0:
				self.display[number - 1].set("X")
				self.dict[str(number)].config(foreground = ["red" if (self.display[int(number) - 1].get() == "O") else "black"][0])
			else:
				self.display[number - 1].set("O")
				self.dict[str(number)].config(foreground = ["red" if (self.display[int(number) - 1].get() == "O") else "black"][0])
		# second to check if it wins, if yes, pop up congrads, else, check full, if full, pop up due, else continue
		boolen, player = self.winCheck(self.display)
		if boolen: # if someone wins
			answer = tkMessageBox.askretrycancel(title = 'Result', message = 'Congradulations! Player: {}. \n Do you wanna PLAY agan?'.format(player))
			if answer: # if want to play agian, clean the format
				for i in range(9):
					self.display[i].set("")
			else: # don't want to play
				self.master.destroy()
		elif self.dueCheck(self.display): # if due
			answer = tkMessageBox.askretrycancel(title = 'Result', message = 'Due!!!\nDo you wanna PLAY agan?')
			if answer: # if want to play agian, clean the format
				for i in range(9):
					self.display[i].set("")
			else: # don't want to play
				self.master.destroy()

		#global display
		#print(number)
		#print(display[int(number) - 1].get())
		

	def winCheck(self, display):
		if display[0].get() == display[1].get() == display[2].get():
			if display[0].get() == "X":
				return True, "X"
			elif display[0].get() == "O":
				return True, "O"
		elif display[3].get() == display[4].get() == display[5].get() and not display[3].get() == "":
			if display[3].get() == "X":
				return True, "X"
			elif display[3].get() == "O":
				return True, "O"
		elif display[6].get() == display[7].get() == display[8].get() and not display[6].get() == "":
			if display[6].get() == "X":
				return True, "X"
			elif display[6].get() == "O":
				return True, "O"
		elif display[0].get() == display[3].get() == display[6].get() and not display[0].get() == "":
			if display[0].get() == "X":
				return True, "X"
			elif display[0].get() == "O":
				return True, "O"
		elif display[1].get() == display[4].get() == display[7].get() and not display[1].get() == "":
			if display[1].get() == "X":
				return True, "X"
			elif display[1].get() == "O":
				return True, "O"
		elif display[2].get() == display[5].get() == display[8].get() and not display[2].get() == "":
			if display[2].get() == "X":
				return True, "X"
			elif display[2].get() == "O":
				return True, "O"
		elif display[0].get() == display[4].get() == display[8].get() and not display[0].get() == "":
			if display[0].get() == "X":
				return True, "X"
			elif display[0].get() == "O":
				return True, "O"
		elif display[2].get() == display[4].get() == display[6].get() and not display[2].get() == "":
			if display[2].get() == "X":
				return True, "X"
			elif display[2].get() == "O":
				return True, "O"
		return False, "None"

	def dueCheck(self, display):
		list = [i.get() for i in display]		
		if list.count("") == 0:
			return True
		return False

def main():
	root = Tk()
	root.geometry('480x480+200+200')
	app = App(root)
	root.mainloop()

if __name__ == "__main__":
	main()

