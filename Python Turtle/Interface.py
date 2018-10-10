
#import modules
from tkinter import *
from tkinter.ttk import Entry, OptionMenu
from turtle import *
from PIL import Image, ImageTk
from turtleFigures import *
from PIL import Image, ImageTk


#create an empty window and give its geometry
root = Tk()
root.title("Turtle Fractals")
root.geometry("350x410+300+300")


canvas = Canvas(root, background='white', height=138, width=400)
image_file = PhotoImage(file='python-logo.gif')
image = canvas.create_image(220,20,anchor='nw', image=image_file)
canvas.pack()



type = ["Tree", "Tree4", "Fern", "Koch", "Flake", "GasKet", "SwissFlag", "Square", "Circle", "Colorful"]
penColor = ["orange","black","blue","red","yellow","green", "purple","grey"]
previewPic = ["tree.png","tree4.png","fern.png", "koch.png", "flake.png","gasket.png","swissflag.png","square.png","circle.png","colorful.png"]

pen = Pen()
pen.color("white")
pen.speed(0)
pen.width(0)

screen = Screen()
screen.bgcolor("#688ac1")

#function==================================
def clearF():
    numberStr.set("")
    lengthStr.set("")
#end def

def ClearCanvasF():
    pen.reset()

def runF():
    n = int(numberStr.get())
    l = int(lengthStr.get())
    #print(typeStr)

    penColorIndex = penColor.index(penColorStr.get())

    if penColorIndex == 0:
        pen.color("orange")
    if penColorIndex == 1:
        pen.color("black")
    if penColorIndex == 2:
        pen.color("blue")
    if penColorIndex == 3:
        pen.color("red")
    if penColorIndex == 4:
        pen.color("yellow")
    if penColorIndex == 5:
        pen.color("green")
    if penColorIndex == 6:
        pen.color("purple")
    if penColorIndex == 7:
        pen.color("grey")   

    typeIndex = type.index(typeStr.get())
    
    if typeIndex == 0 :
        tree(n,l,pen)
    if typeIndex == 1 :
        tree4(n,l,pen)
    if typeIndex == 2 :
        fern(n,l,pen)
    if typeIndex == 3 :
        koch(n,l,pen)
    if typeIndex == 4:
        flake(n,l,pen)
    if typeIndex == 5 :
        gasket(n,l,pen)
    if typeIndex == 6 :
        swiss(n,l,pen)
    if typeIndex == 7 :
        square(n,l,pen)
    if typeIndex == 8 :
        circle(n,l,pen)
    if typeIndex == 9:
        colorful(n,l,pen)
    

def previewF():
    typeIndex = type.index(typeStr.get())

    if typeIndex == 0 :
        img = Image.open(previewPic[0])
    if typeIndex == 1:
        img = Image.open(previewPic[1])
    if typeIndex == 2:
        img = Image.open(previewPic[2])
    if typeIndex == 3:
        img = Image.open(previewPic[3])
    if typeIndex == 4:
        img = Image.open(previewPic[4])
    if typeIndex == 5:
        img = Image.open(previewPic[5])
    if typeIndex == 6:
        img = Image.open(previewPic[6])
    if typeIndex == 7:
        img = Image.open(previewPic[7])
    if typeIndex == 8:
        img = Image.open(previewPic[8])
    if typeIndex == 9:
        img = Image.open(previewPic[9])
        


    img = img.resize((180,150),Image.ANTIALIAS)
    tatras = ImageTk.PhotoImage(img)
    imgLabel.configure(image = tatras)
    imgLabel.image = tatras
    

#end def


#Frame===================================================
Frame = LabelFrame(root, text = "preview", bg="white")

img = Image.open(previewPic[0])
img = img.resize((180,150),Image.ANTIALIAS)
tatras = ImageTk.PhotoImage(img)
imgLabel = Label(Frame, image = tatras)
imgLabel.image = tatras
imgLabel.place(x=10,y=0,width=180,height=150)

Frame.place(x=50,y=170,width=250, height=200)


#===========================================
#        make the interface compoments
#===========================================

label = Label(root, text = " ")
label.grid(row = 0, column = 1, columnspan = 1)


typeLabel = Label(root, text = "Type")
typeLabel.grid(row = 1, column = 3,columnspan = 1)

typeStr = StringVar()
typeOptionMenu = OptionMenu(root, typeStr, type[0], *type)
typeOptionMenu.grid(row = 1, column = 4, columnspan = 1)

penLabel = Label(root, text = "PenColor")
penLabel.grid(row = 2, column = 3,columnspan = 1)

penColorStr = StringVar()
penColorOptionMenu = OptionMenu(root, penColorStr, penColor[0], *penColor)
penColorOptionMenu.grid(row = 2, column = 4,columnspan = 1)




#number===================================================================
numberLabel = Label(root, text = "Order")
numberLabel.grid(row = 3, column = 3, columnspan =1)

numberStr = StringVar()
numberEntry = Entry(root, textvariable = numberStr,width=15)
numberEntry.grid(row = 3, column = 4, columnspan = 1)


#length==================================================================
lengthLabel = Label(root, text = "Length")
lengthLabel.grid(row = 4, column = 3, columnspan = 1)

lengthStr = StringVar()
lengthEntry = Entry(root, textvariable = lengthStr,width=15)
lengthEntry.grid(row = 4, column = 4, columnspan = 1)


#button===================================================================
clearButton = Button(root, text = "Clear", command = clearF)
clearButton.place(x=110, y=130)

runButton = Button(root, text = "Run", command = runF)
runButton.place(x=170, y=130)

previewButton = Button(root, text = "Preview", command = previewF)
previewButton.place(x=225, y=375)

clearcanvasButton = Button(root, text = "ClearCanvas", command = ClearCanvasF)
clearcanvasButton.place(x=5, y=130)

#==============catch events==============
root.mainloop()
