from tkinter import * 
 
root=Tk() 
 
 #Define the size of window or frame of application and text box
root.geometry( "300x300" )

#Set the Menu initially
menu= StringVar()
menu.set("What is your childs Asthma Action Plan (AAP) ?")

#Create a dropdown Menu
drop= OptionMenu(root, menu,"Long-term control" , "Caution" , "Quick relief rescue" , "Allergy")
drop.pack()
menu= StringVar()

#Returning a value from a function that is execueted from the Tkinter button
#Defining method to button 2
def method2(): 
    x="Flovent HFA Inhaler 2 puffs twice daily \nAdvair 45/21 2 puffs twice daily \nPulmicort Inhaler 2 puffs twice daily \nMontelukast 4mg once daily \nSingular 4mg once daily" 
    m.set(x) 
 
m=StringVar() 
b1=Button(root, text="long term", command=method2).pack() 
lb1=Label(root, text="...", textvariable=m).pack() 

#Defining method to button 3
def method3(): 
    x="Albuterol Inhaler 2 puffs every 4 hrs as needed \nFlovent HFA Inhaler 2 puffs twice daily \nAdvair 45/21 2 puffs twice daily" 
    m.set(x) 
 
m=StringVar() 
b2=Button(root, text="caution", command=method3).pack() 
lb2=Label(root, text="...", textvariable=m).pack() 
 
 #Defining method to button 4
def method4(): 
    x="Albuterol inhaler 4 puffs every 20 mins for 40 mins \nVentolin HFA 4 puffs every 20 min for 40 mins \nXopenox 2 puffs every 20 mins for 40 mins \nProventil 2 puffs every 20 mins for 40 mins \nProAir 2 puffs every 20 mins for 40 mins" 
    m.set(x) 
 
m=StringVar() 
b2=Button(root, text="quick relief", command=method4).pack() 
lb2=Label(root, text="...", textvariable=m).pack() 

#Defining method to button 5
def method5(): 
    x="Claritin 2.5-5mg daily \nZyrtec 2.5-5mg daily" 
    m.set(x) 
 
m=StringVar() 
b2=Button(root, text="allergies", command=method5).pack() 
lb2=Label(root, text="...", textvariable=m).pack() 

root.mainloop() 
