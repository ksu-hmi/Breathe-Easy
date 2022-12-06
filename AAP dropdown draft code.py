#Import the required libraries
from tkinter import *

#Create an instance of tkinter frame
root = Tk()

#Define the size of window or frame
root.geometry( "300x300" )

#Set the Menu initially
menu= StringVar()
menu.set("What is your childs Asthma Action Plan (AAP) ?")

#Create a dropdown Menu
drop= OptionMenu(root, menu,"Long-term control" , "Caution" , "Quick relief rescue" , "Allergy")
drop.pack()

root.mainloop()

#This setting will creat an application and text box that will ask the patient for the current status for the minors asthma action plan (AAP).
#The options will follow: long-term control, caution, quick relief, allergy.





#be sure to mention that the patient is already familiar with the asthma action plan and what the language means (long term, caution, quick relief, etc) 
# - if not the language in the app would have to be specified 
