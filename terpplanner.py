
# Terp Planner: helps a student org plan their event on campus
from argparse import ArgumentParser
import re
import sys
import pandas as pd
import matplotlib.pyplot as plt

class User:
    """Defines a user object for the person planning the event
    
    Attributes:
        fname(str): The first name of the person
        lname(str): The last name of the person
        email(str): The UMD email of the person
        org(str): The organization the event is for
        
    Methods:
        email_check(): Checks that the email is a UMD email
        org_check(): Checks that the org is one registered with UMD
    """
    
    def __init__(self, fname, lname, email, org):
        """
        Creates a User class. - Palrika 
            
        Args:  
            fname (str): The first name of the user.
            lname (str): The last name of the user.
            email (str): The email address of the user.
            org (str): The name of the organziation that he user is planning the event for.
            
        Side effects:
            A user object is created with the aforementioned attributes.
        """
        self.fname = fname
        self.lname = lname
        self.email = email
        self.org = org
        
    def email_check(self):
        """
        Uses a regex expression to check whether the email provided is a umd one.
        
        
        Raises:
            ValueError If the program does not find a matching email
        """
        patt1 = re.compile(r"^[^@]+@terpmail.umd.edu")
        patt2 = re.compile(r"^[^@]+@umd.edu")
        match1 = patt1.search(self.email)
        match2 = patt2.search(self.email)
        if match1 or match2:
            return True 
        else:
            raise ValueError("The email you provided is not valid.")
        
    def org_check(self, org_file):
        """ Rabindra
        Takes the org name
        with statement to read the file
        compares to make sure it's an active campus org, otherwises errors
        
        Args:
            org_file(str): file with a list of all active campus org
        
        Returns: 
            Boolean Value
        """
        org_list = []
        with open(org_file, 'r') as f:
            for line in f:
                org_list.append(line.strip())
        
        if self.org in org_list:
            return True
        else:
            return False
        
class Event:
    """ Plans the event for a student organization based on different categories.
    Attributes:
        location(str): The location of the event.
        evlength(float): The length of the event.
        evbudget(float): The budget of the event as specified by the user.
        food(bool): Determines whether the event will include food; default
        is False.
        equip(bool): Determines whether the event will need equipment;
        default is False.
        music(bool):Determines whether the event will need music;
        default is False.
        supplies(bool):Determines whether the event will need supplies;
        default is False.
        
    Methods: 
        loc_checker(str): Determines the best location to hold an event based on a given budget
        event_id)(set of INT):  Give an random event ID for each event, also add it to a set of IDS.
        budget_tracker(float):Keeps track of the budget to help the user to not overspend.  
        fundraise():If the budget tracker becomes negative print a statement that uses f-strings to say "this is how much you need".
        bud_vis(): Creates a diagram of the budget distribution.
    """
    def __init__(self, evlength, location, evbudget, room_bud,
                 foodbudget, equipbudget, musicbudget, suppliesbudget):
        """ Initializes the Event Class. - Sandra
        Args:
            location(str): The location of the event.
            evlength(float): The length of the event.
            evbudget(float): The budget of the event as specified by the user.
            food(bool): Determines whether the event will include food; default
            is False.
            equip(bool): Determines whether the event will need equipment;
            default is False.
            music(bool):Determines whether the event will need music;
            default is False.
            supplies(bool):Determines whether the event will need supplies;
            default is False.
            full_budget(list): A list or dictionary that holds the money per category
        Side effects:
            Creates the location, evlength, evbudget, food, equip, music, and 
            supplies attributes.
            This method will showcase the  Optional Parameter that will be used to 
            determine the budgets for the different event budget categories. 
        """
        self.length = evlength
        self.location=Event.loc_checker(room_bud)
        self.evbudget=Budget("Event",evbudget)
        self.food=Budget("Food",foodbudget)
        self.equip=Budget("Equipment", equipbudget)
        self.music=Budget("Music", musicbudget)
        self.supplies=Budget("Supplies", suppliesbudget)
        self.full_budget=[]
            
        
    def loc_checker(self, filepath, room_budget):
        """Determines the best location to hold an event based on a given budget. - Sandra
        Args: 
            filepath(str):A path to a file of locations on campus.
        Return:
            str: The specific location that is within the given budget
        Confirms if the location is on campus
        Will have the with statement for a txt file with UTF-8 encoding
        Ask the user on the budget for location
        User then picks the location that suits them
        This method will showcase a List Comprehension that gives the location options available 
        based on a given budget.
        """
        # We need to have this file made and hard-coded unfortunately.
        best_location = {}
        with open(filepath, "r",encoding= "utf-8") as f:
            for line in f:
                values= line.split(",")
                if float(values[1].strip()) <= self.loc_budget:
                    best_location[values[0]] = float(values[1].strip())
            return best_location 
        
    def event_id(self, idset): 
        """ Rabindra
            Give an rand event ID for each event, also add it to a set of IDS
            check intersection or sth of the new random number and the set of IDs
            if the event ID already exists, do another randomization
            
        Args:
            idset(set of INT): A set of event ids of events on campus
        
        Side Effects:
            Creates a new set of event ids for new events.
        
        Returns: event_id(int)
            
        """
    
    def budget_tracker(self, budget):
        """
        Budget tracker - Conditional Expression - Palrika
        Keeps track of the budget and calls the fundraise() method using a conditional
        expression if the budget falls below 0.   
            
        Args: 
            budget (float): User-inputted funds they have to plan the event.
            
        Side effect:
            Creates new budget object
        """
        if budget < 0:
            self.fundraise()
            
        
    def bud_vis(self):
        """
        Khushboo: pyplot usage, creates a diagram of the budget distribution     
        Side effects: 
            Shows a bar graph of spending
        """
        df = pd.dataframe(self.full_budget)
        plt.bar(df[0],df[1])

class Budget:
    """Tracks budget objects
    
    Attributes:
        type(str): The category of the budget
        money(float): The budgeted amount for that category
        
    Methods:
        bud_vis(): pyplot visualizaton of the budget distribution
    """
    
    def __init__(self, type, money):
        """
        Creates a budget object
        Args:
            type(str): The category of the budget
            money(float): The budgeted amount for that category
            
        Side efffects:
            Creates a budget object
        
        """
        self.type = type
        self.money = money
        
    def __sub__(self, other):
        """
        Sub magic() method - Magic Method - Palrika
        Compares the given budget with contemporary budget and raise error if the user overspends.
        
        Args:
            other(Budget): The amount of money the user uses while planning the event.
            
        Raises:
            type: If user overspends, this method will raise a type error.
        """
        
        check = self.budget - other.budget
        try:
            if check < 0:
                raise TypeError 
        except TypeError:
            print (f"In order to go forward with this event, you will need to raise ${check*-1}")
        else:
            return check
    

def main(fname, lname, email, orgname):
    """ Calculates the overall event budget based on user input and then writes the completed
    event to a different file. -Sandra
    Args:
        fname(str): The user's first name.
        lname(str): The user's last name.
        email(str): The user's email.
        orgname(str):The organization the user is associated with.
    Return:
        file: A txt file containg the completed event plan with budget details.
    The user will be prompted to fill in the corresponding information for their event to determine the
    budget calculations of the event.
    In order to achieve this we will impllement a loop
    Once the user is  done the program will write to a doc the info of the event (including budget)
    Do you want to plan another event? if yes, restart loop
    """
    welcom_msg=f"Welcome to Terp Planner {fname} {lname}!"
    user=User()
    if user.email_check(email)==True and user.org_check(orgname)==True:
        begin=input("Do you want to plan an event? (yes/no)")
        if begin == begin.lower("yes"):
            name=input("Please provide the name of the event: ")
            event=Event()
            budget=float(input("Please provide the budget for your event: "))
            if event.evbudget(budget) == True:
                event.budget_tracker()
            p1=float(input("Provide your budget for location: "))
            if event.location(p1)==True:
                s0=event.loc_checker()
            p2=input("Does your event have a food budget? (yes/no): ")
            if p2== p2.lower("yes"):
                if event.food(p2)==True:
                    food_bud=float(input("Please provide the budget for food: "))
                    s1=event.budget_tracker()-event.food(food_bud)
            p3=input("Do you want to have an equipment budget?(yes/no)")
            if p3==p3.lower("yes"):
                if event.equip(p3) == True:
                    equip_bud=float(input("Please provide the budget for equipment: "))
                    s2=event.budget_tracker()-event.equip(equip_bud)
            p4= input("Do you want to have a music budget? (yes/no)")
            if p4==p4.lower("yes"):
                if event.music == True:
                    music_bud=float(input("Please provide the budget for music: "))
                    s3=event.budget_tracker()-event.music(music_bud)
            p5= input("Do you want to have a supplies budget? (yes/no)")
            if p5==p5.lower("yes"):
                if event.supplies== True:
                    supp_bud=float(input("Please provide the budget for supplies: "))
                    s4=event.budget_tracker()-event.supplies(supp_bud)
                    

        
            
            
                       

        
        #else:
            #print("Please provide your budget to move forward.")
            
                
                
    
    f = open('event_plan', 'w', encoding='utf-8')
    f.write()
    f.close()

    

def parse_args(comline):
    """
    # KABINDRA Parses the arguments of the command line that are giving the user information. 
    
    Args :
        comline(str) : arguments users input in the command line
    # Shows the class and sequence unpacking
    """
    parser = ArgumentParser()
    parser.add_argument("fname", help="first name of the student")
    parser.add_argument("lname", help = "last name of the student")
    parser.add_argument("email", help = "email of the student")
    parser.add_argument("orgname", help = "name of the organization")

    return parser.parse_args(comline)

  
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    # I think for main, we should take the user's info and then everything else will be prompt based
    main(args.fname, args.lname, args.email, args.orgname)
