from tkinter import *
##custom frame/class

class MainGUI(Frame):
    def __init__(self,container):
        Frame.__init__(self,container,bg = "white")
        self.setupGUI()
        

    def setupGUI(self):
        self.display = Label(self, text = "", anchor=E, bg= "white", height=1, width = 7, font= ("arial", 45))
        self.display.grid(row=0,column=0,columnspan=4, sticky = E+W+N+S)
        self.pack(fill = BOTH, expand=1)
        
#(
        img = PhotoImage(file="abomb.png")
        newButton=Button(self,image=img,command=lambda: self.process("("))
        newButton.image = img
        newButton.grid(row=1,column=0, sticky = N+S+E+W)
        
#)
        img = PhotoImage(file="gelator")
        newButton=Button(self,image=img,command= lambda: self.process(")"))
        newButton.image=img
        newButton.grid(row=1,column=1, sticky = N+S+E+W)
        
#AC
        img = PhotoImage(file="kroaken")
        newButton=Button(self,image=img,command= lambda: self.process("AC"))
        newButton.image=img
        newButton.grid(row=1,column=2, sticky = N+S+E+W)
#Backspace
        img = PhotoImage(file="eric")
        newButton=Button(self,image=img,command= lambda: self.process("bak"))
        newButton.image=img
        newButton.grid(row=1,column=3, sticky = N+S+E+W)
        
#7
        img = PhotoImage(file="nachos")
        newButton=Button(self,image=img,command= lambda: self.process("7"))
        newButton.image=img
        newButton.grid(row=2,column=0, sticky = N+S+E+W)
        


            
            
           

        

        
            


            
#main code
#create the window

window= Tk()
window.title("The Reckoner")
#creatwe the frame or class object
g1 = MainGUI(window)




#display the gui and wait for ix
#window.mainloop()
