#import libraries/data first (symptom > symptom combination > severity; 2nd tab: listed medication_dosing options) – drop down or selection option
# -- Verify library to import (pip, pandas)
#import statistics as s
#Login screen – Email or username & Password (at this stage, any input should allow entry)


#add admin sign ins if we want to go this direction for the treatment plan input vs. user inputting it...
admins = {'Joli':'Miracle','Jasmine':'Williams','Bryana':'Higginbotham'}

#consider repurposing for entering/selecting child's name for individualized mgmt - instances where parents have 2+ children with asthma
#kidprofiles = {'Isobel':[87,88,98], 
            #'Dakota':[88,67,93],
            #'Nboke':[90,88,78]}

#Must revamp the functions and include while loops, etc. Also, must ensure the file we're using for content is read/writeable for user updates to AAP and noteTracking, Likely to be: 
#editAAP(); 
#checkSymptoms() - Line of questions to pinpoint management plan
#noteTracking() - Simply documents note with date/time, likely can keep free text(easiest) or also offer choosing from options

def followup():
    print 

# Added escalating symptom mini tests
#Asks if they are having any Emergency level symptoms?
def final_sym():
    print(""" 

        [1] Medicine is not helping
        [2] Breathing is hard and fast
        [3] Nose opens wide
        [4] Trouble speaking
        [5] Ribs show
        [5] Tight chest
        [6] Coughing at night
        
        """)
    final_sym_input = input("Is your child experiencing any of the above symptoms? (Y/N): ")

            # checking for valid answer
    if final_sym_input.lower() != 'y' and final_sym_input.lower() != 'n':
        print("Invalid answer. Please answer 'Y' for yes, or 'N' for no.")
        self.final_sym()

            # conditional response for 'n'
    elif final_sym_input.lower() == 'n':
#possibly allow for another option to freetext symptom to note
        print("I understand your child is not experiencing any of these symptoms today.")
        print("""
                Based on the symptoms you previously noted your child is in the Caution zone. We recommend they take their quick relief medicine:
                
                Albuterol 2 puffs every 4-6 hours— 
                If symptoms do not improve in 1-2 hours — Contact your pediatrician.
                If symptoms worsen, increase to Danger level med management and get help from a provider right away. 
                If you cannot reach your pediatrician take your child to the ER.
                
                """)
        return final_sym() 
        # conditional response for 'y'
    elif final_sym_input.lower() == 'y': 
        print("I understand your child is experiencing one or more Danger zone symptoms today.")
        print("""
                Based on the symptoms you noted your child is in the Danger zone. 
                We recommend they take their quick relief medicine NOW:
                
                Albuterol 2 puffs every 30mins—1hour, not to exceed X.. 
                Get help from a provider NOW. If you cannot reach your pediatrician, take your child to the Emergency Department.
                """)
        return main()
    
        #providerinfo()  
    #return providerinfo() "What would you like to do for your child's asthma management?"  

def other_sym():
    other_sym_input = input("Is your child experiencing any other symptoms at this time? (Y/N): ")
    if other_sym_input.lower() != 'y' and other_sym_input.lower() != 'n':
        print("Invalid answer. Please answer 'Y' for yes, or 'N' for no.")
        self.other_sym()

            # conditional response for 'n'
    elif other_sym_input.lower() == 'n':
        print("""
                Based on the symptoms you noted, your child is in the Caution zone. We recommend they take their quick relief medicine:
                Albuterol 2 puffs every 4-6 hours— 
                If symptoms do not improve in 1-2 hours — Contact your pediatrician.
                If symptoms worsen, increase to Danger level med management and get help from a provider right away. 
                If you cannot reach your pediatrician take your child to the ER.
                
                """)
        return main()
            
            # conditional response for 'y'
    elif other_sym_input.lower() == 'y': 
        print("I understand your child is experiencing some of the previously listed symptoms and would like to ask if they are experiencing any others.")
        return final_sym()
            
        
            

def anysymptom():
        #Asks if they have any asthma/cold symptoms """
        #Altered output message        
    any_sym_input = input("Is your child experiencing any asthma/cold related symptoms today? (Y/N): ")

        # checking for valid answer
    if any_sym_input.lower() != 'y' and any_sym_input.lower() != 'n':                
        print("Invalid answer. Please answer 'Y' for yes, or 'N' for no.")
        anysymptom()

# conditional response for 'n'
    elif any_sym_input.lower() == 'n':
               #return main screen options
        print("I understand your child is not experiencing any symptoms today.")
        return main()
                    #return help menu "What would you like to do for your child's asthma management?" 
                
                # conditional response for 'y'
    elif any_sym_input.lower() == 'y': 
        first_sym() 
            
    #Asks if they are having any of the cautious level symptoms?
def first_sym():
    print(""" 

            [1] - First signs of cold
            [2] - Exposure to known trigger (allergen, weather, etc.)
            [3] - Cough
            [4] - Mild
            [5] - Tight chest
            [6] - Coughing at night
            
            """)
    first_sym_input = input("Is your child experiencing any of the above symptoms? (Y/N): ")

    # checking for valid answer
    if first_sym_input.lower() != 'y' and first_sym_input.lower() != 'n':
            print("Invalid answer. Please answer 'Y' for yes, or 'N' for no.")
            first_sym()

                # conditional response for 'n'
    elif first_sym_input.lower() == 'n':
                    #return main screen options
        print("I understand your child is not experiencing of these symptoms today.")
        return final_sym() 
                
                # conditional response for 'y'
    elif first_sym_input.lower() == 'y': 
        print("I understand your child is experiencing one or more Caution level symptoms today.")
        return other_sym()

    


def menuchoice():
        action = input('What would you like to do? (Enter a number) ')
            #Here we process their choice of what they want to do.
        if action == '1':
            print('You selected: Add or edit the medications for the Asthma Action Plan')
                #Bryanna - modify function for our program editAAP()
            return editAAP()
        elif action == '2':
            print('You selected: Check symptoms for treatment')
                # call on check symptoms function
            anysymptom()
        
        elif action == '3':
            print('You selected: Make a note')
                #noteTracking() - modify function to write note (append with time)
        elif action == '4':
            print('Exit')
                #exit() - return to initial login?
        else:
            print('Valid option not selected.') 
            return


def main():
        
    profilename = input('Please add your childs profile name: ')
        #Here we present our main menu options once a person logs in successfully.
    print("""
        What would you like to do for your childs Asthma Management right now?

        [1] - Add or edit the Asthma Action Plan
        [2] - Check symptoms for treatment need
        [3] - Note symptoms or moderate/emergent meds initiated
        [4] - Exit
        """)
    menuchoice()

#need to cause it to reprompt
#Login prompt to access based on allowed entries
login = input('Username: ')

if login in admins: 
 
    password = input('Password: ')
    if admins[login] == password:
        print('Welcome',login, "!")
    #now run the code
        while True:
            main()

#loop more appropriate to reprompt
else:
    print('Invalid username or password, please enter valid sign in.')




# Later ability - track all symptoms selected(listed), and document time entered (write to file)
    #Consider using this to log their inputs to a tally or list?

#Later - If DB working - Create list for symptom selection based on the menus
#Yes or No, later: Symptoms[1,2,3,4,5,6]
        
#def ask_questions(self):
    #self.any_sym()
    #self.first_sym()
    #self.other_sym()
    #self.final_sym()
    #return True


#if __name__ == '__main__':
    #il = Illness()
    #il.ask_questions()

#Now we define functions. Functions encapsulate logic into reusable recipes that can be executed whenever we need them by calling their name with parentheses.
