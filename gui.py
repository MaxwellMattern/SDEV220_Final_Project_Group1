import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

"""Constants"""
#File Paths
CIRCLE = "./imgs/Circle.png"
DIAMOND = "./imgs/Diamond.png"
OVAL = "./imgs/Oval.png"
RECT = "./imgs/Rect.png"
RISING_RECT = "./imgs/Rising_Rect.png"
TRAPIZOID = "./imgs/Trapizoid.png"
WAVY_RECT = "./imgs/Wavy_Rect.png"
#Easy-Change Settings
TOOLS_ICON_PADDING = (2,5,5,5)#Left,Up,Right,Down
TOOLS_BAR_SCALER = 40
CANVAS_PADDING =(10,5,5,5)#Left,Up,Right,Down
CANVAS_ITEM_PADDING =(5,5,5,5)#Left,Up,Right,Down
#Keybinds
KEY_CIRCLE = 'Q'
KEY_DIAMOND = 'W'
KEY_OVAL = 'E'
KEY_RECT = 'R'
KEY_RISING_RECT = 'T'
KEY_TRAPIZOID = 'Y'
KEY_WAVY_RECT = 'U'


#Test Variables
flowchart = ['Q','q','W','E','R','T','Y','U']

#Declare root & set basic properties
root = tk.Tk()
root.resizable(True, True)
root.title("Flowcharts!")
root.geometry("500x385")


#Load Images
circleIconImg = 	Image.open(CIRCLE).resize((		1*TOOLS_BAR_SCALER, 1*TOOLS_BAR_SCALER))
diamondIconImg = 	Image.open(DIAMOND).resize((	2*TOOLS_BAR_SCALER, 1*TOOLS_BAR_SCALER))
ovalIconImg = 		Image.open(OVAL).resize((		2*TOOLS_BAR_SCALER, 1*TOOLS_BAR_SCALER))
rectIconImg = 		Image.open(RECT).resize((		2*TOOLS_BAR_SCALER, 1*TOOLS_BAR_SCALER))
risingRectIconImg = Image.open(RISING_RECT).resize((2*TOOLS_BAR_SCALER, 1*TOOLS_BAR_SCALER))
trapizoidIconImg = 	Image.open(TRAPIZOID).resize((	2*TOOLS_BAR_SCALER, 1*TOOLS_BAR_SCALER))
wavyRectIconImg = 	Image.open(WAVY_RECT).resize((	2*TOOLS_BAR_SCALER, 1*TOOLS_BAR_SCALER))
#Convert Image to PhotoImage (Readable by Label)
circleIconLab = 	ImageTk.PhotoImage(circleIconImg)
diamondIconLab = 	ImageTk.PhotoImage(diamondIconImg)
ovalIconLab = 		ImageTk.PhotoImage(ovalIconImg)
rectIconLab = 		ImageTk.PhotoImage(rectIconImg)
risingRectIconLab = ImageTk.PhotoImage(risingRectIconImg)
trapizoidIconLab = 	ImageTk.PhotoImage(trapizoidIconImg)
wavyRectIconLab = 	ImageTk.PhotoImage(wavyRectIconImg)




"""Main Canvas"""
canvasFrame = ttk.Frame(root,padding=CANVAS_PADDING)

"""Update Flowchart Canvas"""
def update(flowchart=['']):
	for i, item in enumerate(flowchart):
		if(item.upper()==KEY_CIRCLE):
			itemLabel = ttk.Label(canvasFrame, image=circleIconLab,		padding=CANVAS_ITEM_PADDING)
		elif(item.upper()==KEY_DIAMOND):
			itemLabel = ttk.Label(canvasFrame, image=diamondIconLab,	padding=CANVAS_ITEM_PADDING)
		elif(item.upper()==KEY_OVAL):
			itemLabel = ttk.Label(canvasFrame, image=ovalIconLab,		padding=CANVAS_ITEM_PADDING)
		elif(item.upper()==KEY_RECT):
			itemLabel = ttk.Label(canvasFrame, image=rectIconLab,		padding=CANVAS_ITEM_PADDING)
		elif(item.upper()==KEY_RISING_RECT):
			itemLabel = ttk.Label(canvasFrame, image=risingRectIconLab,	padding=CANVAS_ITEM_PADDING)
		elif(item.upper()==KEY_TRAPIZOID):
			itemLabel = ttk.Label(canvasFrame, image=trapizoidIconLab,	padding=CANVAS_ITEM_PADDING)
		elif(item.upper()==KEY_WAVY_RECT):
			itemLabel = ttk.Label(canvasFrame, image=wavyRectIconLab,	padding=CANVAS_ITEM_PADDING)

		itemLabel.grid(column=0,row=i)


"""Update (Advanced) Flowchart Canvas"""
#This expects the format of:
#        [
#            [
#                Key,
#                Column,
#                Row
#            ],
#            [...],
#        ]
def updateAdv(flowchart=['']):
	for itemSet in flowchart:
		if(item[0]==KEY_CIRCLE):
			itemLabel = ttk.Label(canvasFrame, image=circleIconLab,		padding=CANVAS_ITEM_PADDING)
		elif(item[0]==KEY_DIAMOND):
			itemLabel = ttk.Label(canvasFrame, image=diamondIconLab,	padding=CANVAS_ITEM_PADDING)
		elif(item[0]==KEY_OVAL):
			itemLabel = ttk.Label(canvasFrame, image=ovalIconLab,		padding=CANVAS_ITEM_PADDING)
		elif(item[0]==KEY_RECT):
			itemLabel = ttk.Label(canvasFrame, image=rectIconLab,		padding=CANVAS_ITEM_PADDING)
		elif(item[0]==KEY_RISING_RECT):
			itemLabel = ttk.Label(canvasFrame, image=risingRectIconLab,	padding=CANVAS_ITEM_PADDING)
		elif(item[0]==KEY_TRAPIZOID):
			itemLabel = ttk.Label(canvasFrame, image=trapizoidIconLab,	padding=CANVAS_ITEM_PADDING)
		elif(item[0]==KEY_WAVY_RECT):
			itemLabel = ttk.Label(canvasFrame, image=wavyRectIconLab,	padding=CANVAS_ITEM_PADDING)

		itemLabel.grid(column=itemSet[1],row=itemSet[2])




"""Tool Bar"""
toolsFrame = ttk.Frame(root,borderwidth=4,relief="solid")

"""Tool Bar - Icons"""
#Place PhotoImage into Label
circleIcon = 		ttk.Label(toolsFrame, image=circleIconLab,		padding=TOOLS_ICON_PADDING)
diamondIcon = 		ttk.Label(toolsFrame, image=diamondIconLab,		padding=TOOLS_ICON_PADDING)
ovalIcon = 			ttk.Label(toolsFrame, image=ovalIconLab,		padding=TOOLS_ICON_PADDING)
rectIcon = 			ttk.Label(toolsFrame, image=rectIconLab,		padding=TOOLS_ICON_PADDING)
risingRectIcon = 	ttk.Label(toolsFrame, image=risingRectIconLab,	padding=TOOLS_ICON_PADDING)
trapizoidIcon =		ttk.Label(toolsFrame, image=trapizoidIconLab,	padding=TOOLS_ICON_PADDING)
wavyRectIcon = 		ttk.Label(toolsFrame, image=wavyRectIconLab,	padding=TOOLS_ICON_PADDING)
#Place Label on grid
circleIcon.grid(	column=0, row=0)
diamondIcon.grid(	column=0, row=1)
ovalIcon.grid(		column=0, row=2)
rectIcon.grid(		column=0, row=3)
risingRectIcon.grid(column=0, row=4)
trapizoidIcon.grid(	column=0, row=5)
wavyRectIcon.grid(	column=0, row=6)

"""Tool Bar - Key Labels"""
#Create Labels
circleLabel = 		ttk.Label(toolsFrame, text="Q")
diamondLabel = 		ttk.Label(toolsFrame, text="W")
ovalLabel = 		ttk.Label(toolsFrame, text="E")
rectLabel = 		ttk.Label(toolsFrame, text="R")
risingRectLabel = 	ttk.Label(toolsFrame, text="T")
trapizoidLabel = 	ttk.Label(toolsFrame, text="Y")
wavyRectLabel = 	ttk.Label(toolsFrame, text="U")
#Place Labels on grid
circleLabel.grid(		column=0,row=0)
diamondLabel.grid(		column=0,row=1)
ovalLabel.grid(			column=0,row=2)
rectLabel.grid(			column=0,row=3)
risingRectLabel.grid(	column=0,row=4)
trapizoidLabel.grid(	column=0,row=5)
wavyRectLabel.grid(		column=0,row=6)




""" Load flowchart **For Testing Purposes** """
# update(flowchart)


"""Place frames in root"""
toolsFrame.grid(column=0,row=0,sticky="NW")
canvasFrame.grid(column=1,row=0,sticky="N")

root.mainloop()