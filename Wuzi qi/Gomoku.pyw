# Wuziqi.pyw

"""
This is a 20 by 20 Wu zi qi.

Algorithm:
1. Create a frame as the 20 by 20 chess panel
2. Add totally 400 labels on the panel with chess image on it.
3. For each click on specific label:
	a) it will first check if the text of label is empty: if yes, draw one player on it based on the total empty; if not, don't do anything
	b) winCheck for the panel (four directions): if True happens, pop up an MessageBox; if False, do Due check: if yes, pop up messagebox, if not, continue

RMK: Create objects for labels and App Frame; create functions -- WinCheck, DueCheck, callback for main algorithm
Panel:
(x, y)
 1(0, 0)  2(1, 0)  3(2, 0)... 20(19, 0)
21(0, 1) 22(1, 1) 23(2, 1)... 40(19, 1)
.
.
.
381(0, 19) 382(1, 19), 383(2, 19)... 399(19, 19) 
"""
from __future__ import division
from __future__ import print_function
from Tkinter import Tk, Canvas, BOTH, YES
from ttk import Frame
import tkMessageBox
from PIL import Image, ImageTk

class App(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)
        self.master.title("Gomoku Game")
        self.tags = [] # this is to store tags
        self.image = Image.open("C:\Users\Zhixiong Cheng\OneDrive\Documents\GitHub Projects\Wuzi qi\game.gif")
        self.img_copy= self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)
        #self.background = Label(self, image=self.background_image)
        self.background = Canvas(self, background = "red")
        self.background.pack(fill=BOTH, expand=YES)
        self.background.create_image(200,200, image = self.background_image)
        self.background.bind('<Configure>', self._resize_image)

        self.background.bind('<Button-1>', self._callback)
        #self.bind("<Configure>", self.enforce_aspect_ratio) # this is to make the root screen keep square
	'''
    def enforce_aspect_ratio(self, event):
    	new_width = event.width
    	new_height = int(event.width)
    	self.master.geometry("{}x{}".format(new_width,new_height))
	'''

    def _resize_image(self,event):
    	'''
    	if event.width <= event.height:
    		new_width, new_height = event.width, int(event.width)
    	else:
    		new_width, new_height = event.height, event.height
    	'''
    	new_width, new_height = event.width, event.height

    	self.image = self.img_copy.resize((new_width, new_height))
    	self.background_image = ImageTk.PhotoImage(self.image)
    	self.background.create_image(new_width//2,new_height//2, image = self.background_image)
    
    def _callback(self, event): # 27 is the distance between them when default, starting point as (15, 15), 7 is the radius of oval
		#print(event.x, event.y) 
		self.start_x = 15
		self.radius = 7
		self.diff = [27,27,25,27,26,26,27,26,28,25,28,25,27,25]
		
		iv_x, x_draw = self.create_intervals(event.x) # check if event.x in interval
		iv_y, y_draw = self.create_intervals(event.y)


		if iv_x and iv_y: # if players point in range
			if not self.background.gettags("{},{},{}".format(x_draw, y_draw, "white")) or not self.background.gettags("{},{},{}".format(x_draw, y_draw, "black")): # if this spot is empty, then draw
				if len(self.tags) % 2 == 0: # if this is white turn:
					oval = self.background.create_oval(sum(self.diff[:x_draw]) + self.start_x - self.radius\
						, sum(self.diff[:y_draw]) + self.start_x - self.radius\
						, sum(self.diff[:x_draw]) + self.start_x + self.radius\
						, sum(self.diff[:y_draw])+ self.start_x + self.radius, tags = "{},{},{}".format(x_draw, y_draw, "white"))
					self.background.itemconfigure("{},{},{}".format(x_draw, y_draw, "white"), fill = 'white') # the tags are stored in tuple
					#self.tags.append(self.background.gettags("{},{}.{}".format(x_draw, y_draw, "white")))
					self.tags.append("{},{},{}".format(x_draw, y_draw, "white"))
					if self.winCheck_hori(x_draw, y_draw, "white") or self.winCheck_verti(x_draw, y_draw, "white") or\
					 self.winCheck_slash(x_draw, y_draw, "white") or self.winCheck_slash_back(x_draw, y_draw, "white"): # if wins
						answer = tkMessageBox.askretrycancel(title = 'Result', message = 'Congradulations! Player: {}. \n Do you wanna PLAY agan?'.format("white"))
						if answer: # if want to play agian, clean the format
							for item in self.tags:
								self.background.delete(item)
							self.tags = []
						else: # don't want to play
							self.master.destroy()
					# elif dueCheck()

				else:
					oval = self.background.create_oval(sum(self.diff[:x_draw]) + self.start_x - self.radius\
						, sum(self.diff[:y_draw]) + self.start_x - self.radius\
						, sum(self.diff[:x_draw]) + self.start_x + self.radius\
						, sum(self.diff[:y_draw])+ self.start_x + self.radius, tags = "{},{},{}".format(x_draw, y_draw, "black"))
					self.background.itemconfigure("{},{},{}".format(x_draw, y_draw, "black"), fill = 'black') # the tags are stored in tuple
					#self.tags.append(self.background.gettags("{},{},{}".format(x_draw, y_draw, "black")))
					self.tags.append("{},{},{}".format(x_draw, y_draw, "black"))
					#print("{},{}".format(x_draw, y_draw))
					#print(self.tags)
					if self.winCheck_hori(x_draw, y_draw, "black") or self.winCheck_verti(x_draw, y_draw, "black") or\
					 self.winCheck_slash(x_draw, y_draw, "black") or self.winCheck_slash_back(x_draw, y_draw, "black"):
					 	answer = tkMessageBox.askretrycancel(title = 'Result', message = 'Congradulations! Player: {}. \n Do you wanna PLAY agan?'.format("black"))
						if answer: # if want to play agian, clean the format
							for item in self.tags:
								self.background.delete(item)
							self.tags = []
						else: # don't want to play
							self.master.destroy()

			
    
    def create_intervals(self, x):
		
		for i in range(15):
			if x in range(sum(self.diff[:i]) + self.start_x - self.radius, sum(self.diff[:i]) + self.start_x + self.radius):
				return True, i
		return False, 0

    def winCheck_hori(self, x_draw, y_draw, color):
    	# four directions:
		if not not self.background.gettags("{},{},{}".format(x_draw - 1, y_draw, color))and\
		not not self.background.gettags("{},{},{}".format(x_draw - 2, y_draw, color)) and\
		not not self.background.gettags("{},{},{}".format(x_draw - 3, y_draw, color)) and\
		not not self.background.gettags("{},{},{}".format(x_draw - 4, y_draw, color)):
			return True
		elif not not self.background.gettags("{},{},{}".format(x_draw - 1, y_draw, color))and\
		not not self.background.gettags("{},{},{}".format(x_draw - 2, y_draw, color)) and\
		not not self.background.gettags("{},{},{}".format(x_draw - 3, y_draw, color)) and\
		not not self.background.gettags("{},{},{}".format(x_draw + 1, y_draw, color)):
			return True
		elif not not self.background.gettags("{},{},{}".format(x_draw - 1, y_draw, color))and\
		not not self.background.gettags("{},{},{}".format(x_draw - 2, y_draw, color)) and\
		not not self.background.gettags("{},{},{}".format(x_draw + 1, y_draw, color)) and\
		not not self.background.gettags("{},{},{}".format(x_draw + 2, y_draw, color)):
			return True
		elif not not self.background.gettags("{},{},{}".format(x_draw - 1, y_draw, color))and\
		not not self.background.gettags("{},{},{}".format(x_draw + 1, y_draw, color)) and\
		not not self.background.gettags("{},{},{}".format(x_draw + 2, y_draw, color)) and\
		not not self.background.gettags("{},{},{}".format(x_draw + 3, y_draw, color)):
			return True
		elif not not self.background.gettags("{},{},{}".format(x_draw + 1, y_draw, color))and\
		not not self.background.gettags("{},{},{}".format(x_draw + 2, y_draw, color)) and\
		not not self.background.gettags("{},{},{}".format(x_draw + 3, y_draw, color)) and\
		not not self.background.gettags("{},{},{}".format(x_draw + 4, y_draw, color)):
			return True

		return False

    def winCheck_verti(self, x_draw, y_draw, color):
    	# four directions:
		if not not self.background.gettags("{},{},{}".format(x_draw, y_draw - 1, color))and\
		not not self.background.gettags("{},{},{}".format(x_draw, y_draw - 2, color)) and\
		not not self.background.gettags("{},{},{}".format(x_draw, y_draw - 3, color)) and\
		not not self.background.gettags("{},{},{}".format(x_draw, y_draw - 4, color)):
			return True
		elif not not self.background.gettags("{},{},{}".format(x_draw, y_draw - 1, color))and\
		not not self.background.gettags("{},{},{}".format(x_draw, y_draw - 2, color)) and\
		not not self.background.gettags("{},{},{}".format(x_draw, y_draw - 3, color)) and\
		not not self.background.gettags("{},{},{}".format(x_draw, y_draw + 1, color)):
			return True
		elif not not self.background.gettags("{},{},{}".format(x_draw, y_draw - 1, color))and\
		not not self.background.gettags("{},{},{}".format(x_draw, y_draw - 2, color)) and\
		not not self.background.gettags("{},{},{}".format(x_draw, y_draw + 1, color)) and\
		not not self.background.gettags("{},{},{}".format(x_draw, y_draw + 2, color)):
			return True
		elif not not self.background.gettags("{},{},{}".format(x_draw, y_draw - 1, color))and\
		not not self.background.gettags("{},{},{}".format(x_draw, y_draw + 1, color)) and\
		not not self.background.gettags("{},{},{}".format(x_draw, y_draw + 2, color)) and\
		not not self.background.gettags("{},{},{}".format(x_draw, y_draw + 3, color)):
			return True
		elif not not self.background.gettags("{},{},{}".format(x_draw, y_draw + 1, color))and\
		not not self.background.gettags("{},{},{}".format(x_draw, y_draw + 2, color)) and\
		not not self.background.gettags("{},{},{}".format(x_draw, y_draw + 3, color)) and\
		not not self.background.gettags("{},{},{}".format(x_draw, y_draw + 4, color)):
			return True

		return False

    def winCheck_slash(self, x_draw, y_draw, color):
    	# four directions:
		if not not self.background.gettags("{},{},{}".format(x_draw - 1, y_draw - 1, color))and\
		not not self.background.gettags("{},{},{}".format(x_draw - 2, y_draw - 2, color)) and\
		not not self.background.gettags("{},{},{}".format(x_draw - 3, y_draw - 3, color)) and\
		not not self.background.gettags("{},{},{}".format(x_draw - 4, y_draw - 4, color)):
			return True
		elif not not self.background.gettags("{},{},{}".format(x_draw - 1, y_draw - 1, color))and\
		not not self.background.gettags("{},{},{}".format(x_draw - 2, y_draw - 2, color)) and\
		not not self.background.gettags("{},{},{}".format(x_draw - 3, y_draw - 3, color)) and\
		not not self.background.gettags("{},{},{}".format(x_draw + 1, y_draw + 1, color)):
			return True
		elif not not self.background.gettags("{},{},{}".format(x_draw - 1, y_draw - 1, color))and\
		not not self.background.gettags("{},{},{}".format(x_draw - 2, y_draw - 2, color)) and\
		not not self.background.gettags("{},{},{}".format(x_draw + 1, y_draw + 1, color)) and\
		not not self.background.gettags("{},{},{}".format(x_draw + 2, y_draw + 2, color)):
			return True
		elif not not self.background.gettags("{},{},{}".format(x_draw - 1, y_draw - 1, color))and\
		not not self.background.gettags("{},{},{}".format(x_draw + 1, y_draw + 1, color)) and\
		not not self.background.gettags("{},{},{}".format(x_draw + 2, y_draw + 2, color)) and\
		not not self.background.gettags("{},{},{}".format(x_draw + 3, y_draw + 3, color)):
			return True
		elif not not self.background.gettags("{},{},{}".format(x_draw + 1, y_draw + 1, color))and\
		not not self.background.gettags("{},{},{}".format(x_draw + 2, y_draw + 2, color)) and\
		not not self.background.gettags("{},{},{}".format(x_draw + 3, y_draw + 3, color)) and\
		not not self.background.gettags("{},{},{}".format(x_draw + 4, y_draw + 4, color)):
			return True

		return False

    def winCheck_slash_back(self, x_draw, y_draw, color):
    	# four directions:
		if not not self.background.gettags("{},{},{}".format(x_draw + 1, y_draw - 1, color))and\
		not not self.background.gettags("{},{},{}".format(x_draw + 2, y_draw - 2, color)) and\
		not not self.background.gettags("{},{},{}".format(x_draw + 3, y_draw - 3, color)) and\
		not not self.background.gettags("{},{},{}".format(x_draw + 4, y_draw - 4, color)):
			return True
		elif not not self.background.gettags("{},{},{}".format(x_draw + 1, y_draw - 1, color))and\
		not not self.background.gettags("{},{},{}".format(x_draw + 2, y_draw - 2, color)) and\
		not not self.background.gettags("{},{},{}".format(x_draw + 3, y_draw - 3, color)) and\
		not not self.background.gettags("{},{},{}".format(x_draw - 1, y_draw + 1, color)):
			return True
		elif not not self.background.gettags("{},{},{}".format(x_draw + 1, y_draw - 1, color))and\
		not not self.background.gettags("{},{},{}".format(x_draw + 2, y_draw - 2, color)) and\
		not not self.background.gettags("{},{},{}".format(x_draw - 1, y_draw + 1, color)) and\
		not not self.background.gettags("{},{},{}".format(x_draw - 2, y_draw + 2, color)):
			return True
		elif not not self.background.gettags("{},{},{}".format(x_draw + 1, y_draw - 1, color))and\
		not not self.background.gettags("{},{},{}".format(x_draw - 1, y_draw + 1, color)) and\
		not not self.background.gettags("{},{},{}".format(x_draw - 2, y_draw + 2, color)) and\
		not not self.background.gettags("{},{},{}".format(x_draw - 3, y_draw + 3, color)):
			return True
		elif not not self.background.gettags("{},{},{}".format(x_draw - 1, y_draw + 1, color))and\
		not not self.background.gettags("{},{},{}".format(x_draw - 2, y_draw + 2, color)) and\
		not not self.background.gettags("{},{},{}".format(x_draw - 3, y_draw + 3, color)) and\
		not not self.background.gettags("{},{},{}".format(x_draw - 4, y_draw + 4, color)):
			return True

		return False




def main():
	root = Tk()
	root.geometry("400x400+100+100")
	root.resizable(False, False)
	app = App(root)
	app.pack(fill=BOTH, expand=YES)
	root.mainloop()

#logo = PhotoImage(file = 'C:\Users\Zhixiong Cheng\Desktop\game.gif')
#logo2 = logo.resize((width, height))
#image = canvas.create_image(w//2, h//2, image = logo)
#canvas.bind('<Configure>', self._resize_image)
#frame.pack(expand = YES, fill = BOTH)
#label(frame, relx = i/20, rely = i/20)

if __name__ == "__main__":
	main()