# Calc.py:
# Calculater
from __future__ import division
from Tkinter import *
from ttk import *

class Calc():

	def __init__(self, master):
		global Num
		Num = StringVar()
		global Sym 
		Sym = StringVar()
		global Num_p
		Num_p = StringVar()

		master.geometry('360x300+200+200')
		master.title('Canon Calculator')
		master.resizable(False, False)
		#master.configure(background = '#F5F5F5') # WhiteSmoke color

		self.style = Style()
		self.style.configure('TFrame', background = '#0000FF') # Blue
		self.style.configure('Lower.TFrame', background = '#F5F5F5') 
		self.style.configure('Title.TLabel', background = '#808080', font = ('Arial', 11))
		self.style.configure('SubTitle.TLabel', background = '#808080', font = ('Arial', 8))
		self.style.configure('SubSubTitle.TLabel', background = '#808080', font = ('Arial', 5)) # Grey

		self.frame_dis = Frame(master) # create a display frame
		self.frame_dis.config(height = 50, width = 360, style = 'TFrame') # Blue
		self.frame_dis.pack()

		Label(self.frame_dis, text = "Canon", style = 'Title.TLabel').grid(row = 0, column = 0, stick = 'nsew')
		Label(self.frame_dis, text = "LS-82Z", style = 'SubTitle.TLabel').grid(row = 0, column = 1, stick = 'nsew')
		Label(self.frame_dis, text = "SOLAR AND BATTARY *#", style = 'SubSubTitle.TLabel').grid(row = 1, column = 0, columnspan = 2, stick = 'nsew')
		#canvas = Canvas(self.frame_dis)
		#canvas.grid(row = 0, column = 2, columnspan = 2, rowspan = 2)
		#canvas.create_rectangle(180, 5, 300, 10)

		screen = Entry(self.frame_dis, textvariable = Num, width = 12, font = ('Arial', 40))
		screen.grid(row = 2, column = 0, columnspan = 4, pady = 5)

		self.frame_func = Frame(master) # create a display frame
		self.frame_func.config(height = 260, width = 360, style = 'Lower.TFrame')
		self.frame_func.pack()

		button1 = Button(self.frame_func, text = '7', command = lambda: self.callback_num('7'), width = 8)
		button2 = Button(self.frame_func, text = '8', command = lambda: self.callback_num('8'), width = 8)
		button3 = Button(self.frame_func, text = '9', command = lambda: self.callback_num('9'), width = 8)
		button4 = Button(self.frame_func, text = 'x', command = lambda: self.callback_sym('*'), width = 8)
		button5 = Button(self.frame_func, text = '4', command = lambda: self.callback_num('4'), width = 8)
		button6 = Button(self.frame_func, text = '5', command = lambda: self.callback_num('5'), width = 8)
		button7 = Button(self.frame_func, text = '6', command = lambda: self.callback_num('6'), width = 8)
		button8 = Button(self.frame_func, text = '-', command = lambda: self.callback_sym('-'), width = 8)
		button9 = Button(self.frame_func, text = '1', command = lambda: self.callback_num('1'), width = 8)
		button10 = Button(self.frame_func, text = '2', command = lambda: self.callback_num('2'), width = 8)
		button11 = Button(self.frame_func, text = '3', command = lambda: self.callback_num('3'), width = 8)
		button12 = Button(self.frame_func, text = '+', command = lambda: self.callback_sym('+'), width = 8)
		button13 = Button(self.frame_func, text = '0', command = lambda: self.callback_num('0'), width = 8)
		button14 = Button(self.frame_func, text = '.', command = lambda: self.callback_num('.'), width = 8)
		button15 = Button(self.frame_func, text = '=', command = lambda: self.callback_result('='), width = 8)
		Button(self.frame_func, text = '/', command = lambda: self.callback_sym('/'), width = 8).grid(row = 0, column = 4, padx = 5, pady = 5,stick = 'nsew')
		Button(self.frame_func, text = 'Square', command = lambda: self.callback_sym('Square'), width = 8).grid(row = 1, column = 4, padx = 5, pady = 5,stick = 'nsew')
		Button(self.frame_func, text = 'Root', command = lambda: self.callback_sym('Root'), width = 8).grid(row = 2, column = 4, padx = 5, pady = 5,stick = 'nsew')
		Button(self.frame_func, text = 'CE', command = lambda: self.callback_sym('CE'), width = 8).grid(row = 3, column = 4, padx = 5, pady = 5,stick = 'nsew')

		button1.grid(row = 0, column = 0, padx = 5, pady = 5)
		button2.grid(row = 0, column = 1, padx = 5, pady = 5)
		button3.grid(row = 0, column = 2, padx = 5, pady = 5)
		button4.grid(row = 0, column = 3, padx = 5, pady = 5)
		button5.grid(row = 1, column = 0, padx = 5, pady = 5)
		button6.grid(row = 1, column = 1, padx = 5, pady = 5)
		button7.grid(row = 1, column = 2, padx = 5, pady = 5)
		button8.grid(row = 1, column = 3, padx = 5, pady = 5)
		button9.grid(row = 2, column = 0, padx = 5, pady = 5)
		button10.grid(row = 2, column = 1, padx = 5, pady = 5)
		button11.grid(row = 2, column = 2, padx = 5, pady = 5)
		button12.grid(row = 2, column = 3, rowspan = 2, padx = 5, pady = 5, stick = 'nsew')
		button13.grid(row = 3, column = 0, padx = 5, pady = 5)
		button14.grid(row = 3, column = 1, padx = 5, pady = 5)
		button15.grid(row = 3, column = 2, padx = 5, pady = 5)

	def callback_num(self, number):
		global Num
		global Num_p

		temp = Num.get() + number
		Num.set(temp)
		
	def callback_sym(self, string):
		global Num
		global Sym
		global Num_p
		if not Num.get() == '':
			Num_p.set(Num.get())
			Num.set('')
			if string == '-':
				Sym.set('-')
			elif string == '+':
				Sym.set('+')
			elif string == '*':
				Sym.set('*')
			elif string == '/':
				Sym.set('/')
			elif string == 'Square':
				Sym.set('Square')
			elif string == 'Root':
				Sym.set('Root')
			elif string == 'CE':
				Num.set('')
		else:
			pass

	def callback_result(self, string):
		global Num
		global Sym
		global Num_p
		if Sym.get() == '-' and string == '=':
			try:
				temp = float(Num_p.get()) - float(Num.get())
				Num.set(str(temp))
			except ValueError:
				pass
		elif Sym.get() == '+' and string == '=':
			try:
				temp = float(Num_p.get()) + float(Num.get())
				Num.set(str(temp))
			except ValueError:
				pass
		elif Sym.get() == '*' and string == '=':
			try:
				temp = float(Num_p.get()) * float(Num.get())
				Num.set(str(temp))
			except ValueError:
				pass
		elif Sym.get() == '/' and string == '=':
			try:
				temp = float(Num_p.get()) / float(Num.get())
				Num.set(str(temp))
			except ValueError:
				pass
		elif Sym.get() == 'Square' and string == '=':
			try:
				temp = float(Num_p.get()) ** (float(Num.get()))
				Num.set(str(temp))
			except ValueError:
				pass
		elif Sym.get() == 'Root' and string == '=':
			try:
				temp = float(Num_p.get()) ** (1/float(Num.get()))
				Num.set(str(temp))
			except ValueError:
				pass


def main():
	root = Tk()
	calculator = Calc(root)
	root.mainloop()

if __name__ == '__main__': main()
